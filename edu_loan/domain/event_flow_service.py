from edu_loan.domain.event_flow_repository_interface import EventFlowRepositoryInterface
from edu_loan.repository.exceptions import RepositoryException
from injector import inject


class EventFlowServiceException(Exception):
    pass


class EventFlowService:
    @inject
    def __init__(self, secret_key: str, event_flow_repo: EventFlowRepositoryInterface):
        self.secret_key = secret_key
        self.event_flow_repo = event_flow_repo

    def add_event_flow(self, events: list) -> None:
        try:
            self.event_flow_repo.add(events)
        except (ValueError, RepositoryException) as e:
            raise EventFlowServiceException(str(e))

    def get_event_flow(self) -> str:
        try:
            return self.event_flow_repo.get()
        except RepositoryException as e:
            raise EventFlowServiceException(str(e))
