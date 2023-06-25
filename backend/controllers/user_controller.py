import os

from fastapi import APIRouter

from controllers.dto.create_user_dto import CreateUserDTO
from data.databaseservice import DatabaseService
from services.user_service import UserService

user_router = APIRouter()

user_service = UserService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@user_router.post("/create")
async def create_user(user: CreateUserDTO):
    return await user_service.create_user(user.login, user.name, user.surname, user.password)

@user_router.get("/statistics/{user_id}")
async def create_user(user_id: int):
    return await user_service.get_statistics(user_id)

