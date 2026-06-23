from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Awaitable, Callable, Final, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.types import Message, ReplyKeyboardRemove
from cachebox import TTLCache

from config import settings
from enums import Throttle, StickerID

if TYPE_CHECKING:
    from aiogram.types import TelegramObject
    from aiogram_i18n import I18nContext
    from util import DeleteAfter


class TTLtMiddleware(BaseMiddleware):
    """
    TTL limiting middleware with temporary blocking

    tracks user message frequency. if a user exceeds `MAX` messages within
    `WINDOW` seconds (configured in ThrottleEnum), they are blocked for
    `BLOCK_DURATION` seconds. During the block

    Args (from ThrottleEnum):
        MAX: maximum allowed messages
        WINDOW: time window in seconds
        BLOCK_DURATION: how long to block the user after exceeding the limit
    """

    def __init__(self) -> None:
        self._counter: Final[TTLCache[int, int]] = TTLCache(
            maxsize=1000, ttl=Throttle.WINDOW
        )
        self._blocked: Final[TTLCache[int, datetime]] = TTLCache(
            maxsize=1000, ttl=Throttle.BLOCK_DURATION
        )
        self.config = settings

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message) or event.from_user is None:
            return await handler(event, data)

        user_id = event.from_user.id
        if user_id == self.config.SUDO_ID:
            return await handler(event, data)

        if user_id in self._blocked:
            return None

        count = self._counter.get(user_id, 0)
        self._counter[user_id] = count + 1

        if count + 1 >= Throttle.MAX:
            self._blocked[user_id] = datetime.now() + timedelta(
                seconds=Throttle.BLOCK_DURATION.value
            )
            await self._notify_blocked(event, data)
            return None

        return await handler(event, data)

    @staticmethod
    async def _notify_blocked(event: Message, data: dict[str, Any]) -> None:
        """Warn the spamming user and auto-clean the warning once the block expires"""
        i18n: I18nContext | None = data.get("i18n")

        sticker_msg = await event.answer_sticker(
            sticker=StickerID.BLOCKED_DUCK,
            reply_markup=ReplyKeyboardRemove(),
        )
        warn_msg = await event.answer(
            text=i18n.get(
                "dont-spam-dialog",
                block_duration=Throttle.BLOCK_DURATION.value,
            )
        )

        delete_after: DeleteAfter | None = data.get("delete_after")
        if delete_after is not None:
            delete_after(
                event.chat.id,
                [sticker_msg.message_id, warn_msg.message_id],
                Throttle.BLOCK_DURATION.value,
            )
