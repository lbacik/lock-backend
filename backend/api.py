
from .app_factory import create_app_with_redis
from fastapi import FastAPI
from pydantic import BaseModel
from .app import App
from fastapi.responses import Response


backend: App = create_app_with_redis()
app: FastAPI = FastAPI(version="1.1.0", title="Backend API")


class NewPassword(BaseModel):
    password: str


class Request(BaseModel):
    password: str


@app.get("/")
def dashboard() -> dict:
    return backend.get_counters()

@app.put("/reset")
def reset() -> Response:
    backend.reset()
    return Response(status_code=204)

@app.get("/get-password")
def get_password() -> dict:
    return {"password": backend.get_password()}

@app.put("/set-password")
def set_password(new_password: NewPassword) -> Response:
    backend.set_password(new_password.password)
    return Response(status_code=204)

@app.post("/send-request")
def send_request(request: Request) -> dict:
    result: bool = backend.do_action(request.password)
    return {"result": result}

