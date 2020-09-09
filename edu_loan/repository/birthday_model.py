from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin
from edu_loan.repository.users_model import Users

Base = declarative_base()


class BirthDay(Base, TimestampedMixin):
    __tablename__ = 'birthday'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    birthday = Column(Date)
    user = Column(Integer, ForeignKey(Users.id), nullable=False)

    def is_eq(self, birthday):
        return self.birthday == birthday
