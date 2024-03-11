from pydantic import BaseModel


class UserCreateDto(BaseModel):
    email: str
    name: str
    surname: str
    password: str
    access_level: int
