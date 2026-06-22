from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboard.sudo.inline_callback import InboxCallback
from enums import REACTIONS, InboxAction

if TYPE_CHECKING:
    from aiogram_i18n import I18nContext


class OwnerInlineKeyboard:
    """Inline keyboard layouts shown to the owner"""

    @staticmethod
    def inbox(
        i18n: I18nContext,
        *,
        user_id: int,
        user_message_id: int,
        is_blocked: bool = False,
        locale: str | None = None,
    ) -> InlineKeyboardMarkup:
        """Build the action keyboard attached to an incoming message"""
        btn = InlineKeyboardBuilder()

        for idx, emoji in enumerate(REACTIONS):
            btn.button(
                text=emoji,
                callback_data=InboxCallback(
                    action=InboxAction.REACT,
                    user_id=user_id,
                    message_id=user_message_id,
                    reaction_idx=idx,
                ),
            )

        btn.button(
            text=i18n.get("reply-btn", locale),
            callback_data=InboxCallback(
                action=InboxAction.REPLY,
                user_id=user_id,
                message_id=user_message_id,
            ),
        )

        btn.button(
            text=i18n.get("unblock-btn" if is_blocked else "block-btn", locale),
            callback_data=InboxCallback(
                action=InboxAction.BLOCK if is_blocked else InboxAction.UNBLOCK,
                user_id=user_id,
                message_id=user_message_id,
            ),
        )

        btn.adjust(len(REACTIONS), 1, 1)
        return btn.as_markup()
