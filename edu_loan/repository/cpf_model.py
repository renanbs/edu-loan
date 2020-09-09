from pycpfcnpj import cpfcnpj
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

from edu_loan.repository.mixins import TimestampedMixin
from edu_loan.repository.users_model import Users

Base = declarative_base()


class Cpf(Base, TimestampedMixin):
    __tablename__ = 'cpf'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    cpf = Column(String(11), unique=True)
    user = Column(Integer, ForeignKey(Users.id), nullable=False)

    @validates('cpf')
    def validate_cpf(self, key, cnpj) -> str:
        if not len(cnpj) == 11:
            raise ValueError('invalid cpf')
        if not cpfcnpj.validate(cnpj):
            raise ValueError('invalid cpf')
        return cnpj

    def __eq__(self, other):
        return self.cpf == other.cpf
