from enum import StrEnum, auto

class InboxAction(StrEnum):
    """Owner actions available on an incoming (relayed) message"""
    REPLY = auto()
    BLOCK = auto()
    UNBLOCK = auto()
    REACT = auto()