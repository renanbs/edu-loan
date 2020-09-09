from abc import ABC, abstractmethod


class EventFlowRepositoryInterface(ABC):
    @abstractmethod
    def add(self, flow: list) -> None:
        pass

    @abstractmethod
    def get(self) -> str:
        pass
