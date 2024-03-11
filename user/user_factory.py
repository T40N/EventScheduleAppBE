from user.dtos.user_create_dto import UserCreateDto
from user.user_model import User


class UserFactory:
    @staticmethod
    def from_dto(user_create_dto: UserCreateDto) -> User:
        return User(
            name=user_create_dto.username,
            surname=user_create_dto.surname,
            email=user_create_dto.email,
            password=user_create_dto.password,
            access_level=user_create_dto.access_level
        )
