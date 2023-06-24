from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    login: str
    password: str
    name: str
    surname: str
