from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin
from edu_loan.repository.users_model import Users

Base = declarative_base()


class Name(Base, TimestampedMixin):
    __tablename__ = 'name'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(70))
    user = Column(Integer, ForeignKey(Users.id), nullable=False)

    def is_eq(self, first, last):
        return self.first_name == first and self.last_name == last
