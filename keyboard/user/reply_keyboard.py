from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram_i18n import I18nContext


class UserReplyKeyboard:
    """Reply keyboard layouts for regular users"""

    @staticmethod
    def main_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
        """Return the localized main menu keyboard"""
        btn = ReplyKeyboardBuilder()

        btn.button(text=i18n.get("message-btn"))
        btn.button(text=i18n.get("anonymous-message-btn"))
        btn.button(text=i18n.get("links-btn"))
        btn.button(text=i18n.get("help-btn")) 

        btn.adjust(2, 1, 1)
        return btn.as_markup(resize_keyboard=True)

    @staticmethod
    def cancel(i18n: I18nContext) -> ReplyKeyboardMarkup:
        """Return a single-button keyboard for leaving the send flow"""
        btn = ReplyKeyboardBuilder()
        btn.button(text=i18n.get("cancel-btn"))
        return btn.as_markup(resize_keyboard=True)