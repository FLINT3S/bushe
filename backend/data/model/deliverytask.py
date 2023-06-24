from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class DeliveryTask(SQLModel, table=True):
    __tablename__ = "deliverytask"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(
        back_populates="users"
    )
    status_id: int = Field(foreign_key="deliverytaskstatus.id")
    status: Optional["TaskStatus"] = Relationship(
        back_populates="delivery_tasks"
    )
    orders: List["Order"] = Relationship(
        back_populates="delivery_task"
    )