from http import HTTPStatus

import pytest

from edu_loan.domain.users_service import UsersServiceException


@pytest.fixture
def serialized_token():
    return {
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2F'
                 'AanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY',
        'data': '68077335004'
    }


@pytest.fixture
def serialized_cpf(serialized_token):
    serialized_token['data'] = '68077335004'
    return serialized_token


@pytest.fixture
def serialized_name(serialized_token):
    serialized_token['data'] = 'Juca da Silva'
    return serialized_token


@pytest.fixture
def serialized_birthday(serialized_token):
    serialized_token['data'] = '1990-06-03'
    return serialized_token


@pytest.fixture
def serialized_phone(serialized_token):
    serialized_token['data'] = '51999999999'
    return serialized_token


@pytest.fixture
def serialized_address(serialized_token):
    serialized_token['data'] = '88035640,myaddress,22,apto,floripa,sc'
    return serialized_token


@pytest.fixture
def serialized_amount(serialized_token):
    serialized_token['data'] = '123'
    return serialized_token


def test_should_save_cpf(api_client, mocker, serialized_cpf):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_cpf', return_value='my-next-endpoint')
    response = api_client.post('/api/v1/users/cpf', json=serialized_cpf)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True, 'next-endpoint': 'my-next-endpoint'}


def test_should_not_save_cpf(api_client, mocker, serialized_cpf):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_cpf',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/cpf', json=serialized_cpf)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_save_name(api_client, mocker, serialized_name):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_name', return_value='my-next-endpoint')
    response = api_client.post('/api/v1/users/full-name', json=serialized_name)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True, 'next-endpoint': 'my-next-endpoint'}


def test_should_not_save_name(api_client, mocker, serialized_name):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_name',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/full-name', json=serialized_name)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_save_birthday(api_client, mocker, serialized_birthday):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_birthday', return_value='my-next-endpoint')
    response = api_client.post('/api/v1/users/birthday', json=serialized_birthday)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True, 'next-endpoint': 'my-next-endpoint'}


def test_should_not_save_birthday(api_client, mocker, serialized_birthday):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_birthday',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/birthday', json=serialized_birthday)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_save_phone(api_client, mocker, serialized_phone):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_phone', return_value='my-next-endpoint')
    response = api_client.post('/api/v1/users/phone', json=serialized_phone)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True, 'next-endpoint': 'my-next-endpoint'}


def test_should_not_save_phone(api_client, mocker, serialized_phone):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_phone',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/phone', json=serialized_phone)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_save_address(api_client, mocker, serialized_address):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_address', return_value='my-next-endpoint')
    response = api_client.post('/api/v1/users/address', json=serialized_address)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True, 'next-endpoint': 'my-next-endpoint'}


def test_should_not_save_address(api_client, mocker, serialized_address):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_address',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/address', json=serialized_address)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_save_loan_amount(api_client, mocker, serialized_amount):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_amount')
    response = api_client.post('/api/v1/users/amount', json=serialized_amount)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {'success': True}


def test_should_not_save_amount(api_client, mocker, serialized_amount):
    mocker.patch('edu_loan.domain.users_service.UsersService.save_amount',
                 side_effect=UsersServiceException('weird error'))
    response = api_client.post('/api/v1/users/amount', json=serialized_amount)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}
