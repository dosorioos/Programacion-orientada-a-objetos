#Ejercicio 2.1

class Persona: 
    def __init__(self, nombre, apellido, id, año_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.año_de_nacimiento = año_de_nacimiento

    def ver_datos_persona(self):
        print("Datos de la persona: ")
        print(self.nombre, self.apellido)
        print(self.id)
        print(self.año_de_nacimiento)
        print()

nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
id = input("Ingrese el documento de identidad de la persona: ")
año_de_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))

nueva_persona = Persona(nombre, apellido, id, año_de_nacimiento)
nueva_persona.ver_datos_persona()

        