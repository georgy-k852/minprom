from functools import lru_cache

from sqlalchemy.future import select

from .base import BaseService
from db.storages import app_context
from models.app import Link


class LinkService(BaseService):
    _context = app_context

    async def get_all(self) -> Link:
        async with self.context.session_builder.begin() as session:
            query = select(Link).order_by(Link.order)
            result = await session.execute(query)
            models = result.scalars().all()
            return models


@lru_cache
def get_link_service() -> LinkService:
    return LinkService()
