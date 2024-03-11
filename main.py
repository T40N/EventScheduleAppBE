from fastapi import FastAPI
from user.user_router import userRouter
from event.event_router import eventRouter

app = FastAPI()

app.include_router(eventRouter, prefix="/events", tags=["events"])
app.include_router(userRouter, prefix="/user", tags=["user"])


