from databases import Database
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    Float,
    MetaData,
    String,
    Table,
    create_engine,
    func,
)

from config import settings
from constants import DB_NAMING_CONVENTION

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

database = Database(DATABASE_URL, force_rollback=settings.ENVIRONMENT.is_testing)


users = Table(
    'users',
    metadata,
    Column('id', Integer, Identity(), primary_key=True),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('avatar_url', String),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('updated_at', DateTime, onupdate=func.now()),
)

banks = Table(
    'banks',
    metadata,
    Column('id', Integer, Identity(), primary_key=True),
    Column('name', String, nullable=False),
    Column('logo_url', String),
    Column('color', String),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('updated_at', DateTime, onupdate=func.now()),
)

users_accounts = Table(
    'users_accounts',
    metadata,
    Column('id', Integer, Identity(), primary_key=True),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('account_id', ForeignKey('accounts.id'), nullable=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('updated_at', DateTime, onupdate=func.now()),
)

accounts = Table(
    'accounts',
    metadata,
    Column('id', Integer, Identity(), primary_key=True),
    Column('account_number', String, nullable=False),
    Column('bank_id', ForeignKey('banks.id', ondelete='CASCADE'), nullable=False),
    Column('balance', Float, nullable=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('updated_at', DateTime, onupdate=func.now()),
)

cards = Table(
    'cards',
    metadata,
    Column('id', Integer, Identity(), primary_key=True),
    Column('card_number', String, nullable=False),
    Column('account_id', ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False),
    Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    Column('logo_url', String),
    Column('color', String),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('updated_at', DateTime, onupdate=func.now()),
)
