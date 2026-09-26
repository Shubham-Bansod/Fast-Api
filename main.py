from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

users = {}

@app.get("/health")
def home():
    return {"Running"}

@app.post("/users")
def create_user(user: User):
    user_id = len(users) + 1

    users[user_id] = {
         "id": user_id,
        "name": user.name,
        "age": user.age,
        "email": user.email
    }

    return users[user_id]


@app.get("/users/{user_id}")
def getUsers(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[user_id]

@app.get("/users")
def getUsers():

    return users

@app.delete("/users/{user_id}")
def deleteUser(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    del users[user_id]

    return {"delete user"}

@app.put("/users/{user_id}")
def update_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = {
        
        "name": "priyanka",
    }

    return users[user_id]

@app.patch("/users/{user_id}")
def update_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id]["name"] = "priyankla"


    return users[user_id]
