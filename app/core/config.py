from app.core.creds import DATABASE_URL

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

settings = Settings(database_url=DATABASE_URL)