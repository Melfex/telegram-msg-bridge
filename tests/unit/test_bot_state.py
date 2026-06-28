"""Unit tests for the in-memory bot on/off state cache"""

from __future__ import annotations

from util import BotStateService


class TestBotStateService:
    def test_starts_unloaded(self) -> None:
        service = BotStateService()
        assert service.loaded is False

    def test_defaults_to_online_when_unloaded(self) -> None:
        # Fail-open: until the real status is known, the bot is considered online
        service = BotStateService()
        assert service.online is True

    def test_set_online_marks_loaded(self) -> None:
        service = BotStateService()
        service.set_online(True)
        assert service.loaded is True
        assert service.online is True

    def test_set_offline(self) -> None:
        service = BotStateService()
        service.set_online(False)
        assert service.loaded is True
        assert service.online is False

    def test_set_online_is_idempotent_and_overridable(self) -> None:
        service = BotStateService()
        service.set_online(False)
        service.set_online(True)
        assert service.online is True
