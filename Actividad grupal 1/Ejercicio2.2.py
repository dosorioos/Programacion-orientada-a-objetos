#Ejercicio 2.3

from enum import Enum

class Tipo_de_planeta(Enum):
    Gasesoso = "GASEOSO"
    Terrestre = "TERRESTRE"
    Enano = "ENANO"

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_media_sol, tipo, observabilidad):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_media_sol = distancia_media_sol
        self.tipo = tipo
        self.observabilidad = observabilidad
    
    def mostrar_datos_planeta(self):
        print("Nombre del planeta: ", self.nombre)
        print("Cantidad de satélites: ", self.cantidad_satelites)
        print("Masa del planeta: ", self.masa)
        print("Volumen del planeta: ", self.volumen)
        print("Diámetro del planeta: ", self.diametro)
        print("Distancia al sol: ", self.distancia_media_sol)
        print("Tipo de planeta: ", self.tipo.name)
        print("¿Es observable?: ", self.observabilidad)

    def densidad_planeta(self):
        if self.volumen == 0:
            return 0
        else:
            return self.masa/self.volumen
     
    def planeta_exterior(self):
        UA = 149597870
        if self.distancia_media_sol > 3.4*UA:
            return True
        else:
            return False
        

nombre_p1 = input("ingrese el nombre del planeta 1: ")
cantidad_satelites_p1 = int(input("ingrese la cantidad de satelites del planeta 1: "))
masa_p1 = float(input("ingrese la masa (en kg) del planeta 1: "))
volumen_p1 = float(input("ingrese el volumen (en km^3) del planeta 1: "))
diametro_p1 = int(input("ingrese el diametro (en km) del planeta 1: "))
distancia_media_sol_p1 = int(input("ingrese la distancia media al sol (en km) del planeta 1: "))

nombre_p2 = input("ingrese el nombre del planeta 2: ")
cantidad_satelites_p2 = int(input("ingrese la cantidad de satelites del planeta 2: "))
masa_p2 = float(input("ingrese la masa (en kg) del planeta 2: "))
volumen_p2 = float(input("ingrese el volumen (en km^3) del planeta 2: "))
diametro_p2 = int(input("ingrese el diametro (en km) del planeta 2: "))
distancia_media_sol_p2 = int(input("ingrese la distancia media al sol (en km) del planeta 2: "))

Planeta1 = Planeta(nombre_p1,cantidad_satelites_p1,masa_p1,volumen_p1,diametro_p1,distancia_media_sol_p1,Tipo_de_planeta.Terrestre,True)
Planeta2 = Planeta(nombre_p2,cantidad_satelites_p2,masa_p2,volumen_p2,diametro_p2,distancia_media_sol_p2,Tipo_de_planeta.Enano,False)

print("Datos planeta 1:")
Planeta1.mostrar_datos_planeta()
print("Densidad del planeta 1: ", Planeta1.densidad_planeta())
print("¿El planeta es exterior?: ", Planeta1.planeta_exterior())
print()
print("Datos planeta 2:")
Planeta2.mostrar_datos_planeta()
print("Densidad del planeta 2: ", Planeta2.densidad_planeta())
print("¿El planeta es exterior?: ", Planeta2.planeta_exterior())
print()

