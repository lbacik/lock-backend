
from ..repository_abc import RepositoryAbstract


class RedisRepository(RepositoryAbstract):

    key_password = "password"

    def __init__(self, redis):
        self.redis = redis

    def decode_to_str(self, key: str) -> str:
        value = self.redis.get(key)
        if value is None:
            return ''
        return value.decode("utf-8")

    def get_password(self) -> str:
        return self.decode_to_str(self.key_password)

    def set_password(self, password: str) -> None:
        self.redis.set(self.key_password, password)

    def get_counters(self) -> dict:
        return {
            self.key_successes: int(self.decode_to_str(self.key_successes)),
            self.key_failures: int(self.decode_to_str(self.key_failures)),
        }

    def set_counters(self, **counters) -> None:
        for key, value in counters.items():
            self.redis.set(key, value)

    def increment_successes(self) -> None:
        self.redis.incr(self.key_successes)

    def increment_failures(self) -> None:
        self.redis.incr(self.key_failures)

