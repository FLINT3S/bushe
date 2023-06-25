from datetime import datetime
from typing import List

from pydantic import BaseModel

class DeliveryTaskDTO(BaseModel):
    user_id: int
    orders: List[int]
