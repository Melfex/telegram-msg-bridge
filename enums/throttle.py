from enum import IntEnum


class ThrottleEnum(IntEnum):
    MAX = 3
    WINDOW = 5
    BLOCK_DURATION = 60
