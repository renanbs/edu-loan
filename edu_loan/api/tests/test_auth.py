from http import HTTPStatus

import pytest

from edu_loan.domain.auth_service import AuthServiceException


@pytest.fixture
def serialized_user():
    return {
        'email': 'juca@email.com',
        'password': '123456'
    }


def test_should_register_user(api_client, mocker, serialized_user):
    mocker.patch('edu_loan.domain.auth_service.AuthService.create_new_user', return_value='my token')
    response = api_client.post('/api/v1/auth/register', json=serialized_user)

    assert response.status_code == HTTPStatus.CREATED
    assert response.get_json() == {'token': 'my token'}


def test_should_not_register_user(api_client, mocker, serialized_user):
    mocker.patch('edu_loan.domain.auth_service.AuthService.create_new_user',
                 side_effect=AuthServiceException('weird error'))
    response = api_client.post('/api/v1/auth/register', json=serialized_user)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}


def test_should_login(api_client, mocker, serialized_user):
    mocker.patch('edu_loan.domain.auth_service.AuthService.login', return_value='my token')
    response = api_client.post('/api/v1/auth/login', json=serialized_user)

    assert response.status_code == HTTPStatus.CREATED
    assert response.get_json() == {'token': 'my token'}


def test_should_not_login(api_client, mocker, serialized_user):
    mocker.patch('edu_loan.domain.auth_service.AuthService.login', side_effect=AuthServiceException('weird error'))
    response = api_client.post('/api/v1/auth/login', json=serialized_user)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'weird error'}
