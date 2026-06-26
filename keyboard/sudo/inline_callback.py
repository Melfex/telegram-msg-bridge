from aiogram.filters.callback_data import CallbackData

from enums import InboxAction, BotStatus


class InboxCallback(CallbackData, prefix="ib"):
    """Callback payload for owner inbox buttons

    Carries everything needed to reply, block, or react without a database
    lookup: ``user_id`` is the original sender, ``message_id`` is that
    sender's message (reaction target), and ``reaction_idx`` indexes
    :data:`enums.REACTIONS` for react actions (``-1`` otherwise)
    """

    action: InboxAction
    user_id: int
    message_id: int = 0
    reaction_idx: int = -1


class BotStatusCallback(CallbackData, prefix="bs"):
    """Callback payload emitted when the owner picks a global bot status"""

    status: BotStatus
