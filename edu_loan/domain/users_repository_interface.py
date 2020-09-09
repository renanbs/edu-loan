from abc import ABC, abstractmethod

from edu_loan.repository.users_model import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create_new_user(self, email: str, hashed_password: str, event_flow: str) -> None:
        pass

    @abstractmethod
    def find_user_by_email(self, email: str) -> Users:
        pass

    @abstractmethod
    def get_hashed_password_from_user(self, email: str) -> str:
        pass

    @abstractmethod
    def save_amount(self, email: str, amount: int) -> None:
        pass

    @abstractmethod
    def set_next_step(self, email: str) -> str:
        pass

    @abstractmethod
    def get_next_step(self, email: str) -> str:
        pass
