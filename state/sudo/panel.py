from aiogram.fsm.state import State, StatesGroup


class AdminPanel(StatesGroup):
    """Owner admin-panel flows that expect a follow-up message"""

    BLOCK_USER = State()
    UNBLOCK_USER = State()
    BROADCAST = State()
