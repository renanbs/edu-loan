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

    def create_new_user(self, email: str, hashed_password: str, event_flow: str) -> None:
        try:
            first_step = event_flow.split(',', maxsplit=1)[0]
            user = Users(email=email, password_hash=hashed_password,
                         event_flow=event_flow, step=first_step, step_index=0)
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

    def save_amount(self, email: str, amount: int) -> None:
        try:
            user = self.find_user_by_email(email)
            user.amount = amount
            user.step_index = user.step_index + 1
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def set_next_step(self, email: str) -> str:
        try:
            user = self.find_user_by_email(email)
            user.step_index = user.step_index + 1
            user.step = user.event_flow.split(',')[user.step_index]
            self.session.commit()
            return user.step
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def get_next_step(self, email: str) -> str:
        user = self.find_user_by_email(email)
        return user.event_flow.split(',')[user.step_index]
