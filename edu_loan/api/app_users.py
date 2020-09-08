import json
from http import HTTPStatus

from flask import Blueprint, request

from injector import inject

from edu_loan.api.serializers import UsersSerializer, SerializerException
from edu_loan.config.dependencies import Application
from edu_loan.domain.users_service import UsersService, UsersServiceException


class UsersEndpoint:

    @inject
    def __init__(self, app: Application, users_service: UsersService):
        self.app = app
        self.users_service = users_service

    def register_endpoints(self):
        app_bp = Blueprint('UsersApp', __name__)

        @self.app.route('/api/v1/users/cpf', methods=['POST'])
        def cpf():
            try:
                serializer = UsersSerializer(json.loads(request.data))
                serializer.is_valid()

                self.users_service.save_cpf(serializer.get('token'), serializer.get('data'))
                return {'status': 'ok'}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/full-name', methods=['POST'])
        def full_name():
            pass

        @self.app.route('/api/v1/users/birthday', methods=['POST'])
        def birthday():
            pass

        @self.app.route('/api/v1/users/phone', methods=['POST'])
        def phone():
            pass

        @self.app.route('/api/v1/users/address', methods=['POST'])
        def address():
            pass

        return app_bp
