from __future__ import annotations

from typing import TYPE_CHECKING, Any, Awaitable, Callable

from aiogram import BaseMiddleware

from enums import Locale

if TYPE_CHECKING:
    from aiogram.types import TelegramObject, User
    from database import Member, TransactionScope

_SUPPORTED_LOCALES: frozenset[str] = frozenset(Locale)


def _normalize_locale(language_code: str | None) -> str:
    """
    map a Telegram ``language_code`` (e.g. ``en``, ``en-US``, ``pt-br``) to a
    supported two-letter locale, falling back to the default locale.
    """
    if not language_code:
        return Locale.DEFAULT
    primary = language_code.split("-", 1)[0].lower()
    return primary if primary in _SUPPORTED_LOCALES else Locale.DEFAULT


class UserMiddleware(BaseMiddleware):
    """middleware that ensures a `Member` object exists in the handler data"""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        """
        resolve the member and inject it into data

        :param handler: the next middleware or event handler
        :param event: the incoming Telegram event
        :param data: a mutable dictionary shared across the middleware chain
        :return: the result of the next handler
        """
        tg_user: User | None = data.get("event_from_user")

        if tg_user is None or tg_user.is_bot:
            return await handler(event, data)

        scope: TransactionScope | None = data.get("scope")
        if scope is None:
            return await handler(event, data)

        store = scope.members
        member: Member | None = await store.by_id(tg_user.id)

        if member is None:
            lang = _normalize_locale(tg_user.language_code)
            member = await store.add(tg_user.id, lang)
            await scope.persist()

        data["member"] = member
        return await handler(event, data)
