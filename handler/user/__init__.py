from aiogram import Router

from .commands import command_router


def setup_user_router() -> Router:
    router = Router()

    router.include_router(command_router)

    return router
