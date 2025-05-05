from fastapi import FastAPI

from redis_client import RedisClient
from services import ShortenerService

app = FastAPI()

redis_client = RedisClient()

shortener_service = ShortenerService()

