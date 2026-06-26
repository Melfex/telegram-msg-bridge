from aiogram import Router

from filter import IsSudo
from .command import command_router
from .button import button_router
from .state import state_router
from .callback import callback_router


def setup_sudo_router() -> Router:
    """Build the sudo-only router subtree"""
    router = Router()

    router.message.filter(IsSudo())
    router.callback_query.filter(IsSudo())

    router.include_router(command_router)
    router.include_router(button_router)
    router.include_router(state_router)
    router.include_router(callback_router)

    return router
