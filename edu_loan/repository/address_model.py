from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

from edu_loan.repository.mixins import TimestampedMixin
from edu_loan.repository.users_model import Users

Base = declarative_base()


class Address(Base, TimestampedMixin):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    cep = Column(String(11), nullable=False)
    street = Column(String(11), nullable=False)
    number = Column(Integer, nullable=False)
    complement = Column(String(20), nullable=True)
    city = Column(String(50), nullable=False)
    state = Column(String(2), nullable=False)
    user = Column(Integer, ForeignKey(Users.id), nullable=False)

    def is_eq(self, cep, street, number, complement, city, state):
        return self.cep == cep and \
            self.street == street and \
            self.number == number and \
            self.complement == complement and \
            self.city == city and \
            self.state == state
