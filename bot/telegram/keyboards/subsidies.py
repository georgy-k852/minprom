from aiogram import types


def get_ask_documents_info_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Необходимые документы',
                                        callback_data='ask-documents-info')]
        ]
    )


def get_ask_list_documents_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Скачать документы',
                                        callback_data='ask-documents-list')]
        ]
    )


def get_list_documents_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Приложение 1 (заявка)', callback_data='share_doc_1')],
            [types.InlineKeyboardButton(text='Приложение 2 (информация)', callback_data='share_doc_2')],
            [types.InlineKeyboardButton(text='Приложение 3 (справка-расчет)', callback_data='share_doc_3')],
            [types.InlineKeyboardButton(text='Приложение 4 (паспорт инвестпроекта)', callback_data='share_doc_4')],
            [types.InlineKeyboardButton(text='Приложение 5 (реестр документов)', callback_data='share_doc_5')],
            [types.InlineKeyboardButton(text='Приложение 6 (согласие)', callback_data='share_doc_6')]
        ]
    )
