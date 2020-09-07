from flask import Blueprint

from injector import inject


from edu_loan.config.dependencies import Application


class UsersEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('UsersApp', __name__)

        @self.app.route('/api/v1/users/cpf', methods=['POST'])
        def cpf():
            pass

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
