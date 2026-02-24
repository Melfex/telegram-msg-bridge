from __future__ import annotations

from typing import Final, TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart

if TYPE_CHECKING:
    from aiogram.types import Message

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="hello sudo!")
