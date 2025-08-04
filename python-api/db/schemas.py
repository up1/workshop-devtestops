from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class CreateUser(UserBase):
    class Config:
        orm_mode = True