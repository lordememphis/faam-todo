from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    APPLICATION_NAME: str = "TODO APP"

    DEBUG_MODE: bool = False

    HOST: str = "0.0.0.0"
    PORT: int = 8001

    MONGO_DATABASE_URI: str
    MONGO_DATABASE_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
