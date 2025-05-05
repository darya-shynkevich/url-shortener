from fastapi import FastAPI

from web.redis_client import RedisClient
from web.services import ShortenerService

app = FastAPI()

redis_client = RedisClient()

shortener_service = ShortenerService()

