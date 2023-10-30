from functools import lru_cache

from sqlalchemy.future import select

from .base import BaseService
from db.storages import app_context
from models.app import Appeal


class AppealService(BaseService):
    _context = app_context

    async def save(self, appeal: Appeal):
        async with self.context.session_builder.begin() as session:
            session.add(appeal)
            await session.commit()


@lru_cache
def get_appeal_service() -> AppealService:
    return AppealService()
