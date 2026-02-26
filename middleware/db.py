from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict, TYPE_CHECKING

from aiogram import BaseMiddleware

if TYPE_CHECKING:
    from aiogram.types import TelegramObject
    from database import DatabaseConnector


class DatabaseMiddleware(BaseMiddleware):
    """middleware that injects a database transaction scope into the handler data"""

    def __init__(self, connector: DatabaseConnector):
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.connector.create_scope() as scope:
            data["scope"] = scope
            return await handler(event, data)
