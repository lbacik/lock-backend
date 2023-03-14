FROM python:3.11

ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV REDIS_DB 0

COPY . /opt/backend
WORKDIR /opt/backend

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN ~/.local/bin/poetry config virtualenvs.create false && \
    ~/.local/bin/poetry install --no-root --no-dev --no-interaction --no-ansi

CMD ["/root/.local/bin/poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "backend.api:app", "--reload"]

EXPOSE 8000

