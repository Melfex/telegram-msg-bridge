from aiogram.fsm.state import State, StatesGroup


class OwnerReply(StatesGroup):
    """Owner flow for replying to a specific sender"""

    WAITING = State()
