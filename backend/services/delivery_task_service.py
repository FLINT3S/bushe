import datetime

from sqlalchemy.orm import joinedload, selectinload
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

    async def get_user_tasks(self, user_id: int):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(DeliveryTask) \
                .where(DeliveryTask.user_id == user_id) \
                .where(DeliveryTask.date >= datetime.datetime.now().date()) \
                .options(
                selectinload(DeliveryTask.status),
                selectinload(DeliveryTask.orders),
                selectinload(DeliveryTask.user)
            )

            result = await session.execute(st)
            tasks = result.scalars().all()
            return tasks

    async def get_users_active_task(self, user_id: int) -> DeliveryTask:
        async with AsyncSession(self.database_service.engine) as session:
            st = select(DeliveryTask) \
                .where(DeliveryTask.user_id == user_id) \
                .where(DeliveryTask.status_id == 4) \
                .options(
                joinedload(DeliveryTask.status),
                joinedload(DeliveryTask.orders),
                joinedload(DeliveryTask.user)
            )

            result = (await session.execute(st)).first()
            if result:
                return result[0]

    async def get_delivery_task_by_id(self, id: int):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(DeliveryTask) \
                .where(DeliveryTask.id == id) \
                .limit(1) \
                .options(
                selectinload(DeliveryTask.status),
                selectinload(DeliveryTask.orders),
                selectinload(DeliveryTask.user)
            )

            result = (await session.execute(st)).first()

            if result:
                return result[0]


    async def finish_delivery_task_by_id(self, id: int):
        delivery_task = await self.get_delivery_task_by_id(id)
        print(delivery_task)
        orders = delivery_task.orders

        for order in orders:
            order.status_id = 4
            await self.database_service.save(order)
        delivery_task.status_id = 5
        await self.database_service.save(delivery_task)

        return delivery_task

