from sqlmodel import SQLModel
from typing import Optional

class UserForms(SQLModel):
    username: str
    email: str
    pwd: str


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserInfo(SQLModel):
    username: str
    email: str
    is_email_verified: bool