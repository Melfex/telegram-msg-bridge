from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import F
from aiogram.enums import ChatType
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore
from structlog import get_logger

from enums.locale import Locale
from handler import setup_sudo_router, setup_user_router
from middleware import (
    DatabaseMiddleware,
    UserMiddleware,
    LexiconManager,
    TTLtMiddleware,
)

if TYPE_CHECKING:
    from aiogram import Dispatcher
    from database import DatabaseConnector

logger = get_logger(__name__)


def setup_router(dispatcher: Dispatcher) -> None:
    """
    setup roter's

    :param dispatcher: instance from root router
    :return: None"""

    dispatcher.include_router(setup_user_router())
    dispatcher.include_router(setup_sudo_router())
    logger.info("setup routers complete")


def setup_global_filter(dispatcher: Dispatcher) -> None:
    """
    setup global filter/filters

    :param dispatcher: instance from root router
    :return: None
    """

    dispatcher.message.filter(F.chat.type == ChatType.PRIVATE)
    logger.info("setup global filter/filters complete")


def setup_middleware(dispatcher: Dispatcher, db_connector: DatabaseConnector) -> None:
    i18n_middleware = dispatcher["i18n_middleware"] = I18nMiddleware(
        core=FluentRuntimeCore(
            path="lexicon/{locale}",
            raise_key_error=False,
        ),
        default_locale=Locale.DEFAULT,
        manager=LexiconManager(),
    )

    dispatcher.update.outer_middleware(DatabaseMiddleware(connector=db_connector))
    dispatcher.update.outer_middleware(UserMiddleware())
    dispatcher.message.outer_middleware(TTLtMiddleware())
    i18n_middleware.setup(dispatcher)
    logger.info("setup middleware complete")
