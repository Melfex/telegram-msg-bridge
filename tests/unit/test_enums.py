"""Sanity checks for the project enums and their declared defaults"""

from __future__ import annotations

from enums import BotStatus, Locale, Status, LANGUAGES, REACTIONS, InboxAction


class TestStatus:
    def test_members(self) -> None:
        assert Status.BLOCKED == "blocked"
        assert Status.UNBLOCKED == "unblocked"

    def test_default_is_unblocked(self) -> None:
        assert Status.DEFAULT is Status.UNBLOCKED


class TestBotStatus:
    def test_members(self) -> None:
        assert BotStatus.ONLINE == "online"
        assert BotStatus.OFFLINE == "offline"
        assert BotStatus.PANEL == "panel"

    def test_default_is_online(self) -> None:
        assert BotStatus.DEFAULT is BotStatus.ONLINE


class TestLocale:
    def test_default_is_persian(self) -> None:
        assert Locale.DEFAULT is Locale.FA

    def test_every_locale_is_two_chars(self) -> None:
        # Member.preferred_lang is String(2); each locale value must fit.
        # Iterating the enum yields canonical members only (DEFAULT is an alias
        # of FA, so it is not double-counted)
        assert all(len(str(loc)) == 2 for loc in Locale)

    def test_languages_cover_all_locales(self) -> None:
        # Every supported locale must have a display label, and vice versa.
        assert set(LANGUAGES.keys()) == set(Locale)


class TestInboxAndReactions:
    def test_inbox_actions(self) -> None:
        assert {a.value for a in InboxAction} == {"reply", "block", "unblock", "react"}

    def test_reactions_non_empty_and_unique(self) -> None:
        assert len(REACTIONS) > 0
        assert len(set(REACTIONS)) == len(REACTIONS)
