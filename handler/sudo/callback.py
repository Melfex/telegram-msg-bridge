from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, ReactionTypeEmoji
from structlog import get_logger

from keyboard import (
    InboxCallback,
    OwnerReplyKeyboard,
    OwnerInlineKeyboard,
    BotStatusCallback,
    LanguageCallback,
    UserInlineKeyboard,
)
from enums import REACTIONS, InboxAction, Locale, BotStatus
from state import OwnerReply
from util import setup_owner_commands, DeleteAfter
from .helper import set_block_status, show_panel, strip_html

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope, Member
    from util import BotStateService

logger = get_logger(__name__)
callback_router: Final[Router] = Router(name=__name__)

_PICKER_TTL: Final[float] = 0.3


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.REPLY))
async def start_reply(
    callback: CallbackQuery, 
    callback_data: InboxCallback, 
    state: FSMContext, 
    i18n: I18nContext, 
    scope: TransactionScope
) -> None:
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
async def block_user(
    callback: CallbackQuery, 
    callback_data: InboxCallback, 
    i18n: I18nContext, 
    scope: TransactionScope
) -> None:
    """Block the sender of the selected message"""
    await set_block_status(callback, callback_data, i18n, scope, blocked=True)


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.UNBLOCK))
async def unblock_user(
    callback: CallbackQuery, 
    callback_data: InboxCallback, 
    i18n: I18nContext, 
    scope: TransactionScope
) -> None:
    """Unblock the sender of the selected message"""
    await set_block_status(callback, callback_data, i18n, scope, blocked=False)


@callback_router.callback_query(InboxCallback.filter(F.action == InboxAction.REACT))
async def react_to_message(
    callback: CallbackQuery, 
    callback_data: InboxCallback, 
    bot: Bot, 
    i18n: I18nContext
) -> None:
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


@callback_router.callback_query(BotStatusCallback.filter())
async def set_bot_status(
    callback: CallbackQuery,
    callback_data: BotStatusCallback,
    i18n: I18nContext,
    scope: TransactionScope,
    bot_state: BotStateService,
) -> None:
    """Apply the bot status the owner picked and refresh the inline keyboard"""
    action = callback_data.status

    if action == BotStatus.PANEL:
        await show_panel(callback.message, i18n)
        await callback.message.delete()
        return

    config = await scope.config.get_or_create()

    if config.status == action:
        await callback.answer()
        return

    await scope.config.set_status(action)
    bot_state.set_online(action == BotStatus.ONLINE)

    if callback.message is not None:
        await callback.message.edit_reply_markup(
            reply_markup=OwnerInlineKeyboard.bot_status(i18n, current=action)
        )

    key = "bot-enabled-dialog" if action == BotStatus.ONLINE else "bot-disabled-dialog"
    await callback.answer(text=strip_html(i18n.get(key)), show_alert=True)


@callback_router.callback_query(LanguageCallback.filter())
async def owner_select_language(
    callback: CallbackQuery,
    callback_data: LanguageCallback,
    i18n: I18nContext,
    member: Member,
    delete_after: DeleteAfter
) -> None:
    """Persist the owner's locale and return them to the owner panel"""
    new_locale = callback_data.locale

    if member.preferred_lang == new_locale:
        await callback.answer()
        return

    await i18n.set_locale(new_locale)

    if callback.message is not None:
        await callback.message.edit_text(
            text=i18n.get("language-dialog"),
            reply_markup=UserInlineKeyboard.language_menu(current=new_locale),
        )

    await callback.answer(text=strip_html(i18n.get("language-changed-dialog")))
    await setup_owner_commands(callback.bot, i18n, callback.from_user.id)

    if callback.message is not None:
        await show_panel(callback.message, i18n)

    delete_after(callback.message.chat.id, [callback.message.message_id], _PICKER_TTL)