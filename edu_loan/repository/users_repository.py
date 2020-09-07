from injector import inject

from sqlalchemy.orm.exc import NoResultFound

from edu_loan.config.dependencies import Session
from edu_loan.repository.exceptions import RepositoryException

from edu_loan.domain.users_repository_interface import UsersRepositoryInterface
from edu_loan.repository.users_model import Users


class UsersRepository(UsersRepositoryInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def create_new_user(self, email: str, hashed_password: str) -> None:
        try:
            user = Users(email=email, password_hash=hashed_password)
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def find_user_by_email(self, email: str) -> Users:
        try:
            return self.session.query(Users).filter(Users.email == email).one()
        except NoResultFound as e:
            raise RepositoryException(e)

    def get_hashed_password_from_user(self, email: str) -> str:
        user = self.find_user_by_email(email)
        return user.password_hash
