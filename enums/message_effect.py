from enum import StrEnum


class MessageEffect(StrEnum):
    """Telegram message effect IDs for `message_effect_id` parameter"""
    FIRE = "5104841245755180586"          # 🔥
    THUMBS_UP = "5107584321108051014"     # 👍
    HEART = "5159385139981059251"         # ❤️
    THUMBS_DOWN = "5104858069142078462"   # 👎
    PARTY_POPPER = "5046509860389126442"  # 🎉
    POOP = "5046589136895476101"          # 💩