from http import HTTPStatus

from flask import Blueprint, request

from injector import inject

from edu_loan.config.dependencies import Application
from edu_loan.domain.serializers import CpfSerializer, SerializerException, NameSerializer, BirthDaySerializer, \
    PhoneSerializer, AddressSerializer, AmountSerializer
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
                serializer = CpfSerializer().load(data=request.get_json())

                self.users_service.save_cpf(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/full-name', methods=['POST'])
        def full_name():
            try:
                serializer = NameSerializer().load(data=request.get_json())

                self.users_service.save_name(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/birthday', methods=['POST'])
        def birthday():
            try:
                serializer = BirthDaySerializer().load(data=request.get_json())

                self.users_service.save_birthday(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/phone', methods=['POST'])
        def phone():
            try:
                serializer = PhoneSerializer().load(data=request.get_json())

                self.users_service.save_phone(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/address', methods=['POST'])
        def address():
            try:
                serializer = AddressSerializer().load(data=request.get_json())

                self.users_service.save_address(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        @self.app.route('/api/v1/users/amount', methods=['POST'])
        def loan_amount():
            try:
                serializer = AmountSerializer().load(data=request.get_json())

                self.users_service.save_amount(serializer.get('token'), serializer.get('data'))
                return {'success': True}, HTTPStatus.OK

            except (UsersServiceException, SerializerException) as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

        return app_bp
