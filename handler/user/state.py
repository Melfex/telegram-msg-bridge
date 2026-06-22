from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram_i18n import LazyProxy

from config import settings
from keyboard import UserReplyKeyboard
from state import SendMessage
from .helper import build_owner_inbox, send_success_and_clear

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope

state_router: Final[Router] = Router(name=__name__)


@state_router.message(StateFilter(SendMessage.WAITING), F.text == LazyProxy("cancel-btn"))
async def cancel_sending(message: Message, state: FSMContext, i18n: I18nContext) -> None:
    """Leave the send flow and return to the main menu"""
    await state.clear()
    await message.answer(
        text=i18n.get("cancelled-dialog"),
        reply_markup=UserReplyKeyboard.main_menu(i18n),
    )


@state_router.message(StateFilter(SendMessage.WAITING), F.text)
async def relay_text(message: Message, state: FSMContext, bot: Bot, i18n: I18nContext, scope: TransactionScope,) -> None:
    """Relay a text message to the owner"""
    text, keyboard = await build_owner_inbox(message, state, i18n, scope)
    await bot.send_message(
        chat_id=settings.SUDO_ID,
        text=text,
        reply_markup=keyboard,
    )
    await send_success_and_clear(message, state, i18n)


@state_router.message(StateFilter(SendMessage.WAITING))
async def relay_media(message: Message, state: FSMContext, i18n: I18nContext, scope: TransactionScope,) -> None:
    """Relay media to the owner"""
    text, keyboard = await build_owner_inbox(message, state, i18n, scope)
    await message.copy_to(
        chat_id=settings.SUDO_ID,
        caption=text,
        reply_markup=keyboard,
    )
    await send_success_and_clear(message, state, i18n)
