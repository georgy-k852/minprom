from aiogram import types


def get_start_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Субсидии', callback_data='subsidies')],
            [types.InlineKeyboardButton(text='Производительность труда',
                                        url='https://minprom.gov74.ru/minprom/NacProject/PovysheniePrzTrydaPD.htm')],
            [types.InlineKeyboardButton(text='Каталог промышленности',
                                        callback_data='catalog_prom')],
            [types.InlineKeyboardButton(text='Нет нужного ответа', callback_data='create-appeal')],
        ]
    )
