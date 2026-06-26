from __future__ import annotations

from typing import TYPE_CHECKING

from structlog import get_logger

from config import settings
from util import setup_bot_commands, setup_owner_commands

if TYPE_CHECKING:
    from aiogram import Bot, Dispatcher
    from aiogram_i18n import I18nMiddleware
    from util import MessageJanitor

logger = get_logger(__name__)


async def startup_polling(bot: Bot, dispatcher: Dispatcher):
    """
    delete webhook on startup to ensure polling mode works correctly

    :param bot: Bot instance

    :return: None
    """
    i18n: I18nMiddleware = dispatcher["i18n_middleware"]
    with i18n.use_context() as context:
        await setup_bot_commands(bot, context)
        await setup_owner_commands(bot, context, settings.SUDO_ID)
        logger.info("Bot commands setup")

    janitor: MessageJanitor = dispatcher["janitor"]
    janitor.start(bot)

    await bot.delete_webhook(drop_pending_updates=True)


async def shutdown_polling(bot: Bot, dispatcher: Dispatcher):
    """
    close storage and bot session on shutdown to release resources

    :param bot: Bot instance
    :param dispatcher: Dispatcher instance

    :return: None
    """
    janitor: MessageJanitor = dispatcher["janitor"]
    await janitor.stop()

    await dispatcher.storage.close()
    await bot.session.close()

    logger.info("shutdown polling complete")


async def polling_run(bot: Bot, dispatcher: Dispatcher):
    """
    configure and start the bot in polling mode, registering startup/shutdown handlers

    :param bot: Bot instance
    :param dispatcher: Dispatcher instance

    :return: None
    """
    logger.info("starting polling mode..")
    dispatcher.startup.register(startup_polling)
    dispatcher.shutdown.register(shutdown_polling)
    await dispatcher.start_polling(bot)


def webhook_run() -> None:
    """
    TODO: setup webhook
    """
    pass
