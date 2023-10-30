from functools import lru_cache

from sqlalchemy.future import select

from .base import BaseService
from db.storages import app_context
from models.app import TextMessage


class TextMessageService(BaseService):
    _context = app_context

    async def get_by_name(self, name: str) -> TextMessage:
        async with self.context.session_builder.begin() as session:
            query = select(TextMessage).where(TextMessage.name == name)
            result = await session.execute(query)
            models = result.scalars().first()
            return models


@lru_cache
def get_text_message_service() -> TextMessageService:
    return TextMessageService()
