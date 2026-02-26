from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class RootEntity(AsyncAttrs, DeclarativeBase):
    """base model with automatic lowercase table name from class"""

    __abstract__ = True

    def __init_subclass__(cls, **kwargs):
        """convert class name to lowercase and set as __tablename__"""
        super().__init_subclass__(**kwargs)
        cls.__tablename__ = cls.__name__.lower()
