from pydantic import BaseModel


class EventDeleteDto(BaseModel):
    id: str
    message: str
