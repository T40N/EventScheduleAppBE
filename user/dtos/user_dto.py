from datetime import datetime
from pydantic import BaseModel

from event.dtos.event_dto import EventDto


class UserDto(BaseModel):
    email: str
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime
    participated_events: list[EventDto]
    organized_events: list[EventDto]
    access_level: int

    class Config:
        from_attributes = True


