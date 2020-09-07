from edu_loan.api.app import initialize
from edu_loan.config.main_module import MODULES

application = initialize(modules=MODULES)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
