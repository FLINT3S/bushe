from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from data.databaseservice import DatabaseService
from data.model.deliverytaskstatus import DeliveryTaskStatus

delivery_task_statuses = ["Задача создана", "Назначено", "Готовится", "Ожидает выдачи", "В доставке", "Доставлен"]


class DeliveryTaskStatusService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def drop_and_init_default_data(self):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(DeliveryTaskStatus)
            results = (await session.execute(st))
            for value in results:
                await session.delete(value[0])
                await session.commit()
            for index in range(len(delivery_task_statuses)):
                await self.database_service.save(DeliveryTaskStatus(id=index, name=delivery_task_statuses[index]))
                await session.commit()


