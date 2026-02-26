from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from .setup import setup_router, setup_global_filter, setup_middleware

if TYPE_CHECKING:
    from config.setting import BotSettings


def bot_instance(bot_settings: BotSettings) -> Bot:
    """
    create and configure Bot instance

    :param bot_settings: configuration settings
    :return: Bot
    """

    bot: Bot = Bot(
        token=bot_settings.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    return bot


def dispatcher_instance() -> Dispatcher:
    """
    create and configure root router

    :return: Dispatcher
    """

    dispatcher: Dispatcher = Dispatcher(
        name="MAIN-ROUTER",
        storage=MemoryStorage(),
    )
    setup_router(dispatcher)
    setup_global_filter(dispatcher)
    setup_middleware(dispatcher)

    return dispatcher
