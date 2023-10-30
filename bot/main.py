import asyncio

from telegram.loader import telegram_config


if __name__ == '__main__':
    asyncio.run(telegram_config.run())
