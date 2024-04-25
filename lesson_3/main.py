import uvicorn
from fastapi import FastAPI, Cookie, Response
from typing import Optional, List

from models.models import User

title = "Lesson 3"


app = FastAPI(title=title)

# имитируем хранилище юзеров
sample_user: dict = {
    "username": "user123",
    "password": "password123",
}  # создали тестового юзера, якобы он уже зарегистрирован у нас
fake_db: List[User] = [User(**sample_user)]
# имитируем хранилище сессий
sessions: dict = {}  # это можно хранить в кэше, например в Redis

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


# основная логика программы
@app.post("/login")
async def login(user: User, response: Response):
    for person in fake_db:  # перебрали юзеров в нашем примере базы данных
        if (
            person.username == user.username and person.password == user.password
        ):  # сверили логин и пароль
            session_token = "abc123xyz456"  # тут можно использовать модуль uuid (в продакшене), или модуль random (для выполнения задания), или самому написать рандомное значение куки, т.к. это пример тестовый
            sessions[session_token] = (
                user  # сохранили у себя в словаре сессию, где токен - это ключ, а значение - объект юзера
            )
            response.set_cookie(
                key="session_token", value=session_token, httponly=True
            )  # тут установили куки с защищенным флагом httponly - недоступны для вредоносного JS; флаг secure означает, что куки идут только по HTTPS
            return {"message": "куки установлены"}
    return {
        "message": "Invalid username or password"
    }  # тут можно вернуть что хотите, в ТЗ не конкретезировалось, что делать, если логин/пароль неправильные


@app.get("/user")
async def user_info(session_token=Cookie()):
    user = sessions.get(
        session_token
    )  # ищем в сессиях был ли такой токен создан, и если был, то возвращаем связанного с ним юзера
    if user:
        return (
            user.dict()
        )  # у pydantic моделей есть метод dict(), который делает словарь из модели. Можно сразу хранить словарь в сессии, не суть. Для Pydantic версии > 2 метод переименован в model_dump()
    return {"message": "Unauthorized"}
