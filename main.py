import asyncio

from handler import setup_routers
from instance import bot, dp, logger


async def main() -> None:
    dp.include_routers(setup_routers())
    try:
        logger.info("Bot started..")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.error("Bot closed..")


if __name__ == "__main__":
    asyncio.run(main())
