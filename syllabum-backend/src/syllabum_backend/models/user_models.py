from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone


class User(SQLModel, table=True):
    id: Optional[int] = None
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    pwd: str
    is_email_verified: bool = Field(default=False)
    refresh_token: Optional[str] = Field(default=None)
    forgot_password_token: Optional[str] = Field(default=None)
    forgot_password_token_expiry: Optional[datetime] = Field(default=None)
    email_verification_token: Optional[str] = Field(default=None)
    email_verification_token_expiry: Optional[datetime] = Field(default=None)
