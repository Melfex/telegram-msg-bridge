from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router
from aiogram.types import CallbackQuery
from structlog import get_logger

from keyboard import LanguageCallback, UserInlineKeyboard, UserReplyKeyboard
from enums import StickerID

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext
    from database import Member
    from util import DeleteAfter

callback_router: Final[Router] = Router(name=__name__)

_PICKER_TTL: Final[float] = 0.3

logger = get_logger(__name__)


@callback_router.callback_query(LanguageCallback.filter())
async def select_language(
    callback: CallbackQuery,
    callback_data: LanguageCallback,
    i18n: I18nContext,
    member: Member,
    state: FSMContext,
    delete_after: DeleteAfter,
) -> None:
    """Persist the user's language choice, greet them, and tidy the picker"""
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

    data = await state.get_data()
    old_message_ids: list[int] = [callback.message.message_id]
    sticker_id = data.get("lang_sticker_id")

    if sticker_id is not None:
        old_message_ids.append(sticker_id)

    delete_after(callback.message.chat.id, old_message_ids, _PICKER_TTL)
    
    await state.clear()
