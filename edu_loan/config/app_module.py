from edu_loan.domain.auth_service import AuthService
from edu_loan.domain.users_repository_interface import UsersRepositoryInterface
from injector import Module, singleton, provider, inject

from edu_loan.api.app_auth import AuthEndpoint
from edu_loan.api.app_users import UsersEndpoint
from edu_loan.config.default import Config
from edu_loan.config.dependencies import ApplicationRegister, ApplicationConfig


class AppModule(Module):
    @singleton
    @provider
    def register(self) -> ApplicationRegister:
        return [UsersEndpoint, AuthEndpoint]

    @provider
    def configuration(self) -> ApplicationConfig:
        return Config

    @provider
    @inject
    def auth_service(self, config: ApplicationConfig, users_repo: UsersRepositoryInterface) -> AuthService:
        return AuthService(config.SECRET_KEY, users_repo)
