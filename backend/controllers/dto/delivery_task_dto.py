from datetime import datetime
from typing import List

from pydantic import BaseModel


class DeliveryTaskDTO(BaseModel):
    delivery_way_len: float
    user_id: int
    orders: List[int]
