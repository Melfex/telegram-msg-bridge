from sqlalchemy import BigInteger, String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from enums import StatusEnum, LocaleEnum
from .base import RootEntity


class Member(RootEntity):
    __tablename__ = "members"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=False,
        comment="telegram id of member",
    )
    preferred_lang: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
        default=LocaleEnum.DEFAULT,
        comment="preferred language of member",
    )
    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum),
        nullable=False,
        default=StatusEnum.UNBLOCKED,
        comment="status (block or unblock) of member",
    )
