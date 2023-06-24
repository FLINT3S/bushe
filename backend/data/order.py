from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from data.orderstatus import OrderStatus


class Order(SQLModel, Table=True):
    __tablename__ = "order"

    id: Optional[int] = Field(default=None, primary_key=True)
    status: Optional["OrderStatus"] = Relationship(
        back_populates="order"
    )