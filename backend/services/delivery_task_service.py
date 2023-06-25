from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from controllers.dto.delivery_task_dto import DeliveryTaskDTO
from data.databaseservice import DatabaseService
from data.model.deliverytask import DeliveryTask
from data.model.order import Order


class DeliveryTaskService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def create_delivery_task(self, deliveryTaskDTO: DeliveryTaskDTO):
        created_delivery_task = DeliveryTask(user_id=deliveryTaskDTO.user_id, status_id=1)
        await self.database_service.save(created_delivery_task)

        for order_id in deliveryTaskDTO.orders:
            order = await self.get_order_by_id(order_id)
            order.delivery_task_id = created_delivery_task.id
            await self.database_service.save(order)

        return created_delivery_task


    async def get_order_by_id(self, id: int):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(Order) \
                .where(Order.id == id) \
                .limit(1)
            result = (await session.execute(st)).first()

            if result:
                return result[0]