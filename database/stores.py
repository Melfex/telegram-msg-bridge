from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from enums.locale import LocaleEnums
from enums.status import StatusEnum
from .models import Member


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

    async def add(self, telegram_id: int, lang: str = LocaleEnums.DEFAULT) -> Member:
        member = Member(telegram_id=telegram_id, preferred_lang=lang)
        self.session.add(member)
        return member

    async def update_status(self, telegram_id: int, new_state: StatusEnum) -> None:
        await self.session.execute(
            update(Member)
            .where(Member.telegram_id == telegram_id)
            .values(state=new_state)
        )

    async def update_lang(self, telegram_id: int, new_lang: str) -> None:
        await self.session.execute(
            update(Member)
            .where(Member.telegram_id == telegram_id)
            .values(preferred_lang=new_lang)
        )
