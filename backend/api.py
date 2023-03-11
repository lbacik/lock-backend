
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Password(BaseModel):
    password: str


class Request(BaseModel):
    password: str
    data: int = 0


class Counters(BaseModel):
    successes: int = 0
    failures: int = 0


password: Password = Password(password="1234")
counters: Counters = Counters()

@app.get("/")
def dashboard():
    return {"successes": counters.successes, "failures": counters.failures}

@app.get("/reset")
def reset():
    counters.successes = 0
    counters.failures = 0
    password.password = "1234"
    return {"successes": counters.successes, "failures": counters.failures}

@app.get("/get-password")
def get_password():
    return {"password": password.password}

@app.put("/set-password")
def set_password(new_password: Password):
    password.password = new_password.password
    return {"password": password.password}

@app.post("/send-request")
def send_request(request: Request):
    if request.password == password.password:
        counters.successes += 1
        return {"success": True}
    else:
        counters.failures += 1
        return {"success": False, "error": "Wrong password"}

