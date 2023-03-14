
from abc import ABC, abstractmethod


class RepositoryAbstract(ABC):

    key_successes = "successes"
    key_failures = "failures"

    @abstractmethod
    def get_password(self) -> str:
        pass

    @abstractmethod
    def set_password(self, password) -> None:
        pass

    @abstractmethod
    def get_counters(self) -> dict:
        pass

    @abstractmethod
    def set_counters(self, **counters) -> None:
        pass

    @abstractmethod
    def increment_successes(self) -> None:
        pass

    @abstractmethod
    def increment_failures(self) -> None:
        pass

