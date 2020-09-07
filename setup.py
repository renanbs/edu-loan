from setuptools import setup, find_packages

setup(name='edu_loan',
      description='Education Loan Service',
      long_description='This is just a education loan service',
      packages=find_packages(exclude=["*tests*"]),
      version='1.0.0',
      install_requires=[
          'Flask==1.1.2',
          'injector==0.16.0',
          'pycpfcnpj==1.5.1',
          'marshmallow==3.7.1',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.6.0',
              'pytest==6.0.1',
              'pytest-cov==2.10.1',
              'requests-mock==1.8.0',
              'pytest-mock==3.3.1',
              'pytest-sugar==0.9.4',
              'pytest-lazy-fixture==0.6.3',
              'flake8==3.8.3',
          ],
      }
      )
