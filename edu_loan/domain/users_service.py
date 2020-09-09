from datetime import date

from edu_loan.domain.auth_service import AuthService
from edu_loan.domain.profiler_repository_interface import ProfilerRepositoryInterface
from edu_loan.repository.address_model import Address
from edu_loan.repository.birthday_model import BirthDay
from edu_loan.repository.cpf_model import Cpf
from edu_loan.repository.exceptions import RepositoryException
from injector import inject

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface
from edu_loan.repository.name_model import Name
from edu_loan.repository.phone_model import Phone


class UsersServiceException(Exception):
    pass


class UsersService:
    @inject
    def __init__(self, auth_service: AuthService, users_repo: UsersRepositoryInterface,
                 profiler_repo: ProfilerRepositoryInterface):
        self.auth_service = auth_service
        self.users_repo = users_repo
        self.profiler_repo = profiler_repo

    def _get_user(self, token):
        email = self.auth_service.get_email_from_token(token)
        return self.users_repo.find_user_by_email(email)

    def save_cpf(self, token: str, cpf: str, url: str):
        try:
            user = self._get_user(token)
            self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)
            last_saved = self.profiler_repo.get_last_entity(Cpf, user.id)

            if not last_saved or last_saved.cpf != cpf:
                self.profiler_repo.save_cpf(user.id, cpf)
                return self.users_repo.set_next_step(user.email)

            self.profiler_repo.update_timestamp(last_saved)
            return self.users_repo.get_next_step(user.email)

        except RepositoryException as e:
            raise UsersServiceException(e)

    def save_name(self, token: str, name: str, url: str):
        try:
            user = self._get_user(token)
            self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)
            last_saved = self.profiler_repo.get_last_entity(Name, user.id)

            first, last = name.split(' ', maxsplit=1)
            if not last_saved or not last_saved.is_eq(first, last):
                self.profiler_repo.save_name(user.id, first, last)
                return self.users_repo.set_next_step(user.email)

            self.profiler_repo.update_timestamp(last_saved)
            return self.users_repo.get_next_step(user.email)

        except RepositoryException as e:
            raise UsersServiceException(e)

    def save_birthday(self, token: str, birthday: date, url: str):
        try:
            user = self._get_user(token)
            self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)
            last_saved = self.profiler_repo.get_last_entity(BirthDay, user.id)

            if not last_saved or not last_saved.is_eq(birthday):
                self.profiler_repo.save_birthday(user.id, birthday)
                return self.users_repo.set_next_step(user.email)

            self.profiler_repo.update_timestamp(last_saved)
            return self.users_repo.get_next_step(user.email)

        except RepositoryException as e:
            raise UsersServiceException(e)

    def save_phone(self, token: str, phone: str, url: str):
        try:
            user = self._get_user(token)
            self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)
            last_saved = self.profiler_repo.get_last_entity(Phone, user.id)

            if not last_saved or not last_saved.is_eq(phone):
                self.profiler_repo.save_phone(user.id, phone)
                return self.users_repo.set_next_step(user.email)

            self.profiler_repo.update_timestamp(last_saved)
            return self.users_repo.get_next_step(user.email)

        except RepositoryException as e:
            raise UsersServiceException(e)

    def save_address(self, token: str, address: str, url: str):
        try:
            user = self._get_user(token)
            self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)
            last_saved = self.profiler_repo.get_last_entity(Address, user.id)

            cep, street, number, complement, city, state = address.split(',', maxsplit=6)

            # not the best place to clear my data
            cep = cep.strip()
            street = street.strip()
            number = int(number)
            complement = complement.strip()
            city = city.strip()
            state = state.strip()

            if not last_saved or not last_saved.is_eq(cep, street, number, complement, city, state):
                self.profiler_repo.save_address(user.id, cep, street, number, complement, city, state)
                return self.users_repo.set_next_step(user.email)

            self.profiler_repo.update_timestamp(last_saved)
            return self.users_repo.get_next_step(user.email)

        except RepositoryException as e:
            raise UsersServiceException(e)

    def save_amount(self, token: str, amount: int, url: str) -> None:
        user = self._get_user(token)
        self._validate_step(user.step, user.step_index, user.event_flow.split(','), url)

        email = self.auth_service.get_email_from_token(token)
        self.users_repo.save_amount(email, amount)

    @staticmethod
    def _validate_step(current_step: str, index: int, event_flow: list, url: str):
        final_endpoint = url.split('/')[-1]

        # this way we can call the same endpoint more than once (updating the timestamp)
        if current_step == event_flow[index] and final_endpoint == current_step:
            return
        last_step = event_flow[index - 1]
        if final_endpoint == last_step:
            return
        raise UsersServiceException(f'Invalid step, please execute {current_step} first')
