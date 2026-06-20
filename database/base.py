from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class RootEntity(AsyncAttrs, DeclarativeBase):
    """Declarative base with automatic lowercase table names"""

    __abstract__ = True

    def __init_subclass__(cls, **kwargs):
        """Set ``__tablename__`` from the class name"""
        super().__init_subclass__(**kwargs)
        cls.__tablename__ = cls.__name__.lower()
