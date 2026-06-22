from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import Message, InlineKeyboardMarkup

from config import settings
from enums import Locale, MessageMode
from keyboard import OwnerInlineKeyboard, UserReplyKeyboard
from state import SendMessage
from database import Member
from keyboard import UserInlineKeyboard

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import TransactionScope


async def enter_mode(
    message: Message,
    state: FSMContext,
    i18n: I18nContext,
    mode: MessageMode,
) -> None:
    """Enter user send-flow and show the mode"""
    await state.set_state(SendMessage.WAITING)
    await state.update_data(mode=mode)
    prompt = "send-anon-dialog" if mode == MessageMode.ANONYMOUS else "send-direct-dialog"
    await message.answer(
        text=i18n.get(prompt),
        reply_markup=UserReplyKeyboard.cancel(i18n),
    )


async def build_owner_inbox(
    message: Message,
    state: FSMContext,
    i18n: I18nContext,
    scope: TransactionScope,
) -> tuple[str, InlineKeyboardMarkup]:
    """Build the owner-facing inbox text and action keyboard in the owner's locale"""
    data = await state.get_data()
    is_anonymous = MessageMode(data.get("mode", MessageMode.DIRECT)) == MessageMode.ANONYMOUS

    owner = await scope.members.by_id(settings.SUDO_ID)
    locale = owner.preferred_lang if owner else Locale.DEFAULT
    user = message.from_user
    body = message.html_text or "—"

    if is_anonymous:
        text = i18n.get("inbox-anon-dialog", locale, message=body)
    else:
        text = i18n.get(
            "inbox-direct-dialog",
            locale,
            name=user.full_name,
            user_id=str(user.id),
            user_name=f"@{user.username}" if user.username else "—",
            message=body,
        )

    keyboard = OwnerInlineKeyboard.inbox(
        i18n,
        user_id=user.id,
        user_message_id=message.message_id,
        locale=locale,
    )
    return text, keyboard


async def send_success_and_clear(
    message: Message,
    state: FSMContext,
    i18n: I18nContext,
) -> None:
    """Confirm delivery and return the user to the main menu"""
    await state.clear()
    await message.answer(
        text=i18n.get("message-delivered-dialog"),
        reply_markup=UserReplyKeyboard.main_menu(i18n),
    )


def _picker_markup(member: Member | None):
    """Pre-build the language picker keyboard with the user's current locale marked"""
    return UserInlineKeyboard.language_menu(
        current=member.preferred_lang if member else None,
    )


__all__ = [
    "enter_mode",
    "build_owner_inbox",
    "send_success_and_clear",
    "_picker_markup",
]
