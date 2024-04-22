import uvicorn
from fastapi import FastAPI
from models.models import User

title = "My first App"


app = FastAPI(title=title)



first_user = {'name': 'John Doe', 'age': 1}
my_user = User(**first_user)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.post("/users")
async def user(usr: User):
     return {"name": usr.name,
            "age": usr.age,
            "is_adult": usr.age>=18}
