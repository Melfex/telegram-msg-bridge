from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import TYPE_CHECKING, Iterable

from aiogram.exceptions import TelegramAPIError, TelegramRetryAfter
from structlog import get_logger

if TYPE_CHECKING:
    from aiogram import Bot

logger = get_logger(__name__)


@dataclass(slots=True)
class BroadcastResult:
    total: int
    sent: int
    failed: int


class Broadcaster:
    """Rate-limited, fault-tolerant message broadcaster"""

    def __init__(self, bot: Bot, *, per_second: int = 20) -> None:
        self._bot = bot
        self._per_second = max(1, per_second)

    async def run(
        self,
        *,
        from_chat_id: int,
        message_id: int,
        user_ids: Iterable[int],
    ) -> BroadcastResult:
        """Copy ``message_id`` from ``from_chat_id`` to every id in ``user_ids``"""
        recipients = list(user_ids)
        sent = 0

        for start in range(0, len(recipients), self._per_second):
            batch = recipients[start : start + self._per_second]
            outcomes = await asyncio.gather(
                *(self._send_one(uid, from_chat_id, message_id) for uid in batch)
            )
            sent += sum(outcomes)

            if start + self._per_second < len(recipients):
                await asyncio.sleep(1.0)

        return BroadcastResult(
            total=len(recipients),
            sent=sent,
            failed=len(recipients) - sent,
        )

    async def _send_one(
        self,
        user_id: int,
        from_chat_id: int,
        message_id: int,
    ) -> bool:
        try:
            await self._bot.copy_message(
                chat_id=user_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
            )
            return True
        except TelegramRetryAfter as error:
            await asyncio.sleep(error.retry_after)
            try:
                await self._bot.copy_message(
                    chat_id=user_id,
                    from_chat_id=from_chat_id,
                    message_id=message_id,
                )
                return True
            except TelegramAPIError:
                return False
        except TelegramAPIError:
            return False


__all__ = [
    "Broadcaster",
    "BroadcastResult",
]
