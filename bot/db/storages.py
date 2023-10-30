from abc import ABC

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import get_config


class BaseAppContext(ABC):
    def __init__(self, engine_url: str):
        self.engine = create_async_engine(engine_url, future=True)
        self.metadata = MetaData()
        self.base = declarative_base()
        self.session_builder = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )


app_context = BaseAppContext(get_config().postgres.dsn)
