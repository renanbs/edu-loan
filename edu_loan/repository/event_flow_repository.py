from injector import inject

from sqlalchemy.orm.exc import NoResultFound

from edu_loan.config.dependencies import Session
from edu_loan.domain.event_flow_repository_interface import EventFlowRepositoryInterface
from edu_loan.repository.event_flow_model import EventFlow
from edu_loan.repository.exceptions import RepositoryException


class EventFlowRepository(EventFlowRepositoryInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def add(self, events: list) -> None:
        try:
            event_flow = ','.join(events)
            saved_event_flow = self.session.query(EventFlow).first()
            if not saved_event_flow:
                event_flow = EventFlow(event_flow=event_flow)
                self.session.add(event_flow)
                self.session.commit()
                return

            saved_event_flow.event_flow = event_flow
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def get(self) -> str:
        try:
            return self.session.query(EventFlow).first().event_flow
        except NoResultFound as e:
            raise RepositoryException(e)
