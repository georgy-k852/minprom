from aiogram import types, Router, F
from aiogram.filters import Filter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from models.app import User
from services.order import get_order_service

router = Router()


class AdminFilter(Filter):
    async def __call__(self, event: types.Message | types.CallbackQuery, user: User) -> User | None:
        return user if 'admin' in user.roles else None


@router.message(Command(commands=["admin"]), AdminFilter())
async def admin_panel(message: types.Message, user: User, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text='Выгрузка отчета', callback_data='send_order')]]
    )
    await message.answer('Панель администратора', reply_markup=keyboard)


@router.callback_query(F.data == 'send_order', AdminFilter())
async def change_block_staff(query: types.CallbackQuery, user: User, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='xlsx', callback_data='send_order_xlsx')],
            [types.InlineKeyboardButton(text='ods', callback_data='send_order_ods')]
        ]
    )
    await query.message.edit_text('Выберите формат выгрузки', reply_markup=keyboard)


@router.callback_query(F.data == 'send_order_xlsx', AdminFilter())
async def change_block_staff(query: types.CallbackQuery, user: User, state: FSMContext,
                             _order_service=get_order_service()):
    output = await _order_service.get_admin_order_xlsx()
    input_file = types.BufferedInputFile(output.read(), filename=f'Отчет.xlsx')

    await query.message.answer_document(input_file)


@router.callback_query(F.data == 'send_order_ods', AdminFilter())
async def change_block_staff(query: types.CallbackQuery, user: User, state: FSMContext,
                             _order_service=get_order_service()):
    output = await _order_service.get_admin_order_ods()
    input_file = types.BufferedInputFile(output.read(), filename=f'Отчет.ods')

    await query.message.answer_document(input_file)
