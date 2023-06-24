import os

from fastapi import APIRouter, HTTPException

from controllers.dto.login_data_dto import LoginDataDTO
from data.databaseservice import DatabaseService
from services.jwt_service import JWTService
from services.user_service import UserService

auth_router = APIRouter()
user_service = UserService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))
jwt_service = JWTService()


@auth_router.post("/login")
async def login(login_data: LoginDataDTO):
    if await user_service.check_user_password(login_data.login, login_data.password):
        return {"accessToken": jwt_service.generate_jwt()}
    raise HTTPException(401, "Неверный логин или пароль")
