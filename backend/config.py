import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/vinobingo")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
DEBUG = bool(os.getenv("DEBUG", True))
