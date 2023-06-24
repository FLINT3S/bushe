from controllers.dto.order_dto import OrderDTO
from data.databaseservice import DatabaseService
from data.model.order import Order


class OrderService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    async def create_order(self, orderDTO: OrderDTO):
        created_order = Order(deadline=orderDTO.deadline, address=orderDTO.address, weight=orderDTO.weight,
                              status_id=0, delivery_task_id=None)

        return await self.database_service.save(created_order)
