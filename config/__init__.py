import os
from dotenv import load_dotenv

class Config:
  port: int = int(os.getenv("PORT", default=8000))
  logRotateCount: int = int(os.getenv("LOG_ROTATE_COUNT", default=7))
