from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from .stores import MemberStore


class TransactionScope:
    """
    UOW scope for database transactions.

    provides a context manager that automatically commits on success
    or rolls back on exception, and closes the session afterward
    Exposes stores (e.g., members) for database operations

    :param session: SQLAlchemy asynchronous session.
    """

    def __init__(self, session: AsyncSession):
        self.session = session
        self.members: Optional[MemberStore] = None

    async def __aenter__(self):
        """
        enter the asynchronous context

        initializes the member store and returns the scope instance

        :returns: The TransactionScope instance
        :rtype: TransactionScope
        """
        self.members = MemberStore(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        exit the asynchronous context

        commits the transaction if no exception occurred; otherwise rolls back
        always closes the session

        :param exc_type: exception type if an error occurred, else None
        :param exc_val: exception instance if an error occurred, else None
        :param exc_tb: traceback if an error occurred, else None
        """
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                await self.session.rollback()
        finally:
            await self.session.close()

    async def persist(self):
        """explicitly commit the current transaction"""
        await self.session.commit()
