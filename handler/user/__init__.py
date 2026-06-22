from aiogram import Router

from .command import command_router
from .button import button_router
from .state import state_router
from .callback import callback_router


def setup_user_router() -> Router:
    """Build the public user router subtree"""
    router = Router()

    router.include_router(command_router)
    router.include_router(button_router)
    router.include_router(state_router)
    router.include_router(callback_router)

    return router
