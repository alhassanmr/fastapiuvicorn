from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [ 
    User(
        id = "7870aec7-9523-4f2f-94b2-aaa5e6e105d6", 
        first_name = "jamila", 
        last_name = "hassan",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id="ddebcdf8-3541-4d7f-9212-8fe4460a2f9d", 
        first_name="alhasssan", 
        middle_name = "mas", 
        last_name="hassan",
        gender= Gender.male,
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

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db :
        if user.id == user_id:
            db.remove(user)
            return {user}
    raise HTTPException( 
        status_code= 404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db :
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return[user]
    raise HTTPException( 
        status_code= 404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: UUID):
    for user in db :
        if user.id == user_id:
            return[user]
    raise HTTPException( 
        status_code= 404,
        detail=f"user with id: {user_id} does not exist"
    )