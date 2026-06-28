"""Unit tests for the owner inline keyboards

These assert the *structure* and the packed ``callback_data`` payloads so a
regression in button wiring (wrong action, wrong status) is caught immediately
Localized labels are provided by :class:`tests.factories.FakeI18n`, which echoes
the i18n key, keeping these tests independent of the Fluent catalogs
"""

from __future__ import annotations

from aiogram.enums.button_style import ButtonStyle
from aiogram.types import InlineKeyboardButton

from enums import BotStatus, InboxAction, REACTIONS
from keyboard import OwnerInlineKeyboard, UserInlineKeyboard
from keyboard.sudo.inline_callback import BotStatusCallback, InboxCallback
from keyboard.user.inline_callback import LanguageCallback
from tests.factories import FakeI18n


def _flatten(markup) -> list[InlineKeyboardButton]:
    return [button for row in markup.inline_keyboard for button in row]


class TestBotStatusKeyboard:
    def test_layout_and_payloads(self) -> None:
        i18n = FakeI18n()
        markup = OwnerInlineKeyboard.bot_status(i18n, current=BotStatus.ONLINE)

        rows = markup.inline_keyboard
        assert [len(row) for row in rows] == [2, 1]  # adjust(2, 1)

        on_btn, off_btn = rows[0]
        back_btn = rows[1][0]

        assert BotStatusCallback.unpack(on_btn.callback_data).status == BotStatus.ONLINE
        assert BotStatusCallback.unpack(off_btn.callback_data).status == BotStatus.OFFLINE
        assert BotStatusCallback.unpack(back_btn.callback_data).status == BotStatus.PANEL

    def test_current_status_is_highlighted_green(self) -> None:
        i18n = FakeI18n()
        markup = OwnerInlineKeyboard.bot_status(i18n, current=BotStatus.OFFLINE)
        on_btn, off_btn = markup.inline_keyboard[0]

        assert off_btn.style == ButtonStyle.SUCCESS
        assert on_btn.style is None

    def test_requests_expected_labels(self) -> None:
        i18n = FakeI18n()
        OwnerInlineKeyboard.bot_status(i18n, current=BotStatus.ONLINE)
        assert set(i18n.requested_keys) == {
            "bot-status-on-btn",
            "bot-status-off-btn",
            "back-panel-btn",
        }


class TestInboxKeyboard:
    def test_reaction_buttons_indexed_in_order(self) -> None:
        i18n = FakeI18n()
        markup = OwnerInlineKeyboard.inbox(
            i18n, user_id=42, user_message_id=7, is_blocked=False
        )
        buttons = _flatten(markup)
        react_buttons = buttons[: len(REACTIONS)]

        for idx, button in enumerate(react_buttons):
            payload = InboxCallback.unpack(button.callback_data)
            assert payload.action == InboxAction.REACT
            assert payload.reaction_idx == idx
            assert payload.user_id == 42
            assert payload.message_id == 7
            assert button.text == REACTIONS[idx]

    def test_reply_and_block_actions_when_unblocked(self) -> None:
        i18n = FakeI18n()
        markup = OwnerInlineKeyboard.inbox(
            i18n, user_id=42, user_message_id=7, is_blocked=False
        )
        buttons = _flatten(markup)
        reply_btn, action_btn = buttons[len(REACTIONS) : len(REACTIONS) + 2]

        assert InboxCallback.unpack(reply_btn.callback_data).action == InboxAction.REPLY
        # An unblocked user gets a "block" action.
        assert InboxCallback.unpack(action_btn.callback_data).action == InboxAction.UNBLOCK

    def test_action_flips_when_already_blocked(self) -> None:
        i18n = FakeI18n()
        markup = OwnerInlineKeyboard.inbox(
            i18n, user_id=42, user_message_id=7, is_blocked=True
        )
        action_btn = _flatten(markup)[-1]
        assert InboxCallback.unpack(action_btn.callback_data).action == InboxAction.BLOCK


class TestLanguageMenu:
    def test_button_per_language_with_current_highlighted(self) -> None:
        markup = UserInlineKeyboard.language_menu(current="en")
        buttons = _flatten(markup)

        locales = [LanguageCallback.unpack(b.callback_data).locale for b in buttons]
        assert "en" in locales

        highlighted = [b for b in buttons if b.style == ButtonStyle.SUCCESS]
        assert len(highlighted) == 1
        assert LanguageCallback.unpack(highlighted[0].callback_data).locale == "en"

    def test_no_highlight_when_current_is_none(self) -> None:
        markup = UserInlineKeyboard.language_menu(current=None)
        buttons = _flatten(markup)
        assert all(b.style is None for b in buttons)
