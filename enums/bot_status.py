from enum import auto, StrEnum


class BotStatus(StrEnum):
    """Global runtime status of the bot"""
    ONLINE = auto()
    OFFLINE = auto()
    PANEL = auto() 
    "Back to main-panel"

    DEFAULT = ONLINE
