from functools import lru_cache

from pydantic import BaseSettings, Field, BaseModel
from dotenv import load_dotenv


class PostgresSettings(BaseModel):
    host: str = Field()
    port: int = Field()
    user: str = Field()
    password: str = Field()
    database: str = Field()


class ProjectSettings(BaseModel):
    need_backup: bool = Field()


class Config(BaseSettings):
    postgres: PostgresSettings
    project: ProjectSettings

    class Config:
        env_nested_delimiter = '__'
        env_file = '.env'
        env_file_encoding = 'utf-8'


load_dotenv()


@lru_cache
def get_config() -> Config:
    return Config()
