from aiogram.filters.callback_data import CallbackData

from enums import Locale


class LanguageCallback(CallbackData, prefix="lang"):
    """Callback payload emitted when a user selects a language from the picker"""

    locale: Locale
