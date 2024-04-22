from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    num1: int
    num2: int


@app.post("/calculate")
async def calculate(numbers: Numbers):
    num1 = numbers.num1
    num2 = numbers.num2
    return {f"sum of numbers {num1} and {num2} is ": f"{num1+num2}"}
