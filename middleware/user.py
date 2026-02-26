from __future__ import annotations

from typing import TYPE_CHECKING, Any, Awaitable, Callable

from aiogram import BaseMiddleware

from enums import LocaleEnums

if TYPE_CHECKING:
    from aiogram.types import TelegramObject, User
    from database import Member, TransactionScope


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
            lang = tg_user.language_code or LocaleEnums.DEFAULT
            member = await store.add(tg_user.id, lang)
            await scope.persist()

        data["member"] = member
        return await handler(event, data)
