import jwt

from edu_loan.domain.event_flow_repository_interface import EventFlowRepositoryInterface
from edu_loan.repository.exceptions import RepositoryException
from injector import inject
from werkzeug.security import generate_password_hash, check_password_hash

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface


class AuthServiceException(Exception):
    pass


class AuthService:
    @inject
    def __init__(self, secret_key: str, users_repo: UsersRepositoryInterface,
                 event_flow_repo: EventFlowRepositoryInterface):
        self.secret_key = secret_key
        self.users_repo = users_repo
        self.event_flow_repo = event_flow_repo

    def _generate_token(self, email: str) -> str:
        token = jwt.encode(payload={'email': email}, key=self.secret_key, algorithm='HS256').decode('utf-8')
        return token

    def get_email_from_token(self, token: str) -> str:
        payload = jwt.decode(jwt=token, key=self.secret_key, algorithms=['HS256'])
        return payload['email']

    # TODO: move this method to the user_service
    def create_new_user(self, email: str, password: str) -> str:
        try:
            new_password = generate_password_hash(password, method='pbkdf2:sha256')
            event_flow = self.event_flow_repo.get()
            self.users_repo.create_new_user(email, new_password, event_flow=event_flow)
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
