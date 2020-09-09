from injector import Module, provider, singleton, inject
from sqlalchemy.orm import sessionmaker

from edu_loan.config.default import Config
from edu_loan.config.dependencies import DBEngine, Session
from sqlalchemy import create_engine

from edu_loan.domain.event_flow_repository_interface import EventFlowRepositoryInterface
from edu_loan.domain.profiler_repository_interface import ProfilerRepositoryInterface
from edu_loan.domain.users_repository_interface import UsersRepositoryInterface
from edu_loan.repository.event_flow_repository import EventFlowRepository
from edu_loan.repository.profiler_repository import ProfilerRepository
from edu_loan.repository.users_repository import UsersRepository


class DbModule(Module):
    def configure(self, binder):
        binder.bind(UsersRepositoryInterface, to=UsersRepository, scope=singleton)
        binder.bind(ProfilerRepositoryInterface, to=ProfilerRepository, scope=singleton)
        binder.bind(EventFlowRepositoryInterface, to=EventFlowRepository, scope=singleton)

    @provider
    @singleton
    def engine(self) -> DBEngine:
        engine = create_engine(Config.DB_URL, connect_args={'check_same_thread': False}, echo=True)
        engine.connect()
        return engine

    @provider
    @singleton
    @inject
    def session(self, engine: DBEngine) -> Session:
        session = sessionmaker(bind=engine)
        return session()
