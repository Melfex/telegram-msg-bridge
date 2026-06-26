from __future__ import annotations
from typing import TYPE_CHECKING, Final

from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram_i18n import LazyProxy

from state import OwnerReply, AdminPanel
from config import settings
from keyboard import OwnerReplyKeyboard
from .helper import send_reply_to_user, show_panel, parse_user_id, launch_broadcast


if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope


state_router: Final[Router] = Router(name=__name__)


@state_router.message(StateFilter(OwnerReply.WAITING), F.text == LazyProxy("cancel-btn"))
async def cancel_reply(message: Message, state: FSMContext, i18n: I18nContext) -> None:
    """Abort the reply flow"""
    data = await state.get_data()
    reply_message_id: int = data.get("reply_message_id")

    await message.bot.delete_messages(
        chat_id=message.chat.id, message_ids=[reply_message_id, message.message_id]
    )
    await state.clear()
    await show_panel(message, i18n)


@state_router.message(StateFilter(OwnerReply.WAITING))
async def send_reply(message: Message, state: FSMContext, bot: Bot, i18n: I18nContext, scope: TransactionScope) -> None:
    """Deliver the owner's reply (any content type) to the target sender"""
    data = await state.get_data()
    user_id: int = data.get("reply_to")
    await state.clear()

    await send_reply_to_user(
        message=message,
        bot=bot,
        i18n=i18n,
        scope=scope,
        user_id=user_id,
    )

    await message.answer(text=i18n.get("reply-sent-dialog"))
    await show_panel(message, i18n)


@state_router.message(
    StateFilter(AdminPanel.BLOCK_USER, AdminPanel.UNBLOCK_USER, AdminPanel.BROADCAST),
    F.text == LazyProxy("cancel-btn"),
)
async def cancel_panel_flow(message: Message, state: FSMContext, i18n: I18nContext) -> None:
    """Abort the current panel action and return to the panel"""
    await state.clear()
    await show_panel(message, i18n)


@state_router.message(StateFilter(AdminPanel.BLOCK_USER))
async def receive_block_id(message: Message, state: FSMContext, i18n: I18nContext, scope: TransactionScope) -> None:
    """Block the user whose id the owner just sent"""
    target_id = parse_user_id(message.text)
    if target_id is None:
        await message.answer(text=i18n.get("invalid-id-dialog"))
        return

    await scope.members.set_block(target_id, blocked=True)
    await state.clear()
    await message.answer(text=i18n.get("user-blocked-dialog"))
    await show_panel(message, i18n)


@state_router.message(StateFilter(AdminPanel.UNBLOCK_USER))
async def receive_unblock_id(message: Message, state: FSMContext, i18n: I18nContext, scope: TransactionScope) -> None:
    """Unblock the user whose id the owner just sent"""
    target_id = parse_user_id(message.text)
    if target_id is None:
        await message.answer(text=i18n.get("invalid-id-dialog"))
        return

    await scope.members.set_block(target_id, blocked=False)
    await state.clear()
    await message.answer(text=i18n.get("user-unblocked-dialog"))
    await show_panel(message, i18n)


@state_router.message(StateFilter(AdminPanel.BROADCAST))
async def receive_broadcast(message: Message, state: FSMContext, bot: Bot, i18n: I18nContext, scope: TransactionScope) -> None:
    """Broadcast the owner's message to every unblocked member in the background"""
    user_ids = await scope.members.all_unblocked_ids(exclude=settings.SUDO_ID)
    await state.clear()

    await message.answer(
        text=i18n.get("broadcast-started-dialog", total=str(len(user_ids))),
        reply_markup=OwnerReplyKeyboard.panel(i18n),
    )

    launch_broadcast(
        bot,
        i18n,
        owner_id=settings.SUDO_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        user_ids=user_ids,
    )
