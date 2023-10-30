from functools import lru_cache

from sqlalchemy.future import select

from .base import BaseService
from db.storages import app_context
from models.app import User, Role


class UserService(BaseService):
    _context = app_context

    async def save(self, user: User):
        async with self.context.session_builder.begin() as session:
            session.add(user)
            await session.commit()

    async def get_user_by_id(self, idx: int) -> User:
        async with self.context.session_builder.begin() as session:
            query = select(User).where(User.id == idx)
            result = await session.execute(query)
            model = result.scalars().first()
            return model

    async def get_user_by_telegram_id(self, telegram_idx: int) -> User:
        async with self.context.session_builder.begin() as session:
            query = select(User).where(User.telegram_id == telegram_idx)
            result = await session.execute(query)
            model = result.scalars().first()
            return model

    async def get_user_by_role(self, role: str) -> list[User]:
        async with self.context.session_builder.begin() as session:
            query = select(User).where(User.roles_mapped.any(Role.name == role))
            result = await session.execute(query)
            models = result.scalars().all()
            return models


@lru_cache
def get_user_service() -> UserService:
    return UserService()
