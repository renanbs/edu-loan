from unittest.mock import MagicMock

import jwt
import pytest
from edu_loan.domain.users_service import UsersServiceException


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


def test_should_save_cpf(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
    users_service.profiler_repo.save_cpf = MagicMock()
    users_service._validate_step = MagicMock()

    users_service.save_cpf(juca_token, '12345678910', 'xxx')
    users_service.profiler_repo.save_cpf.assert_called_once()


def test_should_not_save_cpf(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_cpf = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_cpf(juca_token, '12345678910', 'xxx')

    assert str(e.value) == 'weird error'


def test_should_save_name(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
    users_service.profiler_repo.save_name = MagicMock()
    users_service._validate_step = MagicMock()

    users_service.save_name(juca_token, 'Juca name', 'xxx')
    users_service.profiler_repo.save_name.assert_called_once()


def test_should_not_save_name(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_name = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_name(juca_token, 'Juca Name', 'xxx')

    assert str(e.value) == 'weird error'


def test_should_not_save_name_if_ste(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_name = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_name(juca_token, 'Juca Name', 'xxx')

    assert str(e.value) == 'weird error'


def test_should_save_birthday(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
    users_service.profiler_repo.save_birthday = MagicMock()
    users_service._validate_step = MagicMock()

    users_service.save_birthday(juca_token, '1990-06-03', 'xxx')
    users_service.profiler_repo.save_birthday.assert_called_once()


def test_should_not_save_birthday(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_birthday = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_birthday(juca_token, '1990-06-03', 'xxx')

    assert str(e.value) == 'weird error'


def test_should_save_phone(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
    users_service.profiler_repo.save_phone = MagicMock()
    users_service._validate_step = MagicMock()

    users_service.save_phone(juca_token, '51999999999', 'xxx')
    users_service.profiler_repo.save_phone.assert_called_once()


def test_should_not_save_phone(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_phone = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_phone(juca_token, '51999999999', 'xxx')

    assert str(e.value) == 'weird error'


def test_should_save_address(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
    users_service.profiler_repo.save_address = MagicMock()
    users_service._validate_step = MagicMock()

    users_service.save_address(juca_token, '88035640,myaddress,22,apto,floripa,sc', 'xxx')
    users_service.profiler_repo.save_address.assert_called_once()


def test_should_not_save_address(users_service, juca_token):
    users_service.profiler_repo.get_last_entity = MagicMock(side_effect=UsersServiceException('weird error'))
    users_service.profiler_repo.save_address = MagicMock()
    users_service._validate_step = MagicMock()

    with pytest.raises(UsersServiceException) as e:
        users_service.save_address(juca_token, '88035640,myaddress,22,apto,floripa,sc', 'xxx')

    assert str(e.value) == 'weird error'


# def test_should_ensure_steps_order(users_service, juca_token):
#     users_service.profiler_repo.get_last_entity = MagicMock(return_value=None)
#     users_service.profiler_repo.save_phone = MagicMock()
#     users_service._validate_step = MagicMock()
#
#     users_service.save_phone(juca_token, '51999999999', 'xxx')
#     users_service.profiler_repo.save_phone.assert_called_once()
