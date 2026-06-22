from __future__ import annotations
from typing import TYPE_CHECKING, Final

from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram_i18n import LazyProxy

from state import OwnerReply
from .helper import send_reply_to_user


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