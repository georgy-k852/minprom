from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from models.app import User, Appeal
from services.appeal import get_appeal_service
from services.text_message import get_text_message_service
from telegram.states.appeal import Appeal as AppealState
from telegram.keyboards import appeal as appeal_keyboard

router = Router()


@router.callback_query(F.data == 'create-appeal')
async def ask_appeal_process(query: types.CallbackQuery, user: User, state: FSMContext,
                             _text_service=get_text_message_service()):
    await state.set_state(AppealState.text)
    text = await _text_service.get_by_name('ask-appeal')
    await query.message.delete_reply_markup()
    await query.message.edit_text(text.text)


@router.message(AppealState.text)
async def after_okved_process(message: types.Message, user: User, state: FSMContext,
                              _text_service=get_text_message_service(),
                              _appeal_service=get_appeal_service()):
    await state.clear()

    appeal = Appeal()
    appeal.text = message.text
    appeal.user_id = user.id
    await _appeal_service.save(appeal)

    text = await _text_service.get_by_name('after-ask-appeal')
    keyboard = appeal_keyboard.get_contacts_keyboard()
    await message.answer(text.text, reply_markup=keyboard)
