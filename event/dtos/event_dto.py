from pydantic import BaseModel
from user.dtos.user_dto import UserDto


class EventDto(BaseModel):
    name: str
    description: str
    start_date: str
    end_date: str
    location: str
    organizer_id: str
    created_at: str
    updated_at: str
    organizer: UserDto
    participants: list[UserDto]

    class Config:
        from_attributes = True
