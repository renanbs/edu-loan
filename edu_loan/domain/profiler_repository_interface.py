from abc import ABC, abstractmethod
from datetime import date


class ProfilerRepositoryInterface(ABC):
    @abstractmethod
    def save_cpf(self, user_id: int, cpf: str) -> None:
        pass

    @abstractmethod
    def save_name(self, user_id: int, first: str, last: str) -> None:
        pass

    @abstractmethod
    def save_birthday(self, user_id: int, birthday: date) -> None:
        pass

    @abstractmethod
    def save_phone(self, user_id: int, phone: str) -> None:
        pass

    @abstractmethod
    def save_address(self, user_id: int, cep: str, street: str, number: int,
                     complement: str, city: str, state: str) -> None:
        pass

    @abstractmethod
    def get_last_entity(self, klass, user_id: int):
        pass

    @abstractmethod
    def update_timestamp(self, entity) -> None:
        pass
