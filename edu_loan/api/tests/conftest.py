import pytest
from flask import Flask

from edu_loan.api.app import create_app


@pytest.fixture
def app(injector) -> Flask:
    app = create_app(injector)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'my secret key'

    return app


@pytest.fixture
def api_client(app):
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    return app.test_client()
