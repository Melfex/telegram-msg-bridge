from enum import auto, StrEnum
from typing import Final


class Locale(StrEnum):
    """Supported language locales for the bot's i18n localization module"""
    EN = auto()
    RU = auto()
    UK = auto()
    ES = auto()
    UZ = auto()
    PT = auto()
    DE = auto()
    IT = auto()
    FR = auto()
    TR = auto()
    HE = auto()
    AR = auto()
    FA = auto()
    ZH = auto()
    ID = auto()
    SV = auto()
    MS = auto()
    NL = auto()
    HI = auto()
    KO = auto()
    VI = auto()

    DEFAULT = FA


LANGUAGES: Final[dict[Locale, str]] = {
    Locale.EN: "🇬🇧 English",
    Locale.RU: "🇷🇺 Русский",
    Locale.UK: "🇺🇦 Українська",
    Locale.ES: "🇪🇸 Español",
    Locale.UZ: "🇺🇿 Oʻzbek",
    Locale.PT: "🇧🇷 Português",
    Locale.DE: "🇩🇪 Deutsch",
    Locale.IT: "🇮🇹 Italiano",
    Locale.FR: "🇫🇷 Français",
    Locale.TR: "🇹🇷 Türkçe",
    Locale.HE: "🇮🇱 עברית",
    Locale.AR: "🇸🇦 العربية",
    Locale.FA: "فارسی",
    Locale.ZH: "🇨🇳 中文",
    Locale.ID: "🇮🇩 Bahasa Indonesia",
    Locale.SV: "🇸🇪 Svenska",
    Locale.MS: "🇲🇾 Bahasa Melayu",
    Locale.NL: "🇳🇱 Nederlands",
    Locale.HI: "🇮🇳 हिन्दी",
    Locale.KO: "🇰🇷 한국어",
    Locale.VI: "🇻🇳 Tiếng Việt",
}
