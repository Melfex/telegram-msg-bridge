from enum import auto, StrEnum


class Status(StrEnum):
    """
    Enumeration of user account registration and restriction statuses

    Attributes:
        DEFAULT (Status): The initial fallback status applied to new users
    """
    BLOCKED = auto()
    UNBLOCKED = auto()

    DEFAULT = UNBLOCKED
