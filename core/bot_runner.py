from __future__ import annotations

from typing import TYPE_CHECKING

from structlog import get_logger

if TYPE_CHECKING:
    from aiogram import Bot, Dispatcher

logger = get_logger(__name__)


async def startup_polling(bot: Bot):
    """
    delete webhook on startup to ensure polling mode works correctly

    :param bot: Bot instance

    :return: None
    """
    await bot.delete_webhook(drop_pending_updates=True)


async def shutdown_polling(bot: Bot, dispatcher: Dispatcher):
    """
    close storage and bot session on shutdown to release resources

    :param bot: Bot instance
    :param dispatcher: Dispatcher instance

    :return: None
    """
    await dispatcher.storage.close()
    await bot.session.close()


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
