from uuid import UUID
import redis.asyncio as redis

from app.core import settings


class RedisService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.redis = redis.from_url(settings.REDIS_HOST)
            self.initialized = True

    async def set(self, key: str, value: str, expire: int = 1800):
        await self.redis.setex(key, expire, value)

    async def get(self, key: UUID):
        return await self.redis.get(str(key))

    async def delete(self, key: UUID):
        await self.redis.delete(str(key))


redis_service = RedisService()
