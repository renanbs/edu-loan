from abc import ABC, abstractmethod


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create_new_user(self, email: str, hashed_password: str) -> None:
        pass

    @abstractmethod
    def find_user_by_email(self, email: str):
        pass
