from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import settings
from .scope import TransactionScope


class DatabaseConnector:
    """
    manages database engine and session creation

    :param database_url: Database connection URL
    :type database_url: str
    """

    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url)
        self.session_maker = async_sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def init_tables(self):
        """create all tables defined in the base metadata"""
        from .base import RootEntity

        async with self.engine.begin() as conn:
            await conn.run_sync(RootEntity.metadata.create_all)

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """provide an AsyncSession as a context manager"""
        async with self.session_maker() as session:
            yield session

    @asynccontextmanager
    async def create_scope(self) -> AsyncGenerator[TransactionScope, None]:
        """provide a TransactionScope as a context manager"""
        async with self.session_maker() as session:
            async with TransactionScope(session) as scope:
                yield scope


def db_instance() -> DatabaseConnector:
    """
    create a DatabaseConnector instance using settings

    :return: Configured DatabaseConnector
    """
    db_url: str = settings.DATABASE_URL.get_secret_value()
    return DatabaseConnector(db_url)
