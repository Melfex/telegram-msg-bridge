import asyncio

from config import settings
from core import bot_instance, dispatcher_instance
from core import polling_run
from database import db_instance


async def main() -> None:
    db = db_instance()
    dp = dispatcher_instance()
    bot = bot_instance(bot_settings=settings)

    await db.init_tables()
    await polling_run(bot=bot, dispatcher=dp)


if __name__ == "__main__":
    asyncio.run(main())
