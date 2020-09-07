import jwt
from flask import current_app
from injector import inject
from werkzeug.security import generate_password_hash, check_password_hash

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface


class AuthService:
    @inject
    def __init__(self, users_repo: UsersRepositoryInterface):
        self.users_repo = users_repo

    @staticmethod
    def _generate_token(email: str) -> str:
        secret_key = current_app.config.get('SECRET_KEY')
        token = jwt.encode(payload={'email': email},
                           key=secret_key).decode('utf-8')
        return token

    @staticmethod
    def _decode_token(token: str) -> str:
        secret_key = current_app.config.get('SECRET_KEY')
        payload = jwt.decode(token, secret_key)
        return payload['email']

    def create_new_user(self, email: str, password: str) -> str:
        new_password = generate_password_hash(password, method='pbkdf2:sha256')
        self.users_repo.create_new_user(email, new_password)
        return self._generate_token(email)

    def login(self, email: str, password: str) -> str or None:
        user = self.users_repo.find_user_by_email(email)

        if not check_password_hash(user.password_hash, password):
            return None

        return self._generate_token(email)
