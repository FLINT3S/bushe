from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from data.databaseservice import DatabaseService
from data.model.price import Price


class PriceService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def get_cost(self):
        async with AsyncSession(self.database_service.engine) as session:
            st = select(Price)
            result = (await session.execute(st)).first()

            return result[0]
