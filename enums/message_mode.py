from enum import StrEnum, auto


class MessageMode(StrEnum):
    """Delivery mode for a user message relayed to the owner"""
    DIRECT = auto()
    ANONYMOUS = auto()
