from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Final

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from cachebox import TTLCache

from config import settings
from enums import BotStatus, Status, StickerID

if TYPE_CHECKING:
    from aiogram.types import TelegramObject, User
    from aiogram_i18n import I18nContext
    from database import TransactionScope, Member
    from util import BotStateService

# Renotify a denied user at most once per this many seconds
_NOTIFY_TTL: Final[int] = 30

_HTML_TAG_RE: Final[re.Pattern[str]] = re.compile(r"<[^>]+>")


class GateMiddleware(BaseMiddleware):
    """
    Access gate enforced before any handler runs
    Stops two classes of update
    """

    def __init__(self) -> None:
        self._notified: TTLCache[int, bool] = TTLCache(maxsize=10_000, ttl=_NOTIFY_TTL)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user: User | None = data.get("event_from_user")

        if user is None or user.is_bot or user.id == settings.SUDO_ID:
            return await handler(event, data)

        if not isinstance(event, (Message, CallbackQuery)):
            return await handler(event, data)

        bot_state: BotStateService | None = data.get("bot_state")
        await self._ensure_loaded(bot_state, data.get("scope"))

        i18n: I18nContext | None = data.get("i18n")

        if bot_state is not None and not bot_state.online:
            await self._deny(event, i18n, user.id, StickerID.SLEEPY_DUCK, "bot-off-dialog")
            return None

        member: Member | None = data.get("member")
        if member is not None and member.status == Status.BLOCKED:
            await self._deny(event, i18n, user.id, StickerID.BLOCKED_DUCK, "you-are-blocked-dialog")
            return None

        return await handler(event, data)

    @staticmethod
    async def _ensure_loaded(
        bot_state: BotStateService | None,
        scope: TransactionScope | None,
    ) -> None:
        if bot_state is None or bot_state.loaded or scope is None:
            return
        config = await scope.config.get_or_create()
        bot_state.set_online(config.status == BotStatus.ONLINE)

    async def _deny(
        self,
        event: Message | CallbackQuery,
        i18n: I18nContext | None,
        user_id: int,
        sticker: StickerID,
        key: str
    ) -> None:
        if i18n is None:
            return

        text = i18n.get(key)

        if isinstance(event, CallbackQuery):
            await event.answer(text=_HTML_TAG_RE.sub("", text), show_alert=True)
            return

        if user_id in self._notified:
            return
        self._notified[user_id] = True
        await event.answer_sticker(sticker=sticker)
        await event.answer(
            text=text, reply_markup=ReplyKeyboardRemove()
        )
