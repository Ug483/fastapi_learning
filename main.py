#day 6 crud basics in memory data
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -----------------------------
# Pydantic Models
# -----------------------------

# Input model (client sends this)
class UserIn(BaseModel):
    username: str
    password: str

# Output model (client receives this)
class UserOut(BaseModel):
    username: str

# -----------------------------
# In-Memory Storage (RAM)
# -----------------------------
users = []  # temporary storage

# -----------------------------
# CREATE USER (POST)
# -----------------------------
@app.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    users.append(user)   # store in memory
    return user          # password auto-hidden

# -----------------------------
# READ USERS (GET)
# -----------------------------
@app.get("/users", response_model=List[UserOut])
def get_users():
    return users
