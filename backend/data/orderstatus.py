from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class OrderStatus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    orders: List["Order"] = Relationship(back_populates="status")

