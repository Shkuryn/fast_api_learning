import uvicorn
from fastapi import FastAPI
from models.models import UserCreate

title = "My first App"


app = FastAPI(title=title)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


@app.post("/create_user")
async def create_user(new_user: UserCreate):
    return new_user
