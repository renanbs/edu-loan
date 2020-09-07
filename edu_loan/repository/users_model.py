from pycpfcnpj import cpfcnpj
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

from edu_loan.repository.mixins import TimestampedMixin

Base = declarative_base()


class Users(Base, TimestampedMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True)

    @validates('cpf')
    def validate_cpf(self, key, cnpj) -> str:
        if not len(cnpj) == 11:
            raise ValueError('invalid cpf')
        if not cpfcnpj.validate(cnpj):
            raise ValueError('invalid cpf')
        return cnpj
