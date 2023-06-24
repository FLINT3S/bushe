from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    login: str = Field(default=None, nullable=False, unique=True)
    password: str = Field(default=None, nullable=False)
    name: str = Field(default=None, nullable=False)
    surname: str = Field(default=None, nullable=False)
    delivery_tasks: List["User"] = Relationship(back_populates="user")

