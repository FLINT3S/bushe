from sqlalchemy.orm import joinedload, selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from controllers.dto.order_dto import OrderDTO
from data.databaseservice import DatabaseService
from data.model.order import Order


class OrderService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def create_order(self, order_dto: OrderDTO):
        created_order = Order(deadline=order_dto.deadline, address=order_dto.address, weight=order_dto.weight,
                              status_id=0, delivery_task_id=None)

        return await self.database_service.save(created_order)

    async def complete_order(self, order_id: int):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(Order) \
                .where(Order.id == order_id) \
                .options(joinedload(Order.status), joinedload(Order.delivery_task))

            order = (await session.execute(st)).first()[0]
            order.status_id = 4

            await session.commit()
            await session.refresh(order)

            return order

    async def get_all_orders(self):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(Order) \
                .where(Order.status_id == 0) \
                .options(
                selectinload(Order.status),
                selectinload(Order.delivery_task),
            )

            result = await session.execute(st)
            tasks = result.scalars().all()
            return tasks
