from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from data.databaseservice import DatabaseService
from data.model.orderstatus import OrderStatus

order_statuses = ["Создан", "Заказ назначен в задачу", "Заказ готовится", "Выдан курьеру", "Заказ доставлен"]


class OrderStatusService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def drop_and_init_default_data(self):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(OrderStatus)
            results = (await session.execute(st))
            for value in results:
                await session.delete(value[0])
                await session.commit()
            for index in range(len(order_statuses)):
                await self.database_service.save(OrderStatus(id=index, name=order_statuses[index]))
                await session.commit()


