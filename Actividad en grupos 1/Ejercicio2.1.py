#Ejercicio 2.1 POO
#Daniel Osorio - Isabella Caro - Laura Gomez

class Persona: 
    def __init__(self, nombre, apellido, id, año_de_nacimiento, pais_nacimiento, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.año_de_nacimiento = año_de_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero 

    def ver_datos_persona(self):
        print("Datos de la persona: ")
        print(self.nombre, self.apellido)
        print(self.id)
        print(self.año_de_nacimiento)
        print(self.año_de_nacimiento)
        print(self.año_de_nacimiento)
        print(self.pais_nacimiento)
        print(self.genero)
        print()

nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
id = input("Ingrese el documento de identidad de la persona: ")
año_de_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
pais_nacimiento =input("Ingrese el pais de nacimiento de la persona: ")
genero = input("Ingrese el genero de la persona: ")

nueva_persona = Persona(nombre, apellido, id, año_de_nacimiento, pais_nacimiento, genero)
nueva_persona.ver_datos_persona()

        