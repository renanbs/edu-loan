from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin

Base = declarative_base()


class EventFlow(Base, TimestampedMixin):
    __tablename__ = 'event_flow'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    event_flow = Column(String)
