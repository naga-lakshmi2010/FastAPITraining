# This file is the "entry point" to the application

from fastapi import FastAPI

from app.config import settings
from app.database import ping_database

# Creating a fastAPI instance
app = FastAPI(title=settings.APP_NAME)

# This function runs once when the server starts. It checks the DB connection
@app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RunTimeError("Could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App:{settings.APP_NAME}")

# Checks basic health check API end point and confirms GET / is running and reachable. (/ is configured as 'root')
@app.get("/",tags=["Health"])
def health_check():
    return{"status":"ok","app":settings.APP_NAME}    