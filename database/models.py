from sqlalchemy import BigInteger, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from enums import Status, Locale, BotStatus
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
        default=Locale.DEFAULT,
        comment="preferred language of member",
    )
    status: Mapped[Status] = mapped_column(
        Enum(Status),
        nullable=False,
        default=Status.UNBLOCKED,
        comment="status (block or unblock) of member",
    )


class BotConfig(RootEntity):
    __tablename__ = "bot_config"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False,
        default=1,
        comment="fixed singleton primary key (always 1)",
    )
    status: Mapped[BotStatus] = mapped_column(
        Enum(BotStatus),
        nullable=False,
        default=BotStatus.ONLINE,
        comment="global runtime status (online or offline) of the bot",
    )
