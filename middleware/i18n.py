from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiogram_i18n.managers import BaseManager

from enums.locale import LocaleEnum

if TYPE_CHECKING:
    from aiogram.types import User
    from database import Member


class LexiconManager(BaseManager):
    """custom locale manager for aiogram_i18n"""

    default_locale = LocaleEnum.DEFAULT

    async def get_locale(
        self,
        event_from_user: User | None = None,
        **kwargs: Any,
    ) -> str:
        """
        retrieve the user's current locale

        :param event_from_user: The Telegram user who triggered the event
        :type event_from_user: User | None
        :param kwargs: additional keyword arguments; expected to contain
            a "member" key with a `Member` instance if available
        :type kwargs: Any
        :return: a locale code (e.g., "en", "fa").
        :rtype: str
        """
        member: Member = kwargs.get("member")
        if member and hasattr(member, "preferred_lang"):
            return member.preferred_lang

        if event_from_user and event_from_user.language_code:
            return event_from_user.language_code

        return self.default_locale

    async def set_locale(
        self,
        locale: str,
        event_from_user: User | None = None,
        **kwargs: Any,
    ) -> None:
        """
        change the user's locale.

        :param locale: the new locale language code
        :type locale: str
        :param event_from_user: the Telegram user who triggered the event
        :type event_from_user: User | None
        :param kwargs: additional keyword arguments; expected to contain
            a "member" key with a `Member` instance if available
        :type kwargs: Any
        :return: None
        """
        member = kwargs.get("member")
        if member:
            member.preferred_lang = locale
