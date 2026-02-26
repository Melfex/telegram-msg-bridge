from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import BotCommandScopeChat, BotCommandScopeDefault, BotCommand

if TYPE_CHECKING:
    from aiogram import Bot


async def delete_bot_commands(bot: Bot, chat_id: int | str | None = None) -> None:
    """
    remove all bot commands

    :param bot: Bot instance
    :param chat_id: Chat ID

    :return: None
    """

    await bot.delete_my_commands(
        scope=(
            BotCommandScopeChat(chat_id=chat_id)
            if chat_id
            else BotCommandScopeDefault()
        )
    )


async def setup_bot_commands(bot: Bot, chat_id: int | str | None = None) -> None:
    """
    set and initial bot commands

    :param bot: Bot instance
    :param chat_id: Chat ID

    :return: None
    """
    await delete_bot_commands(bot)
    await bot.set_my_commands(
        commands=[
            BotCommand(command="", description=""),
            BotCommand(command="", description=""),
            BotCommand(command="", description=""),
        ],
        scope=(
            BotCommandScopeChat(chat_id=chat_id)
            if chat_id
            else BotCommandScopeDefault()
        ),
    )
