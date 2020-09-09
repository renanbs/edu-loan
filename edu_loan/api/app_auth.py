from http import HTTPStatus

from flask import Blueprint, request

from injector import inject

from edu_loan.config.dependencies import Application
from edu_loan.domain.auth_service import AuthService, AuthServiceException
from edu_loan.domain.serializers import AuthSerializer, SerializerException


class AuthEndpoint:

    @inject
    def __init__(self, app: Application, auth_service: AuthService):
        self.app = app
        self.auth_service = auth_service

    def register_endpoints(self):
        app_bp = Blueprint('AuthApp', __name__)

        @self.app.route('/api/v1/auth/register', methods=['POST'])
        def register():
            try:
                serializer = AuthSerializer().load(data=request.get_json())

                token = self.auth_service.create_new_user(serializer.get('email'), serializer.get('password'))
            except (AuthServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

            return {'token': token}, HTTPStatus.CREATED

        @self.app.route('/api/v1/auth/login', methods=['POST'])
        def login():
            try:
                serializer = AuthSerializer().load(data=request.get_json())

                token = self.auth_service.login(serializer.get('email'), serializer.get('password'))

            except (AuthServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

            return {'token': token}, HTTPStatus.CREATED

        return app_bp
