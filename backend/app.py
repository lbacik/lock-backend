
from .repository_abc import RepositoryAbstract


class App:

    def __init__(self, repository: RepositoryAbstract):
        self.repository = repository
        self.init_app()

    def init_app(self) -> None:
        counters = self.repository.get_counters()
        if not counters.get(self.repository.key_successes):
            self.repository.set_counters(
                successes=0,
            )
        if not counters.get(self.repository.key_failures):
            self.repository.set_counters(
                failures=0,
            )
        password = self.repository.get_password()
        if not password:
            self.repository.set_password(password="1234")

    def get_counters(self) -> dict:
        return self.repository.get_counters()

    def reset(self) -> None:
        self.repository.set_counters(
            successes=0,
            failures=0,
        )

    def get_password(self) -> str:
        return self.repository.get_password()

    def set_password(self, password: str) -> None:
        self.repository.set_password(password)

    def do_action(self, password: str) -> bool:
        if password == self.get_password():
            self.repository.increment_successes()
            return True
        else:
            self.repository.increment_failures()
            return False

