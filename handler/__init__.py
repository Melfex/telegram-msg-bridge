from aiogram import Router

from handler.sudo import setup_sudo_router
from handler.user import setup_user_router


def setup_routers() -> Router:
    master_router = Router()

    master_router.include_router(setup_sudo_router())
    master_router.include_router(setup_user_router())

    return master_router
