import os

from fastapi import APIRouter

from controllers.dto.order_dto import OrderDTO
from data.databaseservice import DatabaseService
from services.order_service import OrderService

order_router = APIRouter()

order_service = OrderService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@order_router.post("/create")
async def create_user(order: OrderDTO):
    return await order_service.create_order(order)
