import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Raw database config
RAW_DB_CONFIG = {
    "host": os.getenv("DB_HOST_RAW"),
    "user": os.getenv("DB_USER_RAW"),
    "password": os.getenv("DB_PASSWORD_RAW"),
    "database": os.getenv("DB_DATABASE_RAW")
}

# Analytics database config
ANALYTICS_DB_CONFIG = {
    "host": os.getenv("DB_HOST_ANALYTICS"),
    "user": os.getenv("DB_USER_ANALYTICS"),
    "password": os.getenv("DB_PASSWORD_ANALYTICS"),
    "database": os.getenv("DB_DATABASE_ANALYTICS")
}