import uvicorn
from fastapi import FastAPI

title = "My first App"


app = FastAPI(title=title)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}
