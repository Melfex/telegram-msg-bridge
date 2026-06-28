"""Tests for the access gate that enforces bot on/off and per-user blocking.

This guards the regression that originally let blocked users and an offline bot
keep working: the gate must actually deny ``Message``/``CallbackQuery`` updates
for non-owners.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Callable

import pytest

from enums import BotStatus, Status
from middleware.gate import GateMiddleware
from util import BotStateService
from tests.factories import (
    FakeI18n,
    make_callback_query,
    make_handler,
    make_message,
    make_user,
)

NON_OWNER_ID = 5


def _data(**overrides) -> dict:
    base: dict = {
        "event_from_user": make_user(NON_OWNER_ID),
        "bot_state": None,
        "scope": None,
        "i18n": FakeI18n(),
        "member": None,
    }
    base.update(overrides)
    return base


class TestGateBypass:
    async def test_owner_bypasses_gate(self, sudo_id: int) -> None:
        gate = GateMiddleware()
        handler = make_handler("ok")
        data = _data(event_from_user=make_user(sudo_id), bot_state=_offline())

        result = await gate(handler, make_callback_query(), data)

        assert result == "ok"
        handler.assert_awaited_once()

    async def test_bot_account_bypasses_gate(self) -> None:
        gate = GateMiddleware()
        handler = make_handler("ok")
        data = _data(event_from_user=make_user(7, is_bot=True), bot_state=_offline())

        result = await gate(handler, make_callback_query(), data)

        assert result == "ok"
        handler.assert_awaited_once()

    async def test_non_message_event_passes_through(self) -> None:
        gate = GateMiddleware()
        handler = make_handler("ok")
        # An Update/other object is neither Message nor CallbackQuery.
        result = await gate(handler, SimpleNamespace(), _data(bot_state=_offline()))

        assert result == "ok"
        handler.assert_awaited_once()


class TestGateOffline:
    async def test_offline_denies_callback(self) -> None:
        gate = GateMiddleware()
        handler = make_handler()
        callback = make_callback_query()

        result = await gate(handler, callback, _data(bot_state=_offline()))

        assert result is None
        handler.assert_not_awaited()
        callback.answer.assert_awaited_once()
        assert callback.answer.await_args.kwargs["show_alert"] is True

    async def test_state_is_read_through_from_db_when_unloaded(
        self, scope, new_scope: Callable
    ) -> None:
        # Persist OFFLINE, then hand the gate a *fresh* (unloaded) state cache.
        await scope.config.set_status(BotStatus.OFFLINE)
        await scope.persist()

        fresh_state = BotStateService()
        assert fresh_state.loaded is False

        gate = GateMiddleware()
        handler = make_handler()
        callback = make_callback_query()

        async with new_scope() as read_scope:
            result = await gate(
                handler, callback, _data(bot_state=fresh_state, scope=read_scope)
            )

        assert result is None
        handler.assert_not_awaited()
        assert fresh_state.loaded is True
        assert fresh_state.online is False


class TestGateBlocking:
    async def test_blocked_member_denied(self) -> None:
        gate = GateMiddleware()
        handler = make_handler()
        callback = make_callback_query()
        data = _data(
            bot_state=_online(),
            member=SimpleNamespace(status=Status.BLOCKED),
        )

        result = await gate(handler, callback, data)

        assert result is None
        handler.assert_not_awaited()
        callback.answer.assert_awaited_once()

    async def test_unblocked_member_allowed(self) -> None:
        gate = GateMiddleware()
        handler = make_handler("ok")
        data = _data(
            bot_state=_online(),
            member=SimpleNamespace(status=Status.UNBLOCKED),
        )

        result = await gate(handler, make_callback_query(), data)

        assert result == "ok"
        handler.assert_awaited_once()

    async def test_no_member_allowed_when_online(self) -> None:
        gate = GateMiddleware()
        handler = make_handler("ok")

        result = await gate(handler, make_callback_query(), _data(bot_state=_online()))

        assert result == "ok"
        handler.assert_awaited_once()


class TestGateMessageNotificationThrottling:
    async def test_message_deny_notifies_only_once_per_user(self) -> None:
        gate = GateMiddleware()
        handler = make_handler()
        message = make_message()
        data = _data(bot_state=_offline(), event_from_user=make_user(NON_OWNER_ID))

        first = await gate(handler, message, data)
        second = await gate(handler, message, data)

        assert first is None and second is None
        handler.assert_not_awaited()
        # The sticker + text are sent on the first denial only (TTL dedupe).
        message.answer_sticker.assert_awaited_once()
        message.answer.assert_awaited_once()


def _online() -> BotStateService:
    state = BotStateService()
    state.set_online(True)
    return state


def _offline() -> BotStateService:
    state = BotStateService()
    state.set_online(False)
    return state
