import os

from fastapi import APIRouter

from controllers.dto.login_data_dto import LoginDataDTO
from data.databaseservice import DatabaseService
from services.user_service import UserService

auth_router = APIRouter()
user_service = UserService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@auth_router.post("/login")
async def login(login_data: LoginDataDTO):
    return await user_service.check_user_password(login_data.login, login_data.password)
