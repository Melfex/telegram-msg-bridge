from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, ReactionTypeEmoji
from structlog import get_logger

from keyboard import InboxCallback, OwnerReplyKeyboard
from enums import REACTIONS, InboxAction, Locale
from state import OwnerReply
from .helper import set_block_status

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope

logger = get_logger(__name__)
callback_router: Final[Router] = Router(name=__name__)


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.REPLY))
async def start_reply(callback: CallbackQuery, callback_data: InboxCallback, state: FSMContext, i18n: I18nContext, scope: TransactionScope) -> None:
    """Begin the reply flow for the selected sender"""
    await state.set_state(OwnerReply.WAITING)

    owner = await scope.members.by_id(callback.from_user.id)
    locale = owner.preferred_lang if owner else Locale.DEFAULT

    reply = await callback.message.answer(
        text=i18n.get("reply-dialog"), reply_markup=OwnerReplyKeyboard.cancel_button(i18n, locale)
    )

    await state.update_data(
        reply_to=callback_data.user_id,
        reply_message_id=reply.message_id,
    )


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.BLOCK))
async def block_user(callback: CallbackQuery, callback_data: InboxCallback, i18n: I18nContext, scope: TransactionScope) -> None:
    """Block the sender of the selected message"""
    await set_block_status(callback, callback_data, i18n, scope, blocked=True)


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.UNBLOCK))
async def unblock_user(callback: CallbackQuery, callback_data: InboxCallback, i18n: I18nContext, scope: TransactionScope) -> None:
    """Unblock the sender of the selected message"""
    await set_block_status(callback, callback_data, i18n, scope, blocked=False)


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.REACT))
async def react_to_message(callback: CallbackQuery, callback_data: InboxCallback, bot: Bot, i18n: I18nContext) -> None:
    """Place the owner's chosen emoji reaction on the sender's message"""
    emoji = REACTIONS[callback_data.reaction_idx]

    await bot.set_message_reaction(
        chat_id=callback_data.user_id,
        message_id=callback_data.message_id,
        reaction=[ReactionTypeEmoji(emoji=emoji)],
    )

    await callback.answer(
        text=i18n.get("reaction-sent-dialog"),
        show_alert=True
    )

