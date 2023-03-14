import os

from dotenv import load_dotenv
from redis import Redis
from .repository_abc import RepositoryAbstract
from .repository.redis import RedisRepository
from .app import App


def create_app_with_redis() -> App:

    load_dotenv()

    host: str = os.getenv("REDIS_HOST") or "localhost"
    port: str|int = os.getenv("REDIS_PORT") or 6379
    db: str|int = os.getenv("REDIS_DB") or 0

    redis: Redis = Redis(host=host, port=int(port), db=int(db))
    repository: RepositoryAbstract = RedisRepository(redis)
    backend: App = App(repository)

    return backend

