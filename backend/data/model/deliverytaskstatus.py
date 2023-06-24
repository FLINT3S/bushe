from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class DeliveryTaskStatus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    delivery_tasks: List["DeliveryTask"] = Relationship(back_populates="status")

