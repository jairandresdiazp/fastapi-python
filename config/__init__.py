import os
from dotenv import load_dotenv

load_dotenv()

logRotateCount: int = int(os.getenv("LOG_ROTATE_COUNT", default=7))
dataBase: str = os.getenv("DATABASE_URL", default="mysql+mysqlconnector://root:root@localhost/fastapi")
