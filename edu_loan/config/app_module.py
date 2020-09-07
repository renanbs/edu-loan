from injector import Module, singleton, provider

from edu_loan.api.app_users import UsersEndpoint
from edu_loan.config.default import Config
from edu_loan.config.dependencies import ApplicationRegister, ApplicationConfig


class AppModule(Module):
    @singleton
    @provider
    def register(self) -> ApplicationRegister:
        return [UsersEndpoint, ]

    @provider
    def configuration(self) -> ApplicationConfig:
        return Config
