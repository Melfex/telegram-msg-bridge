from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from enums import Status, BotStatus
from enums.locale import Locale
from .models import Member, BotConfig


class MemberStore:
    """
    data access layer for Member model
    provides async methods to query and modify members in the database
    changes require an explicit commit via the surrounding transaction scope
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def by_id(self, telegram_id: int) -> Optional[Member]:
        result = await self.session.execute(
            select(Member).where(Member.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def add(self, telegram_id: int, lang: str = Locale.DEFAULT) -> Member:
        member = Member(telegram_id=telegram_id, preferred_lang=lang)
        self.session.add(member)
        return member

    async def update_status(self, telegram_id: int, new_status: Status) -> None:
        await self.session.execute(
            update(Member)
            .where(Member.telegram_id == telegram_id)
            .values(status=new_status)
        )

    async def update_lang(self, telegram_id: int, new_lang: str) -> None:
        await self.session.execute(
            update(Member)
            .where(Member.telegram_id == telegram_id)
            .values(preferred_lang=new_lang)
        )

    async def set_block(self, telegram_id: int, blocked: bool) -> Member:
        """Block or unblock a member, creating the row if it does not exist yet"""
        member = await self.by_id(telegram_id)
        if member is None:
            member = await self.add(telegram_id)
        member.status = Status.BLOCKED if blocked else Status.UNBLOCKED
        return member

    async def all_unblocked_ids(self, exclude: int | None = None) -> list[int]:
        """Return the telegram ids of every unblocked member (for broadcasting)"""
        stmt = select(Member.telegram_id).where(Member.status == Status.UNBLOCKED)
        if exclude is not None:
            stmt = stmt.where(Member.telegram_id != exclude)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())


class BotConfigStore:
    """
    data access layer for the singleton :class:`BotConfig` row

    The whole bot shares a single config row (``id == 1``); accessor methods
    create it on first use so callers never deal with a missing row
    """

    _SINGLETON_ID: int = 1

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_create(self) -> BotConfig:
        """Fetch the singleton config row, creating it with defaults if absent"""
        config = await self.session.get(BotConfig, self._SINGLETON_ID)
        if config is None:
            config = BotConfig(id=self._SINGLETON_ID, status=BotStatus.ONLINE)
            self.session.add(config)
            await self.session.flush()
        return config

    async def set_status(self, status: BotStatus) -> BotConfig:
        """Persist a new global bot status and return the updated row"""
        config = await self.get_or_create()
        config.status = status
        return config
