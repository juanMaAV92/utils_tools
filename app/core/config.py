import os
from dotenv import load_dotenv

if os.getenv('ENV', "prod") == "dev":
    load_dotenv()
    pass

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "util tools api")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.0.1")
    APP_RELOAD: bool = os.getenv("APP_RELOAD", True)
    APP_DOC_URL: str = os.getenv("APP_DOC_URL", "/docs")

    ENV: str = os.getenv("ENV", "prod") # dev, prod
    DEBUG: bool = os.getenv("DEBUG", True)

    SERVER_HOST: str = os.getenv("SERVER_HOST", "127.0.0.1")
    SERVER_PORT: int = os.getenv("SERVER_PORT", 8000)

settings = Settings()