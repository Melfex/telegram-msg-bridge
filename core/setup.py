from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F
from aiogram.enums import ChatType
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

from database import db_instance
from enums.locale import LocaleEnum
from handler import setup_sudo_router, setup_user_router
from middleware import (
    DatabaseMiddleware,
    UserMiddleware,
    LexiconManager,
    TTLtMiddleware,
)

if TYPE_CHECKING:
    from aiogram import Dispatcher


def setup_router(dispatcher: Dispatcher) -> None:
    """
    setup roter's

    :param dispatcher: instance from root router
    :return: None"""

    dispatcher.include_router(setup_user_router())
    dispatcher.include_router(setup_sudo_router())


def setup_global_filter(dispatcher: Dispatcher) -> None:
    """
    setup global filter/filters

    :param dispatcher: instance from root router
    :return: None
    """

    # filter update only for PRIVATE chat type
    dispatcher.update.filter(F.chat.type == ChatType.PRIVATE)


def setup_middleware(dispatcher: Dispatcher) -> None:
    i18n_middleware = dispatcher["i18n_middleware"] = I18nMiddleware(
        core=FluentRuntimeCore(
            path="lexicon/{locale}",
            raise_key_error=False,
        ),
        default_locale=LocaleEnum.DEFAULT,
        manager=LexiconManager(),
    )

    dispatcher.update.outer_middleware(DatabaseMiddleware(connector=db_instance()))
    dispatcher.update.outer_middleware(UserMiddleware())
    dispatcher.message.middleware(TTLtMiddleware())
    i18n_middleware.setup(dispatcher)
