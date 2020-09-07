from http import HTTPStatus

from flask import Blueprint, request, json

from injector import inject

from edu_loan.api.serializers import AuthSerializer
from edu_loan.config.dependencies import Application
from edu_loan.domain.auth_service import AuthService


class AuthEndpoint:

    @inject
    def __init__(self, app: Application, auth_service: AuthService):
        self.app = app
        self.auth_service = auth_service

    def register_endpoints(self):
        app_bp = Blueprint('AuthApp', __name__)

        @self.app.route('/api/v1/auth/register', methods=['POST'])
        def register():
            serializer = AuthSerializer(json.loads(request.data))
            serializer.is_valid()

            token = self.auth_service.create_new_user(serializer.get('email'), serializer.get('password'))

            return {'token': token}, HTTPStatus.CREATED

        @self.app.route('/api/v1/auth/login', methods=['POST'])
        def login():
            serializer = AuthSerializer(json.loads(request.data))
            serializer.is_valid()

            token = self.auth_service.login(serializer.get('email'), serializer.get('password'))

            return {'token': token}, HTTPStatus.CREATED

        return app_bp
