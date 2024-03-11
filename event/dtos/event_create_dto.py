from pydantic import BaseModel


class EventCreateDto(BaseModel):
    name: str
    description: str
    startDate: str
    endDate: str
    location: str
