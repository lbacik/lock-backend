FROM python:3.11

COPY . /opt/backend
WORKDIR /opt/backend

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN ~/.local/bin/poetry install

CMD ["/root/.local/bin/poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "backend.api:app", "--reload"]

EXPOSE 8000

