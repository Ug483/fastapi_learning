#day 2 routes and http method
from fastapi import FastAPI

app = FastAPI()
#get method
@app.get("/hello")
def hello():
    return {"message": "Hello from GET"}


@app.get("/profile")
def profile():
    return {
        "name": "Umang",
        "role": "FastAPI Learner"
    }
#post method
@app.post("/login")
def login():
    return {"status": "Login successful"}

@app.get("/about")
def about():
    return {
        "name": "Umang",
        "course": "B.tech"}