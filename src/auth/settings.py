from functools import lru_cache
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseModel):
    DATABASE_USER:str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_DB: str = ""
    DATABASE_HOST: str = ""
    DATABASE_PORT: str = ""

class TokenSettings(BaseModel):
    SECRET_KEY: str = ""
    ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

class Settings(BaseSettings):
    database_settings: DatabaseSettings = DatabaseSettings()
    token_settings: TokenSettings = TokenSettings()

    model_config = SettingsConfigDict(env_file=".env")
    
@lru_cache
def get_database_settings():
    return Settings().database_settings

@lru_cache
def get_token_settings():
    return Settings().token_settings

