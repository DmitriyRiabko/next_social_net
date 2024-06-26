from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url:str = "postgresql+asyncpg://admin:admin@localhost/next_social_net_db"
    db_echo:bool = True
    
    
settings = Settings()