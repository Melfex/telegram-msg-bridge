from __future__ import annotations

from typing import TYPE_CHECKING, Final

from aiogram import Router, F
from aiogram.types import Message
from aiogram_i18n import LazyProxy

from enums import MessageMode
from .helper import enter_mode

if TYPE_CHECKING:
    from aiogram.fsm.context import FSMContext
    from aiogram_i18n import I18nContext

button_router: Final[Router] = Router(name=__name__)


@button_router.message(F.text == LazyProxy("message-btn"))
async def enter_direct_mode(message: Message, state: FSMContext, i18n: I18nContext) -> None:
    """Start composing a direct message"""
    await enter_mode(message, state, i18n, MessageMode.DIRECT)


@button_router.message(F.text == LazyProxy("anonymous-message-btn"))
async def enter_anonymous_mode(message: Message, state: FSMContext, i18n: I18nContext) -> None:
    """Start composing an anonymous message"""
    await enter_mode(message, state, i18n, MessageMode.ANONYMOUS)



