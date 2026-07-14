class Profesor:
    def imprimir(self):
        print("Es un profesor")

class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular")

class Prueba:
    def __init__(self):
        profesor1 = ProfesorTitular()
        profesor1.imprimir()

Prueba() 