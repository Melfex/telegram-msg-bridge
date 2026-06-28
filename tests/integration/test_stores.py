"""Integration tests for the data-access stores against a real SQLite engine."""

from __future__ import annotations

from typing import Callable

from database.scope import TransactionScope
from enums import BotStatus, Locale, Status


class TestMemberStore:
    async def test_add_and_fetch_roundtrip(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(111, lang="en")

        async with new_scope() as scope:
            member = await scope.members.by_id(111)
            assert member is not None
            assert member.telegram_id == 111
            assert member.preferred_lang == "en"
            # New members are unblocked by default.
            assert member.status == Status.UNBLOCKED

    async def test_by_id_missing_returns_none(self, scope: TransactionScope) -> None:
        assert await scope.members.by_id(404) is None

    async def test_add_uses_default_locale(self, scope: TransactionScope) -> None:
        member = await scope.members.add(222)
        assert member.preferred_lang == Locale.DEFAULT

    async def test_set_block_creates_missing_member(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            member = await scope.members.set_block(333, blocked=True)
            assert member.status == Status.BLOCKED

        async with new_scope() as scope:
            stored = await scope.members.by_id(333)
            assert stored is not None
            assert stored.status == Status.BLOCKED

    async def test_set_block_toggles_existing_member(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(444)

        async with new_scope() as scope:
            await scope.members.set_block(444, blocked=True)
        async with new_scope() as scope:
            assert (await scope.members.by_id(444)).status == Status.BLOCKED

        async with new_scope() as scope:
            await scope.members.set_block(444, blocked=False)
        async with new_scope() as scope:
            assert (await scope.members.by_id(444)).status == Status.UNBLOCKED

    async def test_update_lang(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(555, lang="en")
        async with new_scope() as scope:
            await scope.members.update_lang(555, "de")
        async with new_scope() as scope:
            assert (await scope.members.by_id(555)).preferred_lang == "de"

    async def test_update_status(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(666)
        async with new_scope() as scope:
            await scope.members.update_status(666, Status.BLOCKED)
        async with new_scope() as scope:
            assert (await scope.members.by_id(666)).status == Status.BLOCKED


class TestAllUnblockedIds:
    async def test_returns_only_unblocked(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(1)
            await scope.members.add(2)
            await scope.members.set_block(3, blocked=True)

        async with new_scope() as scope:
            ids = await scope.members.all_unblocked_ids()
            assert set(ids) == {1, 2}

    async def test_exclude_owner(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.members.add(1)
            await scope.members.add(2)
            await scope.members.add(999)

        async with new_scope() as scope:
            ids = await scope.members.all_unblocked_ids(exclude=999)
            assert set(ids) == {1, 2}

    async def test_empty_when_no_members(self, scope: TransactionScope) -> None:
        assert await scope.members.all_unblocked_ids() == []


class TestBotConfigStore:
    async def test_get_or_create_seeds_singleton(self, scope: TransactionScope) -> None:
        config = await scope.config.get_or_create()
        assert config.id == 1
        assert config.status == BotStatus.ONLINE

    async def test_get_or_create_is_idempotent(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            first = await scope.config.get_or_create()
            second = await scope.config.get_or_create()
            assert first.id == second.id == 1

        async with new_scope() as scope:
            # Still exactly one row, still id == 1.
            assert (await scope.config.get_or_create()).id == 1

    async def test_set_status_persists(self, new_scope: Callable) -> None:
        async with new_scope() as scope:
            await scope.config.set_status(BotStatus.OFFLINE)

        async with new_scope() as scope:
            assert (await scope.config.get_or_create()).status == BotStatus.OFFLINE
