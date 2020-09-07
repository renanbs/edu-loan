from injector import Module, provider, singleton, inject
from sqlalchemy.orm import sessionmaker

from edu_loan.config.default import Config
from edu_loan.config.dependencies import DBEngine, Session
from sqlalchemy import create_engine


class DbModule(Module):

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
