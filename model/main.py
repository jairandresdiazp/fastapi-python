# importar la clase persona y crear una nueva persona #
from api.person import Person
# crear una nueva persona
persona = Person(0,"Juan", 20, "M", 70, 1.75)
# mostrar los datos de la persona
persona.toString()
# calcular el IMC de la persona
print("IMC: "+str(persona.calcularIMC()))
print()

print("lista de personas")

listaPersonas = [Person(0, "Juan", 20, "M", 70, 1.75), Person(1, "Maria", 25, "F", 60, 1.60), Person(2, "Pedro", 30, "M", 80, 1.80)]

for i,persona in enumerate(listaPersonas):
  print("Persona "+str(i))
  print("IMC: "+str(persona.calcularIMC()))
  print("Es mayor de edad: "+str(persona.esMayorDeEdad()))
  print("Comprobar sexo: "+str(persona.comprobarSexo("M")))
  print("Comprobar sexo: "+str(persona.comprobarSexo("F")))
  print()