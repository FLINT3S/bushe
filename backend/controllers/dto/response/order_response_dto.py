from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from data.model.deliverytask import DeliveryTask
from data.model.orderstatus import OrderStatus


class OrderResponseDto(BaseModel):
    id: int
    deadline: datetime
    address: str
    weight: int
    status: OrderStatus
    delivery_task: Optional[DeliveryTask]
