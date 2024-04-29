from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root_action():
    return {"surname": "Фамилия", "name": "Имя", "patronymic": "Отчество"}

@app.get("/users")
def users_action():
    return {"phone_number": "8-ХХХ-ХХХ-ХХ-ХХ", "email": "milo@gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": "Смог сделать простое API, используя FastAPI и Docker"}