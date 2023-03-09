from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [ 
    User(
        id = uuid4(), 
        first_name = "jamila", 
        last_name = "hassan",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="alhas", 
        middle_name = "mas", 
        last_name="hassan",
        gender= Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return { "Hello":" world" }

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id" : user.id}