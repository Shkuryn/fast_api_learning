from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    is_subscribed: bool
