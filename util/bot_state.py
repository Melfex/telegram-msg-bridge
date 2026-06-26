from __future__ import annotations


class BotStateService:
    """In-memory, read-through cache of the global bot online/offline status"""

    __slots__ = ("_online",)

    def __init__(self) -> None:
        self._online: bool | None = None

    @property
    def loaded(self) -> bool:
        return self._online is not None

    @property
    def online(self) -> bool:
        return True if self._online is None else self._online

    def set_online(self, value: bool) -> None:
        self._online = value
