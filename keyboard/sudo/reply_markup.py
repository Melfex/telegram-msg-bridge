from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram_i18n import I18nContext

class OwnerReplyKeyboard:
    @staticmethod
    def cancel_button(i18n: I18nContext, locale: str | None = None) -> ReplyKeyboardMarkup:
        """Build the cancel button"""
        btn = ReplyKeyboardBuilder()
        btn.button(
            text=i18n.get("cancel-btn", locale),
        )
        return btn.as_markup(
            resize_keyboard=True,
            placeholder=i18n.get("cancel-btn", locale),
        )