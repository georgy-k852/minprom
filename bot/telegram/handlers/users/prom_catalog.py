from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from models.app import User
from services.link import get_link_service
from telegram.keyboards import prom_catalog

router = Router()


@router.callback_query(F.data == 'catalog_prom')
async def catalog_prom_process(query: types.CallbackQuery, user: User, state: FSMContext):
    await query.message.edit_text(text='Выберите реестр производителей', reply_markup=prom_catalog.prom_main())


@router.callback_query(F.data == 'prom_reestr')
async def catalog_prom_process(query: types.CallbackQuery, user: User, state: FSMContext,
                               _link_service=get_link_service()):
    data = await _link_service.get_all()
    await query.message.edit_text(text='Скачать реестр производителей продукции',
                                  reply_markup=prom_catalog.prom_urls(data))