from aiogram.client.bot import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from core.settings import get_config
from telegram.handlers.users import base
from telegram.handlers.users import subsidies
from telegram.handlers.users import appeal
from telegram.handlers.users import admin
from telegram.handlers.users import prom_catalog
from telegram.middlewares.db_loader import loader_middleware


class Loader:
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    bot = Bot(token=get_config().telegram.token, parse_mode='markdown')

    def init_middlewares(self):
        self.dp.message.outer_middleware(loader_middleware)
        self.dp.callback_query.outer_middleware(loader_middleware)
        self.dp.inline_query.outer_middleware(loader_middleware)

    def init_handlers(self):
        self.dp.include_router(base.router)
        self.dp.include_router(subsidies.router)
        self.dp.include_router(appeal.router)
        self.dp.include_router(admin.router)
        self.dp.include_router(prom_catalog.router)

    async def run(self):
        self.init_middlewares()
        self.init_handlers()
        await self.dp.start_polling(self.bot, skip_updates=True)


telegram_config = Loader()
