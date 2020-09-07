from flask import Blueprint

from injector import inject


from edu_loan.config.dependencies import Application


class AuthEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('AuthApp', __name__)

        @self.app.route('/api/v1/auth/register', methods=['POST'])
        def register():
            pass

        @self.app.route('/api/v1/auth/login', methods=['POST'])
        def login():
            pass

        return app_bp
