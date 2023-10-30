import datetime

from pydantic import BaseModel, Field


class AppealView(BaseModel):
    n: int = Field()
    date: str = Field()
    text: str = Field()
