from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router
from aiogram.filters import CommandStart

if TYPE_CHECKING:
    from aiogram.types import Message
    from aiogram_i18n import I18nContext

router: Final[Router] = Router()


@router.message(CommandStart())
async def start_command(message: Message, i18n: I18nContext):
    await message.answer(text=i18n.get("hello", user=message.from_user.full_name))
