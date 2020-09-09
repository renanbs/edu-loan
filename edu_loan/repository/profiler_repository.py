from datetime import date

from injector import inject
from sqlalchemy import func

from edu_loan.config.dependencies import Session
from edu_loan.repository.address_model import Address
from edu_loan.repository.birthday_model import BirthDay
from edu_loan.repository.cpf_model import Cpf
from edu_loan.repository.exceptions import RepositoryException

from edu_loan.domain.profiler_repository_interface import ProfilerRepositoryInterface
from edu_loan.repository.name_model import Name
from edu_loan.repository.phone_model import Phone


class ProfilerRepository(ProfilerRepositoryInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def _save(self, entity) -> None:
        try:
            self.session.add(entity)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def save_cpf(self, user_id: int, cpf: str) -> None:
        self._save(Cpf(user=user_id, cpf=cpf))

    def save_name(self, user_id: int, first: str, last: str) -> None:
        self._save(Name(user=user_id, first_name=first, last_name=last))

    def save_birthday(self, user_id: int, birthday: date) -> None:
        self._save(BirthDay(user=user_id, birthday=birthday))

    def save_phone(self, user_id: int, phone: str) -> None:
        self._save(Phone(user=user_id, phone=phone))

    def save_address(self, user_id: int, cep: str, street: str, number: int,
                     complement: str, city: str, state: str) -> None:
        self._save(Address(user=user_id, cep=cep, street=street, number=number,
                           complement=complement, city=city, state=state))

    def get_last_entity(self, klass, user_id: int):
        return self.session.query(klass).filter(klass.user == user_id).order_by(klass.updated_at.desc()).first()

    def update_timestamp(self, entity) -> None:
        try:
            entity.updated_at = func.now()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)
