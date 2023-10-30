from typing import Any

from aiogram import types, BaseMiddleware

from models.app import User
from services.user import get_user_service


class LoaderMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler,
            event: types.Message | types.CallbackQuery | types.InlineQuery,
            data: dict[str, Any],
            _service=get_user_service()
    ) -> User:
        if type(event) == types.Message:
            chat = event.chat
        elif type(event) == types.CallbackQuery:
            chat = event.message.chat
        else:
            chat = event.from_user

        user = await _service.get_user_by_telegram_id(chat.id)
        if not user:
            user = User()
            user.telegram_id = chat.id
            user.telegram_username = event.from_user.username
            user.telegram_first_name = event.from_user.first_name
            user.telegram_last_name = event.from_user.last_name
            user.telegram_full_name = event.from_user.full_name
            await _service.save(user)

        data['user'] = user
        return await handler(event, data)


loader_middleware = LoaderMiddleware()
