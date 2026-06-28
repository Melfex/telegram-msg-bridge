"""Unit tests for pure helpers in ``handler/sudo/helper.py``."""

from __future__ import annotations

import pytest

from handler.sudo.helper import parse_user_id, strip_html


class TestParseUserId:
    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("123", 123),
            ("  456  ", 456),  # surrounding whitespace trimmed
            ("-100200300", -100200300),  # negative chat ids allowed
            ("0", 0),
        ],
    )
    def test_valid_ids(self, raw: str, expected: int) -> None:
        assert parse_user_id(raw) == expected

    @pytest.mark.parametrize(
        "raw",
        [None, "", "   ", "abc", "12a", "12.5", "+-1", "--1", "1 2"],
    )
    def test_invalid_ids_return_none(self, raw: str | None) -> None:
        assert parse_user_id(raw) is None


class TestStripHtml:
    def test_removes_tags(self) -> None:
        assert strip_html("<b>Hello</b>") == "Hello"

    def test_removes_tags(self) -> None:
        assert strip_html("<b>The bot is <i>offline</i></b> now") == (
            "The bot is offline now"
        )

    def test_trims_surrounding_whitespace(self) -> None:
        assert strip_html("  <b>x</b>  ") == "x"

    def test_plain_text_unchanged(self) -> None:
        assert strip_html("no tags here") == "no tags here"
