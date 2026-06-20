from aiogram import Router

from filter import IsSudo
from .commands import router as commands_router


def setup_sudo_router() -> Router:
    """Build the sudo-only router subtree"""
    router = Router()

    router.message.filter(IsSudo())

    router.include_router(commands_router)

    return router
