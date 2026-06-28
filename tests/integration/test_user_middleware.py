"""Tests for the middleware that resolves/creates the ``Member`` for an update."""

from __future__ import annotations

from typing import Callable

from database.scope import TransactionScope
from middleware.user import UserMiddleware
from tests.factories import make_handler, make_user


class TestUserMiddlewarePassThrough:
    async def test_no_user_skips_resolution(self) -> None:
        handler = make_handler("ok")
        data: dict = {"event_from_user": None}

        result = await UserMiddleware()(handler, object(), data)

        assert result == "ok"
        assert "member" not in data
        handler.assert_awaited_once()

    async def test_bot_account_skipped(self) -> None:
        handler = make_handler("ok")
        data = {"event_from_user": make_user(1, is_bot=True)}

        await UserMiddleware()(handler, object(), data)

        assert "member" not in data

    async def test_missing_scope_skipped(self) -> None:
        handler = make_handler("ok")
        data = {"event_from_user": make_user(1), "scope": None}

        await UserMiddleware()(handler, object(), data)

        assert "member" not in data


class TestUserMiddlewareResolution:
    async def test_creates_and_persists_new_member(
        self, scope: TransactionScope, new_scope: Callable
    ) -> None:
        handler = make_handler("ok")
        data = {
            "event_from_user": make_user(123, language_code="en-US"),
            "scope": scope,
        }

        result = await UserMiddleware()(handler, object(), data)

        assert result == "ok"
        assert data["member"].telegram_id == 123
        # "en-US" is normalized down to the supported "en" locale.
        assert data["member"].preferred_lang == "en"

        async with new_scope() as verify:
            stored = await verify.members.by_id(123)
            assert stored is not None
            assert stored.preferred_lang == "en"

    async def test_returns_existing_member_without_overwriting(
        self, new_scope: Callable, scope: TransactionScope
    ) -> None:
        async with new_scope() as setup:
            await setup.members.add(123, lang="de")

        handler = make_handler("ok")
        data = {
            "event_from_user": make_user(123, language_code="en"),
            "scope": scope,
        }

        await UserMiddleware()(handler, object(), data)

        # Existing preference is preserved, not reset to the Telegram language.
        assert data["member"].preferred_lang == "de"

    async def test_unsupported_language_falls_back_to_default(
        self, scope: TransactionScope
    ) -> None:
        from enums import Locale

        handler = make_handler("ok")
        data = {
            "event_from_user": make_user(777, language_code="klingon"),
            "scope": scope,
        }

        await UserMiddleware()(handler, object(), data)

        assert data["member"].preferred_lang == Locale.DEFAULT
