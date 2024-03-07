import os
import logging

from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from model.person import Person
from model.response import Response
from config import Config
from typing import List
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
    backupCount=Config.logRotateCount,
    encoding="utf-8"
)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

app = FastAPI(root_path="/api", title="API de Personas", description="API para el manejo de personas", version="0.0.1")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.mount("/public", StaticFiles(directory="public"), name="public")


listaPersonas = [Person(id=0, nombre="Juan", edad=20, sexo="M", peso=70, altura=1.75), 
                 Person(id=1, nombre="Maria", edad=25, sexo="F", peso=60, altura=1.60), 
                 Person(id=2, nombre="Pedro", edad=30, sexo="M", peso=80, altura=1.80), 
                 Person(id=3, nombre="Ana", edad=35, sexo="F", peso=70, altura=1.70)]

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    file_name = "favicon.png"
    file_path = os.path.join(os.getcwd(), "public", file_name)
    return FileResponse(path=file_path, media_type="image/png")

@app.get("/", include_in_schema=False) 
def read_root():
  return {"v": "0.0.1"}

@app.get("/persona") 
def read_persona() -> Response[List[Person]]:
  logger.info("get /persona")
  return Response[List[Person]](data=listaPersonas, success=True, error=None)

@app.get("/persona/{id}")
def read_persona(id: int) -> Response[Person]:
  logger.info(f"get /persona/{id}")
  response = Response[Person](success=False)
  try:
    result = list(filter(lambda persona: persona.id == id, listaPersonas))
    if len(result) > 0:
      response.data = result[0]
      response.success = True
    else:
      response.error = ["Persona no encontrada"]
  except Exception as e:
    response.error = ["Error en la buqueda de la persona "+str(e)]
  finally:
    return response

@app.post("/persona")
def create_persona(persona: Person) -> Response[None]:
  logger.info(f"post /persona {persona}")
  listaPersonas.append(persona)
  return Response[None](data=None, success=True, error=None)

'''
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
'''
