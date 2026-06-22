from __future__ import annotations

from typing import Final, TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart

if TYPE_CHECKING:
    from aiogram.types import Message

command_router: Final[Router] = Router(name=__name__)


@command_router.message(CommandStart())
async def start_command(message: Message):
    """Handle /start for the sudo user"""
    await message.answer(text="hello sudo!")
