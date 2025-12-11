
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///./data.db")
