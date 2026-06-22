from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram_i18n import LazyProxy

from keyboard import UserInlineKeyboard
from enums import StickerID
from .helper import _picker_markup

if TYPE_CHECKING:
    from aiogram.types import Message
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import Member

command_router: Final[Router] = Router(name=__name__)


@command_router.message(CommandStart())
async def start_command(message: Message, i18n: I18nContext, state: FSMContext, member: Member | None = None,) -> None:
    """Greet the user, reset state, and show the language picker"""
    await state.clear()
    await message.reply_sticker(sticker=StickerID.LANGUAGE_DUCK)
    await message.answer(
        text=i18n.get("language-dialog"),
        reply_markup=_picker_markup(member),
    )


@command_router.message(or_f(Command("language"), F.text == LazyProxy("language-btn")))
async def language_command(message: Message, i18n: I18nContext, member: Member | None = None) -> None:
    """Show the language picker so the user can switch locale at any time"""
    await message.answer(
        text=i18n.get("language-dialog"),
        reply_markup=_picker_markup(member),
    )


@command_router.message(or_f(Command("help"), F.text == LazyProxy("help-btn")))
async def help_command(message: Message, i18n: I18nContext) -> None:
    """Handle the /help command"""
    await message.reply_sticker(sticker=StickerID.HELP_DUCK)
    await message.answer(text=i18n.get("help-dialog"))


@command_router.message(or_f(Command("links"), F.text == LazyProxy("links-btn")))
async def links_command(message: Message, i18n: I18nContext) -> None:
    """Handle the /links command"""
    await message.reply_sticker(sticker=StickerID.SOCIAL_DUCK)
    await message.answer(
        text=i18n.get("links-dialog"),
        reply_markup=UserInlineKeyboard.social_links(),
    )
