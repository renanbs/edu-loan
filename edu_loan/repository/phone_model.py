from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin
from edu_loan.repository.users_model import Users

Base = declarative_base()


class Phone(Base, TimestampedMixin):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    phone = Column(String(11), nullable=False)
    user = Column(Integer, ForeignKey(Users.id), nullable=False)

    def is_eq(self, phone):
        return self.phone == phone
