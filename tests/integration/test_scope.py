"""Integration tests for the unit-of-work ``TransactionScope`` semantics."""

from __future__ import annotations

from typing import Callable

import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker

from database.scope import TransactionScope


class TestTransactionScope:
    async def test_commits_on_clean_exit(
        self, session_factory: async_sessionmaker, new_scope: Callable
    ) -> None:
        async with session_factory() as session:
            async with TransactionScope(session) as scope:
                await scope.members.add(1)

        async with new_scope() as scope:
            assert await scope.members.by_id(1) is not None

    async def test_rolls_back_on_exception(
        self, session_factory: async_sessionmaker, new_scope: Callable
    ) -> None:
        boom = RuntimeError("boom")
        with pytest.raises(RuntimeError, match="boom"):
            async with session_factory() as session:
                async with TransactionScope(session) as scope:
                    await scope.members.add(2)
                    raise boom

        async with new_scope() as scope:
            assert await scope.members.by_id(2) is None

    async def test_persist_commits_midflight(
        self, session_factory: async_sessionmaker, new_scope: Callable
    ) -> None:
        async with session_factory() as session:
            async with TransactionScope(session) as scope:
                await scope.members.add(3)
                await scope.persist()

                # Already durable even though the scope hasn't exited yet.
                async with new_scope() as other:
                    assert await other.members.by_id(3) is not None

    async def test_stores_initialized_on_enter(
        self, session_factory: async_sessionmaker
    ) -> None:
        async with session_factory() as session:
            async with TransactionScope(session) as scope:
                assert scope.members is not None
                assert scope.config is not None
