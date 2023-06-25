import os

from fastapi import APIRouter

from controllers.dto.delivery_task_dto import DeliveryTaskDTO
from data.databaseservice import DatabaseService
from services.delivery_task_service import DeliveryTaskService

delivery_task_router = APIRouter()

delivery_task_service = DeliveryTaskService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@delivery_task_router.post("/create")
async def create_user(delivery_task: DeliveryTaskDTO):
    return await delivery_task_service.create_delivery_task(delivery_task)
