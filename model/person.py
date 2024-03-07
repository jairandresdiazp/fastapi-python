from pydantic import BaseModel

class Person(BaseModel):
  id: int
  nombre: str
  edad: int
  sexo: str
  peso: float
  altura: float
  def __init__(self,id, nombre, edad, sexo, peso, altura):
    super().__init__(id=id, nombre=nombre, edad=edad, sexo=sexo, peso=peso, altura=altura)
    self.id = id
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.peso = peso
    self.altura = altura
    
  def calcularIMC(self):
    imc = self.peso / (self.altura ** 2)
    if imc < 20:
      return -1
    elif imc >= 20 and imc <= 25:
      return 0
    else:
      return 1
      
  def esMayorDeEdad(self):
    if self.edad >= 18:
      return True
    else:
      return False
      
  def comprobarSexo(self, sexo):
    if sexo.lower() == self.sexo.lower():
      return True
    else:
      return False
      
  def toString(self):
    print("Id: "+str(self.id))
    print("Nombre: "+self.nombre)
    print("Edad: "+str(self.edad))
    print("Sexo: "+self.sexo)
    print("Peso: "+str(self.peso))
    print("Altura: "+str(self.altura))
    
    