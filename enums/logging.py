from enum import StrEnum, auto


class LogLevel(StrEnum):
    """Enumeration of log severity levels used for application log persistence"""
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()
