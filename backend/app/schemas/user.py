# apps/backend/src/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    full_name: Optional[str] = None
    password: str = Field(
        ...,
        min_length=8,
        description="Password must be at least 8 characters"
    )

class UserResponse(UserBase):
    id: int
    full_name: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AccessCodeVerification(BaseModel):
    access_code: str
