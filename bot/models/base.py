import uuid

from sqlalchemy import Column, DateTime, func, UUID


class BaseAppModel:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    creation_date = Column(DateTime, default=func.now())
