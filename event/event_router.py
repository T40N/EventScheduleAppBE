from fastapi import APIRouter
from event.dtos.event_dto import EventDto
from event.dtos.event_delete_dto import EventDeleteDto
from event.dtos.event_create_dto import EventCreateDto


eventRouter = APIRouter()


@eventRouter.get("/events/", response_model=list[EventDto])
async def get_events():
    return {"message": "Get all events"}


@eventRouter.get("/events/{event_id}", response_model=EventDto)
async def get_event(event_id: str):
    return {"message": f"Get event with id {event_id}"}


@eventRouter.post("/events/", response_model=EventDto)
async def create_event(event_create_dto: EventCreateDto) -> EventDto:
    created_event = EventDto(id="1", **event_create_dto.model_dump())
    return created_event


@eventRouter.put("/events/{event_id}", response_model=EventDto)
async def update_event(event_id: str):
    return {"message": f"Update event with id {event_id}"}


@eventRouter.delete("/events/{event_id}", response_model=EventDeleteDto)
async def delete_event(event_id: str):
    return {"message": f"Delete event with id {event_id}"}
