from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class UserInlineKeyboard:
    @staticmethod
    def social_links() -> InlineKeyboardMarkup:
        btn = InlineKeyboardBuilder()

        btn.button(
            text="GitHub",
            url="https://github.com/Melfex",
        )
        btn.button(
            text="Instagram",
            url="https://www.instagram.com/askari_farshad",
        )
        btn.button(
            text="Twitter",
            url="https://twitter.com/it.frshd",
        )

        btn.adjust(1, 2)
        return btn.as_markup()