import uvicorn
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.models import User

title = "Lesson 4_1"

app = FastAPI(title=title)
security = HTTPBasic()

USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"})]

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


@app.get("/protected_resource/")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}
