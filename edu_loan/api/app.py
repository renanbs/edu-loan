from flask import Flask
from injector import Injector


from edu_loan.config.default import Config
from edu_loan.config.dependencies import ApplicationRegister, Application
from edu_loan.config.main_module import MODULES, create_injector


def create_app(injector: Injector) -> Flask:
    """
    Creates a Flask app
    :param injector: The injector
    :return: Returns the Flask app
    """
    app_flask = Flask(__name__)
    injector.binder.bind(Application, to=app_flask)
    app_flask.config.from_object(Config)

    registers = injector.get(ApplicationRegister)

    if registers:
        for register in registers:
            try:
                register = injector.get(register)
                register.register_endpoints()
            except Exception as e:
                print(e)
                raise

    return app_flask


def initialize(modules=MODULES):
    injector = create_injector(modules=modules)
    application = create_app(injector)
    return application
