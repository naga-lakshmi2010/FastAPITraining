#this file defines all configuration values the app needs
#DB conneection info,app name etc
#pydantic-settings: automatically reads environment variablees & validates their types
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "it_servicedesk"
    #gives the app name
    APP_NAME: str = "IT Service Desk APP API"
    # informs pydantic settings to load values from .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
#shared settings object that all other files can import
settings = Settings()