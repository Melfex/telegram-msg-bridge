from sqlalchemy import BigInteger, String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from enums.status import StatusEnum
from .base import RootEntity


class Member(RootEntity):
    __tablename__ = "members"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False
    )
    preferred_lang: Mapped[str] = mapped_column(
        String(10), nullable=False, default="en"
    )
    state: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum), nullable=False, default=StatusEnum.UNBLOCKED
    )
