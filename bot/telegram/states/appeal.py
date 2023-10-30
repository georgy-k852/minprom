from aiogram.fsm.state import StatesGroup, State


class Appeal(StatesGroup):
    text = State()
