from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F
from aiogram.filters import CommandStart, or_f, Command
from aiogram_i18n import LazyProxy

from keyboard import UserReplyKeyboard, UserInlineKeyboard
from enums import MessageEffect, StickerID

if TYPE_CHECKING:
    from aiogram.types import Message, User
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext

command_router: Final[Router] = Router(name=__name__)


@command_router.message(CommandStart())
async def start_command(message: Message, i18n: I18nContext, state: FSMContext) -> None:
    """Handle the /start command, clear previous states, and show the main menu"""
    await state.clear()
    user: User = message.from_user

    await message.reply_sticker(sticker=StickerID.HI_DUCK)
    await message.answer(
        text=i18n.get("start-dialog", mention=user.mention_html(user.first_name)),
        reply_markup=UserReplyKeyboard.main_menu(i18n),
        message_effect_id=MessageEffect.HEART
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
        reply_markup=UserInlineKeyboard.social_links()
    )

