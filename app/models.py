from typing import Optional
from sqlmodel import Field, SQLModel

# 1. Base model containing shared attributes for users
class UserBase(SQLModel):
    name: str
    email: str = Field(index=True, unique=True)

# 2. Schema for creating a user (API input validation)
class UserCreate(UserBase):
    pass

# 3. Database Table Model representing the actual table in SQLite
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
