from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True

class CreateUser(UserBase):
    # Exclude fields to validate only the fields needed for creation
    id: int = Field(default=None, exclude=True)
    created_at: datetime = Field(default_factory=datetime.now, exclude=True)
    class Config:
        from_attributes = True

class ResponseUser(UserBase):
    class Config:
        from_attributes = True