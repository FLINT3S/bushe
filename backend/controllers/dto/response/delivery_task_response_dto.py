from datetime import datetime
from typing import List

from pydantic import BaseModel

from data.model.deliverytaskstatus import DeliveryTaskStatus
from data.model.order import Order
from data.model.user import User


class DeliveryTaskResponseDto(BaseModel):
    id: int
    date: datetime
    user: User
    status: DeliveryTaskStatus
    orders: List[Order]
