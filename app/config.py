from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MedTeleSystem"
    DATABASE_URL: str
    RABBITMQ_URL: str
    OPENAI_API_KEY: str
    TELEGRAM_BOT_TOKEN: str
    
    class Config:
        env_file = ".env"

settings = Settings()