from aiogram import filters
from aiogram.types import Message, CallbackQuery

from config import settings


class IsSudo(filters.BaseFilter):
    async def __call__(self, update: Message | CallbackQuery):
        user_id = update.from_user.id
        return user_id == settings.SUDO_ID
