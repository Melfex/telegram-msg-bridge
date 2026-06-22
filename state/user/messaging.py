from aiogram.fsm.state import State, StatesGroup


class SendMessage(StatesGroup):
    """User flow for composing a message to the owner

    The active delivery mode (:class:`enums.MessageMode`) is kept in the
    FSM context data under the ``mode`` key while in ``waiting``
    """

    WAITING = State()
