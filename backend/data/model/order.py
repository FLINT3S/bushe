from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from data.model.orderstatus import OrderStatus


class Order(SQLModel, table=True):
    __tablename__ = "order"

    id: Optional[int] = Field(default=None, primary_key=True)
    deadline: datetime = Field(default=None, nullable=False)
    address: str = Field(nullable=False)
    weight: int = Field(nullable=False)
    status_id: int = Field(foreign_key="orderstatus.id")
    status: Optional["OrderStatus"] = Relationship(
        back_populates="orders"
    )
    delivery_task_id: int = Field(foreign_key="deliverytask.id", nullable=True)
    delivery_task: Optional["DeliveryTask"] = Relationship(
        back_populates="orders"
    )