from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    role: int = Field(default=0, nullable=False)  # 1 - курьер, 2 - манагер, 3 - мегачел
    login: str = Field(default=None, nullable=False, unique=True)
    password: str = Field(default=None, nullable=False)
    name: str = Field(default=None, nullable=False)
    surname: str = Field(default=None, nullable=False)
    delivery_tasks: List["DeliveryTask"] = Relationship(back_populates="user")
