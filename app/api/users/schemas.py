from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[HttpUrl] = None


class User(UserBase):
    id: int

    class Config:
        from_attributes = True