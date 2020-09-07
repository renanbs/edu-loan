from unittest.mock import MagicMock

import jwt
import pytest
from edu_loan.domain.auth_service import AuthServiceException
from edu_loan.repository.exceptions import RepositoryException


@pytest.fixture
def juca_email():
    return 'juca@juca.com'


@pytest.fixture
def juca_password():
    return 'mypass'


@pytest.fixture
def juca_hashed_password():
    return 'pbkdf2:sha256:150000$hIxkPd6T$1ded75a9dd810725b42af487411497c50c54b5c9c767a1d02d32954d46209673'


@pytest.fixture
def juca_token(auth_service, juca_email):
    return jwt.encode(payload={'email': juca_email}, key=auth_service.secret_key).decode('utf-8')


def test_should_create_new_user(auth_service, juca_email, juca_token):
    token = auth_service.create_new_user(juca_email, 'my real secret password')
    assert token == juca_token


def test_should_not_create_user(auth_service, juca_email):
    auth_service.users_repo.create_new_user = MagicMock(side_effect=RepositoryException('weird error'))

    with pytest.raises(AuthServiceException) as e:
        auth_service.create_new_user(juca_email, 'my real secret password')

    assert str(e.value) == 'weird error'


def test_should_login(auth_service, juca_email, juca_token, juca_password, juca_hashed_password):
    auth_service.users_repo.get_hashed_password_from_user = MagicMock(return_value=juca_hashed_password)

    token = auth_service.login(juca_email, juca_password)
    assert token == juca_token


def test_should_not_login(auth_service, juca_email):
    auth_service.users_repo.get_hashed_password_from_user = MagicMock(side_effect=RepositoryException('weird error'))

    with pytest.raises(AuthServiceException) as e:
        auth_service.login(juca_email, 'my real secret password')

    assert str(e.value) == 'weird error'
