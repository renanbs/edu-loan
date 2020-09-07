from unittest.mock import MagicMock

import pytest
from edu_loan.domain.auth_service import AuthService

from injector import Injector

from edu_loan.config.dependencies import DBEngine, Session
from edu_loan.config.main_module import MODULES


@pytest.fixture
def engine():
    return MagicMock()


@pytest.fixture
def session():
    return MagicMock()


@pytest.fixture
def injector(engine, session):
    injector = Injector(MODULES)
    injector.binder.bind(DBEngine, to=engine)
    injector.binder.bind(Session, to=session)

    yield injector


@pytest.fixture
def auth_service():
    return AuthService(secret_key='my secret key', users_repo=MagicMock())
