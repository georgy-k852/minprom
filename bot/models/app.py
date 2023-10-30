from sqlalchemy import Column, String, ForeignKey, Table, BigInteger
from sqlalchemy.orm import relationship, Mapped

from db.storages import app_context
from models.base import BaseAppModel


user_role = Table(
    'user_role', app_context.base.metadata,
    Column(BigInteger, primary_key=True, unique=True, autoincrement=True, name='id'),
    Column('user_id', ForeignKey('content.user.id'), primary_key=True),
    Column('role_id', ForeignKey(f'content.role.id'), primary_key=True),
    schema='content'
)


class Role(BaseAppModel, app_context.base):
    __tablename__ = 'role'
    __table_args__ = {'schema': 'content'}

    name = Column(String, unique=True, nullable=False)


class User(BaseAppModel, app_context.base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'content'}

    telegram_id = Column(BigInteger, unique=True, nullable=False)
    telegram_username = Column(String)
    telegram_first_name = Column(String)
    telegram_last_name = Column(String)
    telegram_full_name = Column(String, nullable=False)

    roles_mapped: Mapped[list[Role]] = relationship(Role, secondary=user_role, lazy='subquery')

    @property
    def roles(self) -> list[str]:
        return [x.name for x in self.roles_mapped]


class TextMessage(BaseAppModel, app_context.base):
    __tablename__ = 'text_message'
    __table_args__ = {'schema': 'content'}

    text = Column(String, nullable=False)
    name = Column(String(50), nullable=False)


class Appeal(BaseAppModel, app_context.base):
    __tablename__ = 'appeal'
    __table_args__ = {'schema': 'content'}

    text = Column(String, nullable=False)
    user_id = Column(ForeignKey('content.user.id'))

    user = relationship('User', lazy='joined')


class Link(BaseAppModel, app_context.base):
    __tablename__ = 'link'
    __table_args__ = {'schema': 'content'}

    url = Column(String, nullable=False)
    name = Column(String(100), nullable=False)
    order = Column(String, nullable=False, autoincrement=True, unique=True)
