from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from data.model.deliverytaskstatus import DeliveryTaskStatus


class DeliveryTask(SQLModel, table=True):
    __tablename__ = "deliverytask"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=True)
    date: datetime = Field(default=None, nullable=False)
    user: Optional["User"] = Relationship(
        back_populates="delivery_tasks",
    )
    status_id: int = Field(foreign_key="deliverytaskstatus.id")
    status: Optional[DeliveryTaskStatus] = Relationship(
        back_populates="delivery_tasks"
    )
    orders: List["Order"] = Relationship(
        back_populates="delivery_task"
    )
    delivery_way_len: float = Field(default=0)
