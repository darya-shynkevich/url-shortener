from pydantic_settings import BaseSettings


class Config(BaseSettings):
    port: int = 8000

    redis_url: str = "redis://localhost:6379"

    prefix: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()
