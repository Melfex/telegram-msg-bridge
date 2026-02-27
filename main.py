import asyncio

from structlog import get_logger

from config import settings
from core import bot_instance, dispatcher_instance
from core import polling_run
from database import db_instance
from util import setup_logging

logger = get_logger(__name__)


async def main() -> None:
    setup_logging(
        log_level="INFO",
        json_format=False,
        log_file="logs/bot.log",
        rotate=True,
        service_name="telegram-msg-bridge",
        environment="development",
    )
    db = db_instance()
    dp = dispatcher_instance()
    bot = bot_instance(bot_settings=settings)
    await db.init_tables()
    logger.info(f"db initialized")
    await polling_run(bot=bot, dispatcher=dp)


if __name__ == "__main__":
    asyncio.run(main())
