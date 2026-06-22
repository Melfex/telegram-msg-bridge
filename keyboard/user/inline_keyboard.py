from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.button_style import ButtonStyle

from config import social_links as _links_config
from enums import LANGUAGES
from .inline_callback import LanguageCallback


class UserInlineKeyboard:
    """Inline keyboard layouts for regular users"""

    @staticmethod
    def language_menu(current: str | None = None) -> InlineKeyboardMarkup:
        """Build the language picker; the active locale is rendered as a green button"""
        btn = InlineKeyboardBuilder()

        for locale, label in LANGUAGES.items():
            btn.button(
                text=label,
                callback_data=LanguageCallback(locale=locale),
                style=ButtonStyle.SUCCESS if current == locale else None,
            )

        btn.adjust(2)
        return btn.as_markup()

    @staticmethod
    def social_links() -> InlineKeyboardMarkup:
        """Build social profile buttons from config/social_links.json"""
        btn = InlineKeyboardBuilder()

        for link in _links_config.links:
            btn.button(text=link.label, url=str(link.url))

        btn.adjust(1, 2, 1)
        return btn.as_markup()
