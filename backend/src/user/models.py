from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Optional

from database import Base



class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str ] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    hashed_password:Mapped[str]
