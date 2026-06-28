"""Unit tests for Telegram ``language_code`` -> supported locale mapping."""

from __future__ import annotations

import pytest

from enums import Locale
from middleware.user import _normalize_locale


class TestNormalizeLocale:
    @pytest.mark.parametrize(
        "language_code, expected",
        [
            ("en", "en"),
            ("ru", "ru"),
            ("EN", "en"),  # case-insensitive
            ("en-US", "en"),  # region stripped
            ("pt-br", "pt"),
            ("FA", "fa"),
        ],
    )
    def test_supported_codes(self, language_code: str, expected: str) -> None:
        assert _normalize_locale(language_code) == expected

    @pytest.mark.parametrize("language_code", [None, "", "xx", "klingon", "zz-ZZ"])
    def test_unsupported_falls_back_to_default(self, language_code: str | None) -> None:
        assert _normalize_locale(language_code) == Locale.DEFAULT

    def test_result_is_always_supported(self) -> None:
        supported = {str(loc) for loc in Locale}
        for code in ("en-GB", "de", "weird", None):
            assert _normalize_locale(code) in supported
