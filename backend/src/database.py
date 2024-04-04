from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from config import settings
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(
    settings.db_url,
    echo=settings.db_echo
)
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)




async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
        
class Base(DeclarativeBase):
    pass
