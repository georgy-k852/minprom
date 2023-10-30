from aiogram import types

from models.app import Link


def prom_main() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Реестр производителей продукции', callback_data='prom_reestr')],
            [types.InlineKeyboardButton(text='Включение в реестр производителей', callback_data='add_to_prom_reestr')]
        ]
    )


def prom_urls(data: list[Link]) -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text=x.name, url=x.url)] for x in data
        ]
    )
