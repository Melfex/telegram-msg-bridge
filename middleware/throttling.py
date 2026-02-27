from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Awaitable, Callable, Final, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.types import Message
from cachebox import TTLCache

from config import settings
from enums import ThrottleEnum

if TYPE_CHECKING:
    from aiogram.types import TelegramObject
    from aiogram_i18n import I18nContext


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
            maxsize=1000, ttl=ThrottleEnum.WINDOW
        )
        self._blocked: Final[TTLCache[int, datetime]] = TTLCache(
            maxsize=1000, ttl=ThrottleEnum.BLOCK_DURATION
        )
        self.config = settings

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id

        if not isinstance(event, Message) or user_id == self.config.SUDO_ID:
            return await handler(event, data)

        if user_id in self._blocked:
            return None

        count = self._counter.get(user_id, 0)
        self._counter[user_id] = count + 1

        if count + 1 >= ThrottleEnum.MAX:
            self._blocked[user_id] = datetime.now() + timedelta(
                seconds=ThrottleEnum.BLOCK_DURATION.value
            )
            print("blocked")
            i18n: I18nContext | None = data.get("i18n")
            await event.answer(
                i18n.get("hello", user="spam")
            )  # TODO: will be completed later, now just for fun XD
            return None

        return await handler(event, data)
