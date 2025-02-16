import motor.motor_asyncio
from pydantic import BaseModel
from fastapi import Depends
import os

MONGO_URI = os.getenv("MONGODB_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db = client.get_database("ProjectXVietnam")
CVScoringCol = db.get_collection("CVScoringResult")
CVWrongFormat = db.get_collection("CVWrongFormat")

class MongoModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True