from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    profile_picture: str

class UserCreate(UserBase):
    """Schema used when creating a new user"""


class UserOut(UserBase):
    """Schema used when returning user data"""

    id: int
    created_at: datetime

    # Pydantic v2: enable ORM mode
    model_config = ConfigDict(from_attributes=True)
