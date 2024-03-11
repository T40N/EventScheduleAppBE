from fastapi import APIRouter

from user.dtos.user_create_dto import UserCreateDto
from user.dtos.user_delete_dto import UserDeleteDto
from user.dtos.user_dto import UserDto


userRouter = APIRouter()


@userRouter.get("/users/", response_model=list[UserDto])
async def get_users():
    return {"message": "Get all user"}


@userRouter.get("/users/{user_id}", response_model=UserDto)
async def get_user(user_id: str):
    return {"message": f"Get user with id {user_id}"}


@userRouter.post("/users/", response_model=UserDto)
async def get_user(user_id: str):
    return {"message": f"Get user with id {user_id}"}


@userRouter.post("/users/", response_model=UserDto)
async def create_user(user_create_dto: UserCreateDto) -> UserDto:
    created_user = UserDto(id="1", **user_create_dto.model_dump())
    return created_user


@userRouter.put("/users/{user_id}", response_model=UserDto)
async def update_user(user_id: str):
    return {"message": f"Update user with id {user_id}"}


@userRouter.delete("/users/{user_id}", response_model=UserDeleteDto)
async def delete_user(user_id: str):
    return {"message": f"Delete user with id {user_id}"}


async def login_user(self, user_id: str):
    return {"message": f"Login user with id {user_id}"}
