from __future__ import annotations

import asyncio
import re
from datetime import datetime
from typing import Final, TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from structlog import get_logger

from keyboard import InboxCallback, OwnerReplyKeyboard
from enums import Locale, Status
from keyboard import OwnerInlineKeyboard
from util import Broadcaster

if TYPE_CHECKING:
    from aiogram import Bot
    from aiogram_i18n import I18nContext
    from database import TransactionScope

logger = get_logger(__name__)

_HTML_TAG_RE: Final[re.Pattern[str]] = re.compile(r"<[^>]+>")


def strip_html(text: str) -> str:
    """Remove HTML tags so a dialog can be shown inside a callback alert/toast"""
    return _HTML_TAG_RE.sub("", text).strip()

#while running in the background
_broadcast_tasks: set[asyncio.Task] = set()


async def set_block_status(
    callback: CallbackQuery,
    callback_data: InboxCallback,
    i18n: I18nContext,
    scope: TransactionScope,
    *,
    blocked: bool,
) -> None:
    """Toggle a member block status and refresh inbox action buttons"""
    member = await scope.members.by_id(callback_data.user_id)
    if member is None:
        member = await scope.members.add(callback_data.user_id)

    member.status = Status.BLOCKED if blocked else Status.UNBLOCKED

    if callback.message is not None:
        await callback.message.edit_reply_markup(
            reply_markup=OwnerInlineKeyboard.inbox(
                i18n,
                user_id=callback_data.user_id,
                user_message_id=callback_data.message_id,
                is_blocked=blocked,
            )
        )

    await callback.answer(
        text=i18n.get("user-blocked-dialog" if blocked else "user-unblocked-dialog"),
        show_alert=True,
    )


async def send_reply_to_user(
    message: Message,
    bot: Bot,
    i18n: I18nContext,
    scope: TransactionScope,
    user_id: int,
) -> None:
    """Deliver the owner's reply to a user in the user's preferred locale"""
    member = await scope.members.by_id(user_id)
    locale = member.preferred_lang if member else Locale.DEFAULT

    text = i18n.get(
        "owner-reply-dialog",
        locale,
        answer_text=message.html_text or "—",
        time=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )

    if message.text:
        await bot.send_message(chat_id=user_id, text=text)
    else:
        await message.copy_to(chat_id=user_id, caption=text)


async def show_panel(message: Message, i18n: I18nContext) -> None:
    """Render the owner admin panel"""
    await message.answer(
        text=i18n.get("panel-dialog"),
        reply_markup=OwnerReplyKeyboard.panel(i18n),
    )


def parse_user_id(text: str | None) -> int | None:
    """Parse a numeric Telegram id from owner input, or ``None`` if invalid"""
    if not text:
        return None
    cleaned = text.strip()
    return int(cleaned) if cleaned.lstrip("-").isdigit() else None


def launch_broadcast(
    bot: Bot,
    i18n: I18nContext,
    *,
    owner_id: int,
    from_chat_id: int,
    message_id: int,
    user_ids: list[int],
) -> None:
    """Fire a broadcast in the background and report the result to the owner"""

    async def _job() -> None:
        try:
            result = await Broadcaster(bot).run(
                from_chat_id=from_chat_id,
                message_id=message_id,
                user_ids=user_ids,
            )
            await bot.send_message(
                chat_id=owner_id,
                text=i18n.get(
                    "broadcast-report-dialog",
                    sent=str(result.sent),
                    failed=str(result.failed),
                    total=str(result.total),
                ),
            )
        except Exception as error:  # noqa: BLE001 - background safety net
            logger.error("broadcast job failed", error=str(error))

    task = asyncio.create_task(_job(), name="broadcast")
    _broadcast_tasks.add(task)
    task.add_done_callback(_broadcast_tasks.discard)


__all__ = [
    "set_block_status",
    "send_reply_to_user",
    "show_panel",
    "parse_user_id",
    "launch_broadcast",
    "strip_html",
]