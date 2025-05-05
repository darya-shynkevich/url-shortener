from pydantic_settings import BaseSettings


class Config(BaseSettings):
    port: int = 8000

    redis_host: str = "localhost"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()
