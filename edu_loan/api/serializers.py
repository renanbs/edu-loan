
class AuthSerializerException(Exception):
    pass


class AuthSerializer:
    def __init__(self, data: dict):
        self.data = data

    def _has_valid_data(self, key):
        if not self.data.get(key):
            raise AuthSerializerException(f'{key} is required')

    def get(self, key):
        return self.data[key].lower()

    def is_valid(self):
        self._has_valid_data('email')
        self._has_valid_data('password')
