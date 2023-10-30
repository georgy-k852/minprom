import os

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from core.settings import get_config
from models.app import User
from services.text_message import get_text_message_service
from telegram.states.subsidies import Subsidies
from telegram.keyboards import subsidies as subsidies_keyboard

router = Router()


@router.callback_query(F.data == 'subsidies')
async def subsidies_process(query: types.CallbackQuery, user: User, state: FSMContext,
                            _text_service=get_text_message_service()):
    await state.set_state(Subsidies.okved2)
    text = await _text_service.get_by_name('ask-okved')
    await query.message.delete_reply_markup()
    await query.message.edit_text(text.text)


@router.message(Subsidies.okved2)
async def after_okved_process(message: types.Message, user: User, state: FSMContext,
                              _text_service=get_text_message_service()):
    await state.clear()
    text = await _text_service.get_by_name('after-ask-okved')
    keyboard = subsidies_keyboard.get_ask_documents_info_keyboard()
    await message.answer(text.text, reply_markup=keyboard)


@router.callback_query(F.data == 'ask-documents-info')
async def ask_documents_info_process(query: types.CallbackQuery, user: User, state: FSMContext,
                                     _text_service=get_text_message_service()):
    text = await _text_service.get_by_name('documents-info')
    keyboard = subsidies_keyboard.get_ask_list_documents_keyboard()
    await query.message.edit_text(text.text, reply_markup=keyboard)


@router.callback_query(F.data == 'ask-documents-list')
async def ask_documents_info_process(query: types.CallbackQuery, user: User, state: FSMContext,
                                     _text_service=get_text_message_service()):
    text = await _text_service.get_by_name('documents-list')
    keyboard = subsidies_keyboard.get_list_documents_keyboard()
    await query.message.edit_text(text.text, reply_markup=keyboard)


@router.callback_query(F.data.startswith('share_doc_'))
async def ask_documents_info_process(query: types.CallbackQuery, user: User, state: FSMContext,
                                     _text_service=get_text_message_service()):
    doc_num = query.data.replace('share_doc_', '')
    doc_name = [x for x in os.listdir(get_config().project.file_dir) if doc_num in x][0]
    with open(get_config().project.file_dir + '/' + doc_name, 'rb') as f:
        filename = [x for x in query.message.reply_markup.inline_keyboard if x[0].callback_data == query.data][0][0].text
        input_file = types.BufferedInputFile(f.read(), filename=f'{filename}.{doc_name.split(".")[-1]}')
        await query.message.answer_document(input_file)
