# app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client: AsyncIOMotorClient | None = None

async def get_db():
    from app.db import client
    if client is None:
        raise RuntimeError("DB client not initialized")
    return client[settings.MONGODB_DB]

async def init_db():
    global client
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.MONGODB_DB]
    # indexes
    await db.detections.create_index("timestamp")
    await db.detections.create_index("satellite_id")
    await db.detections.create_index("risk_score")
