"""Unit tests for the rate-limited, fault-tolerant broadcaster.

``asyncio.sleep`` is patched out so the rate-limiting/retry timing logic can be
asserted without slowing the suite down
"""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

import util.broadcaster as broadcaster_module
from util import Broadcaster
from tests.factories import bad_request_error, retry_after_error


@pytest.fixture
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> AsyncMock:
    """Replace ``asyncio.sleep`` inside the broadcaster with an awaitable spy"""
    sleep = AsyncMock()
    monkeypatch.setattr(broadcaster_module.asyncio, "sleep", sleep)
    return sleep


def _bot(copy_side_effect=None, copy_return=None) -> AsyncMock:
    bot = AsyncMock()
    if copy_side_effect is not None:
        bot.copy_message.side_effect = copy_side_effect
    else:
        bot.copy_message.return_value = copy_return
    return bot


class TestBroadcasterHappyPath:
    async def test_all_recipients_succeed(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_return=None)
        result = await Broadcaster(bot).run(
            from_chat_id=1, message_id=2, user_ids=[10, 20, 30]
        )

        assert (result.total, result.sent, result.failed) == (3, 3, 0)
        assert bot.copy_message.await_count == 3

    async def test_empty_recipient_list(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_return=None)
        result = await Broadcaster(bot).run(from_chat_id=1, message_id=2, user_ids=[])

        assert (result.total, result.sent, result.failed) == (0, 0, 0)
        bot.copy_message.assert_not_awaited()
        no_sleep.assert_not_awaited()


class TestBroadcasterFailures:
    async def test_api_error_counts_as_failed(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_side_effect=[None, bad_request_error(), None])
        result = await Broadcaster(bot).run(
            from_chat_id=1, message_id=2, user_ids=[10, 20, 30]
        )

        assert (result.total, result.sent, result.failed) == (3, 2, 1)


class TestBroadcasterRetryAfter:
    async def test_retry_then_success(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_side_effect=[retry_after_error(3), None])
        result = await Broadcaster(bot).run(
            from_chat_id=1, message_id=2, user_ids=[10]
        )

        assert (result.sent, result.failed) == (1, 0)
        assert bot.copy_message.await_count == 2
        no_sleep.assert_awaited_once_with(3)

    async def test_retry_then_permanent_failure(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_side_effect=[retry_after_error(3), bad_request_error()])
        result = await Broadcaster(bot).run(
            from_chat_id=1, message_id=2, user_ids=[10]
        )

        assert (result.sent, result.failed) == (0, 1)
        assert bot.copy_message.await_count == 2


class TestBroadcasterRateLimiting:
    async def test_sleeps_between_batches(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_return=None)
        
        result = await Broadcaster(bot, per_second=2).run(
            from_chat_id=1, message_id=2, user_ids=[1, 2, 3, 4, 5]
        )

        assert result.sent == 5
        assert no_sleep.await_count == 2
        no_sleep.assert_awaited_with(1.0)

    async def test_single_batch_has_no_pause(self, no_sleep: AsyncMock) -> None:
        bot = _bot(copy_return=None)
        await Broadcaster(bot, per_second=20).run(
            from_chat_id=1, message_id=2, user_ids=[1, 2, 3]
        )
        no_sleep.assert_not_awaited()

    def test_per_second_is_clamped_to_at_least_one(self) -> None:
        assert Broadcaster(AsyncMock(), per_second=0)._per_second == 1
        assert Broadcaster(AsyncMock(), per_second=-5)._per_second == 1
