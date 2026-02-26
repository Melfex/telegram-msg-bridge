from enum import auto, StrEnum


class StatusEnum(StrEnum):
    BLOCKED = auto()
    UNBLOCKED = auto()

    DEFAULT = UNBLOCKED
