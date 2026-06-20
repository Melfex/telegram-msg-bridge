from enum import auto, StrEnum


class Locale(StrEnum):
    """Supported language locales for the bot's i18n localization module"""
    FA = auto()
    EN = auto()
    ES = auto()
    AR = auto()

    DEFAULT = EN
