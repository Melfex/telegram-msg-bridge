from aiogram import Router

from .commands import router as commands_router


def setup_user_router() -> Router:
    router = Router()

    router.include_router(commands_router)

    return router
