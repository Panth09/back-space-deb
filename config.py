# app/config.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB: str = "spacewatch"

    CORS_ORIGINS: str = ""
    MODEL_WEIGHTS_PATH: str = "dipak_model.pt"

    class Config:
        env_file = ".env"

settings = Settings()

def cors_origins() -> List[str]:
    if not settings.CORS_ORIGINS:
        return ["*"]
    return [o.strip() for o in settings.CORS_ORIGINS.split(",")]
