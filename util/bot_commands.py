from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import BotCommandScopeChat, BotCommandScopeDefault, BotCommand

if TYPE_CHECKING:
    from aiogram import Bot
    from aiogram_i18n import I18nContext


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


async def setup_bot_commands(
        bot: Bot, 
        i18n: I18nContext, 
        chat_id: int | str | None = None
    ) -> None:
    """
    set and initial bot commands

    :param bot: Bot instance
    :param i18n: i18n context
    :param chat_id: Chat ID

    :return: None
    """
    await delete_bot_commands(bot, chat_id)
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description=i18n.get("start-command-discription")),
            BotCommand(command="language", description=i18n.get("language-command-discription")),
            BotCommand(command="help", description=i18n.get("help-command-discription")),
            BotCommand(command="links", description=i18n.get("links-command-discription")),
        ],
        scope=(
            BotCommandScopeChat(chat_id=chat_id)
            if chat_id
            else BotCommandScopeDefault()
        ),
    )
