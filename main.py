from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("a615a9b7-0c64-44da-a0b6-6a322d0e9f74"),
        first_name="John",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("02844d1c-d52f-4c00-ac91-32cc1e1c2325"),
        first_name="Michel",
        last_name="Chandler",
        gender=Gender.male,
        roles=[Role.admin]
    ),
]


@app.get("/")
async def root():
    return {"Hello": "Mundo!"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

