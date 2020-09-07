import jwt
from edu_loan.repository.exceptions import RepositoryException
from injector import inject
from werkzeug.security import generate_password_hash, check_password_hash

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface


class AuthServiceException(Exception):
    pass


class AuthService:
    @inject
    def __init__(self, secret_key: str, users_repo: UsersRepositoryInterface):
        self.secret_key = secret_key
        self.users_repo = users_repo

    def _generate_token(self, email: str) -> str:
        token = jwt.encode(payload={'email': email}, key=self.secret_key).decode('utf-8')
        return token

    def _decode_token(self, token: str) -> str:
        payload = jwt.decode(token, self.secret_key)
        return payload['email']

    # TODO: move this method to the user_service
    def create_new_user(self, email: str, password: str) -> str:
        try:
            new_password = generate_password_hash(password, method='pbkdf2:sha256')
            self.users_repo.create_new_user(email, new_password)
            return self._generate_token(email)
        except (ValueError, RepositoryException) as e:
            raise AuthServiceException(str(e))

    def login(self, email: str, password: str) -> str or None:
        try:
            hashed_password = self.users_repo.get_hashed_password_from_user(email)

            if not check_password_hash(hashed_password, password):
                return None

            return self._generate_token(email)
        except (RepositoryException, ValueError) as e:
            raise AuthServiceException(str(e))
