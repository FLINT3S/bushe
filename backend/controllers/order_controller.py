import os
from typing import List

from fastapi import APIRouter

from controllers.dto.order_dto import OrderDTO
from controllers.dto.response.order_response_dto import OrderResponseDto
from data.databaseservice import DatabaseService
from services.order_service import OrderService

order_router = APIRouter()

order_service = OrderService(database_service=DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}"
))


@order_router.post("/create")
async def create_user(order: OrderDTO):
    return await order_service.create_order(order)


@order_router.get("/completeOrder/{order_id}", response_model=OrderResponseDto)
async def complete_order(order_id: int):
    return await order_service.complete_order(order_id)


@order_router.get("/getAll", response_model=List[OrderResponseDto])
async def get_all_orders():
    return await order_service.get_all_orders()
