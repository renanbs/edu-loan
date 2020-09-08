from abc import ABC, abstractmethod

from pycpfcnpj import cpfcnpj


class SerializerException(Exception):
    pass


class BaseSerializer(ABC):
    def __init__(self, data: dict):
        self.data = data

    def _has_valid_data(self, key):
        if not self.data.get(key):
            raise SerializerException(f'{key} is required')

    def get(self, key):
        return self.data[key]

    @abstractmethod
    def is_valid(self):
        pass


class AuthSerializer(BaseSerializer):
    def is_valid(self):
        self._has_valid_data('email')
        self._has_valid_data('password')


class UsersSerializer(BaseSerializer):

    def _has_valid_cpf(self, data):
        if not cpfcnpj.validate(self.data.get(data)):
            raise SerializerException('CPF is invalid')

    def is_valid(self):
        self._has_valid_data('token')
        self._has_valid_data('data')
        self._has_valid_cpf('data')
