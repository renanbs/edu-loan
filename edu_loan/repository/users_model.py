from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin

Base = declarative_base()


class Users(Base, TimestampedMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=True)
