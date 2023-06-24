from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from data.orderstatus import OrderStatus


class Order(SQLModel, table=True):
    __tablename__ = "order"

    id: Optional[int] = Field(default=None, primary_key=True)
    status_id: int = Field(foreign_key="orderstatus.id")
    status: Optional["OrderStatus"] = Relationship(
        back_populates="orders"
    )