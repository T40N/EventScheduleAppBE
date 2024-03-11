from pydantic import BaseModel


class UserDeleteDto(BaseModel):
    id: str
    message: str
