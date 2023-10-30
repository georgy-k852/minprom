from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from models.app import User
from services.text_message import get_text_message_service
from telegram.keyboards import base as base_keyboard

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: types.Message, user: User, state: FSMContext,
                _text_service=get_text_message_service()):
    text = await _text_service.get_by_name('start-message')
    keyboard = base_keyboard.get_start_keyboard()
    await message.answer(text.text, reply_markup=keyboard)
