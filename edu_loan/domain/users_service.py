from edu_loan.domain.auth_service import AuthService
from edu_loan.repository.exceptions import RepositoryException
from injector import inject

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface


class UsersServiceException(Exception):
    pass


class UsersService:
    @inject
    def __init__(self, auth_service: AuthService, users_repo: UsersRepositoryInterface):
        self.auth_service = auth_service
        self.users_repo = users_repo

    def save_cpf(self, token: str, cpf: str):
        try:
            email = self.auth_service.get_email_from_token(token)
            self.users_repo.save_cpf(email, cpf)
        except RepositoryException as e:
            raise UsersServiceException(e)
