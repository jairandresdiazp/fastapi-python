from fastapi import APIRouter
from model.api.person import Person
from model.api.response import Response
from typing import List
from config.logger import logger

router = APIRouter()

listaPersonas = [Person(id=0, nombre="Juan", edad=20, sexo="M", peso=70, altura=1.75), 
                 Person(id=1, nombre="Maria", edad=25, sexo="F", peso=60, altura=1.60), 
                 Person(id=2, nombre="Pedro", edad=30, sexo="M", peso=80, altura=1.80), 
                 Person(id=3, nombre="Ana", edad=35, sexo="F", peso=70, altura=1.70)]

@router.get("")
def read_persons() -> Response[List[Person]]:
  logger.info("get /persona")
  logger.info("get /persona")
  return Response[List[Person]](data=listaPersonas, success=True, error=None)

@router.get("/{id}")
def read_person(id: int) -> Response[Person]:
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

@router.post("")
def create_person(persona: Person) -> Response[None]:
  logger.info(f"post /persona {persona}")
  listaPersonas.append(persona)
  return Response[None](data=None, success=True, error=None)
