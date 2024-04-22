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


# Пример пользовательских данных (для демонстрационных целей) 
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

@app.post("/users")
async def user(usr: User):
     return {"name": usr.name,
            "age": usr.age,
            "is_adult": usr.age>=18}
