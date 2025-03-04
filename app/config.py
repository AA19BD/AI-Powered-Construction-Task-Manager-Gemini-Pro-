from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str

    model_config = {"extra": "ignore"}


settings = Settings()
