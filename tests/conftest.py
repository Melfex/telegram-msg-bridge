"""Pytest configuration and shared fixtures.

Environment variables are set *before* any project module is imported so that
``config.settings`` (a module-level pydantic-settings singleton) loads with
deterministic values regardless of the developer's local ``.env``. With
pydantic-settings, real environment variables take precedence over the
``.env`` file, so this is safe and CI-friendly.
"""

from __future__ import annotations

import os

os.environ.setdefault("BOT_TOKEN", "123456789:TEST-TOKEN")
os.environ["SUDO_ID"] = "999999999"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"

from contextlib import asynccontextmanager  # noqa: E402
from typing import AsyncIterator, Callable  # noqa: E402

import pytest  # noqa: E402
import pytest_asyncio  # noqa: E402
from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool  # noqa: E402

from config import settings  # noqa: E402
from database.base import RootEntity  # noqa: E402
from database.scope import TransactionScope  # noqa: E402

# Import models so their tables register on RootEntity.metadata before create_all.
import database.models  # noqa: E402,F401


SUDO_ID: int = settings.SUDO_ID


@pytest.fixture
def sudo_id() -> int:
    """The deterministic owner id used throughout the suite."""
    return SUDO_ID


@pytest_asyncio.fixture
async def db_engine() -> AsyncIterator[AsyncEngine]:
    """A throwaway in-memory SQLite engine with a fresh schema per test.

    ``StaticPool`` keeps a single underlying connection alive so the in-memory
    database survives across multiple sessions within the same test.
    """
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )
    async with engine.begin() as conn:
        await conn.run_sync(RootEntity.metadata.create_all)

    yield engine

    await engine.dispose()


@pytest.fixture
def session_factory(db_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[AsyncSession]:
    async with session_factory() as db_session:
        yield db_session


@pytest_asyncio.fixture
async def scope(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[TransactionScope]:
    """A ready-to-use, auto-committing transaction scope."""
    async with session_factory() as db_session:
        async with TransactionScope(db_session) as transaction_scope:
            yield transaction_scope


@pytest.fixture
def new_scope(
    session_factory: async_sessionmaker[AsyncSession],
) -> Callable[[], "asynccontextmanager[TransactionScope]"]:
    """Factory that opens a fresh committing scope on the shared engine.

    Useful for verifying that data written in one transaction is visible from a
    brand-new transaction::

        async with new_scope() as scope:
            await scope.members.add(1)
        async with new_scope() as scope:
            assert await scope.members.by_id(1) is not None
    """

    @asynccontextmanager
    async def _factory() -> AsyncIterator[TransactionScope]:
        async with session_factory() as db_session:
            async with TransactionScope(db_session) as transaction_scope:
                yield transaction_scope

    return _factory
