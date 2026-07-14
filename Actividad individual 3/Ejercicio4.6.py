class Profesor:
    def imprimir(self):
        print("Es un profesor")

class ProfesorTitular(Profesor):
    
    def __init__(self,años=0):
        self.años = años

    def imprimir(self):
        print("Es un profesor titular")
    
    def imprimir_años(self):
        print(f"Años: {self.años}")

class Prueba:
    def __init__(self):
        profesor1 = ProfesorTitular()
        profesor1.imprimir_años()

class Prueba1:
    def __init__(self):

        profesores = [] 
        profesor1 = Profesor()
        profesor2 = ProfesorTitular(10)
        profesores.append(profesor1)
        profesores.append(profesor2)

        for i in profesores:
            i.imprimir()

Prueba()
print("\n")
Prueba1()


