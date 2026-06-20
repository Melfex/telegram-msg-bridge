from enum import IntEnum


class Throttle(IntEnum):
    """
    Configuration constants for bot rate-limiting and anti-spam controls.

    Attributes:
        MAX: Maximum number of allowed requests within the time window.
        WINDOW: The rolling time window duration in seconds.
        BLOCK_DURATION: Penalty cooldown duration in seconds for spamming users.
    """
    MAX = 3
    WINDOW = 5
    BLOCK_DURATION = 60
