from __future__ import annotations

from typing import Final, TYPE_CHECKING

from aiogram import Router, F
from aiogram.types import ReplyKeyboardRemove
from aiogram_i18n import LazyProxy

from keyboard import OwnerReplyKeyboard, OwnerInlineKeyboard
from state import AdminPanel

if TYPE_CHECKING:
    from aiogram.types import Message
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope, Member

button_router: Final[Router] = Router(name=__name__)


@button_router.message(F.text == LazyProxy("toggle-bot-btn"))
async def toggle_bot(
    message: Message,
    i18n: I18nContext,
    scope: TransactionScope,
) -> None:
    """Show the bot status picker with the current status highlighted"""
    config = await scope.config.get_or_create()

    _w_msg = await message.answer(
        text=".", reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=i18n.get("bot-status-dialog"),
        reply_markup=OwnerInlineKeyboard.bot_status(i18n, current=config.status),
    )

    await _w_msg.delete()


@button_router.message(F.text == LazyProxy("block-user-btn"))
async def ask_block(message: Message, state: FSMContext, i18n: I18nContext, member: Member) -> None:
    """Prompt the owner for the id of the user to block"""
    await state.set_state(AdminPanel.BLOCK_USER)
    await message.answer(
        text=i18n.get("ask-user-id-dialog"),
        reply_markup=OwnerReplyKeyboard.cancel_button(i18n, member.preferred_lang),
    )


@button_router.message(F.text == LazyProxy("unblock-user-btn"))
async def ask_unblock(message: Message, state: FSMContext, i18n: I18nContext, member: Member) -> None:
    """Prompt the owner for the id of the user to unblock"""
    await state.set_state(AdminPanel.UNBLOCK_USER)
    await message.answer(
        text=i18n.get("ask-user-id-dialog"),
        reply_markup=OwnerReplyKeyboard.cancel_button(i18n, member.preferred_lang),
    )


@button_router.message(F.text == LazyProxy("broadcast-btn"))
async def ask_broadcast(message: Message, state: FSMContext, i18n: I18nContext, member: Member) -> None:
    """Prompt the owner for the message to broadcast"""
    await state.set_state(AdminPanel.BROADCAST)
    await message.answer(
        text=i18n.get("broadcast-ask-dialog"),
        reply_markup=OwnerReplyKeyboard.cancel_button(i18n, member.preferred_lang),
    )


