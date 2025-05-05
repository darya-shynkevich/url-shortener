import redis.asyncio as redis

from config import config


class RedisClient:

    def __init__(self, ttl: int = 3600):
        self.redis = redis.Redis(
            host=config.redis_host, port=6379, decode_responses=True
        )
        self.ttl = ttl

    async def set(self, key: str, value: str):
        await self.redis.set(key, value, ex=self.ttl)

    async def get(self, key: str) -> str | None:
        value = await self.redis.get(key)
        return value if value else None
