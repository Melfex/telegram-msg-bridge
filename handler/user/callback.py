from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from structlog import get_logger

from keyboard import LanguageCallback, UserInlineKeyboard, UserReplyKeyboard
from enums import StickerID

if TYPE_CHECKING:
    from aiogram_i18n import I18nContext
    from database import Member

callback_router: Final[Router] = Router(name=__name__)
logger = get_logger(__name__)


@callback_router.callback_query(LanguageCallback.filter())
async def select_language(callback: CallbackQuery, callback_data: LanguageCallback, i18n: I18nContext, member: Member, bot: Bot) -> None:
    """Persist the user's language choice and refresh the menu in the new locale"""
    new_locale = callback_data.locale

    if member.preferred_lang == new_locale:
        await callback.answer()
        return

    await i18n.set_locale(new_locale)
    await callback.message.edit_text(
        text=i18n.get("language-dialog"),
        reply_markup=UserInlineKeyboard.language_menu(current=new_locale),
    )
    await callback.answer(text=i18n.get("language-changed-dialog"))
    await callback.message.answer_sticker(sticker=StickerID.HI_DUCK)
    await callback.message.answer(
        text=i18n.get("start-dialog"),
        reply_markup=UserReplyKeyboard.main_menu(i18n),
    )

    await bot.delete_messages(
        chat_id=callback.message.chat.id,
        message_ids=[callback.message.message_id, callback.message.message_id -1],
    )
