"""Lightweight test doubles and object builders shared across the test suite.

These helpers intentionally avoid constructing fully-validated aiogram models
(which require many fields). Where a handler/middleware only relies on a couple
of attributes, a :class:`~types.SimpleNamespace` is used; where ``isinstance``
checks matter (e.g. the access gate), :func:`unittest.mock.create_autospec` is
used so the mock still passes ``isinstance`` while keeping async methods awaitable.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, create_autospec

from aiogram.exceptions import TelegramBadRequest, TelegramRetryAfter
from aiogram.types import CallbackQuery, Message, User


class FakeI18n:
    """Minimal stand-in for ``aiogram_i18n.I18nContext``.

    ``get`` echoes the requested key back, which keeps keyboard/handler tests
    independent of the Fluent ``.ftl`` catalogs while still letting us assert
    *which* keys were requested.
    """

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[Any, ...], dict[str, Any]]] = []

    def get(self, key: str, *args: Any, **kwargs: Any) -> str:
        self.calls.append((key, args, kwargs))
        return key

    @property
    def requested_keys(self) -> list[str]:
        return [call[0] for call in self.calls]


def make_user(
    user_id: int,
    *,
    is_bot: bool = False,
    language_code: str | None = "en",
) -> SimpleNamespace:
    """Build a duck-typed Telegram user (no ``isinstance`` checks rely on it)."""
    return SimpleNamespace(id=user_id, is_bot=is_bot, language_code=language_code)


def make_callback_query() -> Any:
    """Autospec ``CallbackQuery`` so ``isinstance`` works.

    aiogram's shortcut methods (``answer``/``edit_reply_markup``) are not plain
    ``async def`` functions, so autospec renders them as sync mocks. We override
    the ones the gate awaits with explicit :class:`AsyncMock` instances.
    """
    callback = create_autospec(CallbackQuery, instance=True)
    callback.answer = AsyncMock()
    callback.message = create_autospec(Message, instance=True)
    callback.message.answer = AsyncMock()
    callback.message.edit_reply_markup = AsyncMock()
    return callback


def make_message() -> Any:
    """Autospec ``Message`` so ``isinstance`` works, with awaitable shortcuts."""
    message = create_autospec(Message, instance=True)
    message.answer = AsyncMock()
    message.answer_sticker = AsyncMock()
    return message


def make_handler(return_value: Any = "handled") -> AsyncMock:
    """A next-handler mock for middleware tests."""
    return AsyncMock(return_value=return_value)


def retry_after_error(seconds: int) -> TelegramRetryAfter:
    """Construct a realistic ``TelegramRetryAfter`` without a real bot method."""
    return TelegramRetryAfter(
        method=SimpleNamespace(),
        message="flood control exceeded",
        retry_after=seconds,
    )


def bad_request_error(message: str = "bad request") -> TelegramBadRequest:
    """Construct a realistic ``TelegramBadRequest`` for failure-path tests."""
    return TelegramBadRequest(method=SimpleNamespace(), message=message)


def autospec_user(user_id: int, *, is_bot: bool = False) -> Any:
    """Autospec ``User`` for cases that need a real ``User`` instance."""
    user = create_autospec(User, instance=True)
    user.id = user_id
    user.is_bot = is_bot
    return user
