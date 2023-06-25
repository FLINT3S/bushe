from datetime import datetime

from pydantic import BaseModel


class OrderDTO(BaseModel):
    deadline: datetime
    address: str
    weight: int
