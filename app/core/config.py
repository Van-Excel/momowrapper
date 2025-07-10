from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str

    class Config:
        env_file = ".env"   # Optional: this helps for local scripts outside Docker too

settings = Settings()
