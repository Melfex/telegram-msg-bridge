from __future__ import annotations

from typing import Final, TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart, Command

from keyboard import UserInlineKeyboard
from .helper import show_panel

if TYPE_CHECKING:
    from aiogram.types import Message
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import Member

command_router: Final[Router] = Router(name=__name__)


@command_router.message(CommandStart())
async def start_command(
    message: Message, 
    state: FSMContext, 
    i18n: I18nContext
) -> None:
    """Reset state and open the owner admin panel"""
    await state.clear()
    await show_panel(message, i18n)


@command_router.message(Command("language"))
async def language_command(
    message: Message,
    state: FSMContext,
    i18n: I18nContext,
    member: Member | None = None,
) -> None:
    """Show the language picker to the owner without leaving the owner context"""
    await state.clear()
    await message.answer(
        text=i18n.get("language-dialog"),
        reply_markup=UserInlineKeyboard.language_menu(
            current=member.preferred_lang if member else None,
        ),
    )
