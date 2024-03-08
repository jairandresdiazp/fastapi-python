import os
import logging
import config
from logging.handlers import TimedRotatingFileHandler

logDirectory = "logs"

# Crear el directorio si no existe
os.makedirs(logDirectory, exist_ok=True)

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)

fileHandler = TimedRotatingFileHandler(
    filename=os.path.join(logDirectory, "app.log"),
    when="midnight",
    interval=1,
    backupCount=config.logRotateCount,
    encoding="utf-8"
)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)