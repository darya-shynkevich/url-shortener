import ssl
from urllib.parse import urlparse

import redis.asyncio as redis

from config import config


class RedisClient:
    def __init__(self, ttl: int = 3600):
        parsed_url = urlparse(config.redis_url)

        ssl_context = None
        if parsed_url.scheme == "rediss":
            ssl_context = ssl.create_default_context()

        self.redis = redis.Redis(
            host=parsed_url.hostname,
            port=parsed_url.port,
            password=parsed_url.password,
            ssl=bool(ssl_context),
            ssl_context=ssl_context,
            decode_responses=True,
        )

        self.ttl = ttl

    async def set(self, key: str, value: str):
        await self.redis.set(key, value, ex=self.ttl)

    async def get(self, key: str) -> str | None:
        value = await self.redis.get(key)
        return value if value else None
