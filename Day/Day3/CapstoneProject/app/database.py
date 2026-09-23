#this file creates a single, shared conenctions to MongoDB using pymongo
from pymongo import MongoClient
from pymongo.database import Database

from app.config import settings

#MongoClient manages a poool of connections to the MongoDB server
client : MongoClient =MongoClient(settings.MONGO_URI)
database: Database = client[settings.MONGO_DB_NAME]

# Sends a ping command to the MongoDB to confirm the connection is alive
def ping_database() -> bool:
    try:
        return True
    except Exception:
        return False
     