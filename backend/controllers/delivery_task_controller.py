import os
from typing import List

from fastapi import APIRouter

from controllers.dto.delivery_task_change_status_dto import DeliveryTaskChangeStatusDTO
from controllers.dto.delivery_task_dto import DeliveryTaskDTO
from controllers.dto.response.delivery_task_response_dto import DeliveryTaskResponseDto
from data.databaseservice import DatabaseService
from services.delivery_task_service import DeliveryTaskService

delivery_task_router = APIRouter()

delivery_task_service = DeliveryTaskService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@delivery_task_router.post("/create")
async def create_user(delivery_task: DeliveryTaskDTO):
    return await delivery_task_service.create_delivery_task(delivery_task)


@delivery_task_router.get("/getUserTasks/{user_id}", response_model=List[DeliveryTaskResponseDto])
async def get_user_tasks(user_id: int):
    return await delivery_task_service.get_user_tasks(user_id)


@delivery_task_router.get("/getUserActiveTask/{user_id}", response_model=DeliveryTaskResponseDto | None)
async def get_users_active_task(user_id: int):
    result = await delivery_task_service.get_users_active_task(user_id)
    return result


@delivery_task_router.get("/finish/{delivery_task_id}")
async def finish_delivery_task(delivery_task_id: int):
    return await delivery_task_service.finish_delivery_task_by_id(delivery_task_id)


@delivery_task_router.post("/change-status")
async def change_status(delivery_task_change_status: DeliveryTaskChangeStatusDTO):
    return await delivery_task_service.change_status(delivery_task_change_status.delivery_task_id,
                                                     delivery_task_change_status.new_status_id)


@delivery_task_router.get("/active", response_model=List[DeliveryTaskResponseDto])
async def get_active_tasks():
    return await delivery_task_service.get_active_tasks()


@delivery_task_router.get("/resolved", response_model=List[DeliveryTaskResponseDto])
async def get_resolved_tasks():
    return await delivery_task_service.get_resolved_tasks()
