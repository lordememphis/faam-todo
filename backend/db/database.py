from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient

from backend.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_DATABASE_URI)
database = client[settings.MONGO_DATABASE_NAME]


class Base:
    id: Any
