from aiogram import types


def get_contacts_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Контакты',
                                        url='https://minprom.gov74.ru/minprom/contacts/contact.htm')]
        ]
    )
