from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, func
from datetime import datetime

from database import Base



class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str ] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    hashed_password:Mapped[str] = mapped_column(String(50))
    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
