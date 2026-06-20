from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import social_links as _links_config


class UserInlineKeyboard:
    """Inline keyboard layouts for regular users"""

    @staticmethod
    def social_links() -> InlineKeyboardMarkup:
        """Build social profile buttons from config/social_links.json"""
        btn = InlineKeyboardBuilder()

        for link in _links_config.links:
            btn.button(text=link.label, url=str(link.url))

        btn.adjust(1, 2, 1)
        return btn.as_markup()
