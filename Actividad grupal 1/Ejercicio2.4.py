#Ejercicio 2.4
#Daniel Osorio - Isabella Caro - Laura Gomez

import numpy as np

class circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = np.pi*(self.radio**2)
        return area
    
    def perimetro(self):
        perimetro =2*np.pi*self.radio
        return perimetro

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.base*self.altura
        return area
    
    def perimetro(self):
        perimetro = 2*(self.base + self.altura)
        return perimetro
    
    def hipotenusa(self):
        hipotenusa = np.sqrt((self.base)**2+(self.altura)**2)
        return hipotenusa

class cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        area = self.lado**2
        return area
    
    def perimetro(self):
        perimetro = 4*self.lado
        return perimetro

class triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area = (self.base*self.altura)/2
        return area
    
    def hipotenusa(self):
        hipotenusa = np.sqrt((self.base)**2+(self.altura)**2)
        return hipotenusa

    def perimetro(self):
        perimetro = self.base + self.altura + self.hipotenusa() 
        return perimetro
    
    def tipo(self):
        a = self.altura
        b = self.base
        c = self.hipotenusa()

        if a == b and a == c and b==c:
            print("Triangulo Equilatero")
        elif a != b and a != c and b !=c:
            print("Triangulo Escaleno")
        else: 
            print("Triangulo Isoceles")

class rombo:
    def __init__(self, diagonal_menor, diagonal_mayor, lado):
        self.lado = lado
        self.diagonal_menor = diagonal_menor
        self.diagonal_mayor = diagonal_mayor
    
    def area(self):
        area = (self.diagonal_mayor*self.diagonal_menor)/2
        return area
    
    def perimetro(self):
        perimetro = 4*self.lado
        return perimetro

class trapecio:
    def __init__(self, base_menor, base_mayor, altura):
        self.altura = altura
        self.base_menor = base_menor
        self.base_mayor = base_mayor
    
    def area(self):
        area = ((self.base_mayor*self.base_menor)*self.altura)/2
        return area
    
    def lado(self):
        lado = np.sqrt((self.altura)**2 + ((self.base_mayor - self.base_menor)/2)**2)
        return lado
                        
    def perimetro(self):
        perimetro = 4*self.lado()
        return perimetro
    

#Creación de los objetos

radioCir = float(input("Ingrese el valor del radio del circulo: "))
baseRec = float(input("Ingrese el valor de la base del rectangulo: "))
altRec = float(input("Ingrese el valor de la altura del rectangulo: "))
ladoCuad = float(input("Ingrese el valor del lado del cuadrado: "))
baseTri = float(input("Ingrese el valor de la base del rectangulo: "))
altTri = float(input("Ingrese el valor de la altura del rectangulo: "))
diagmenorR = float(input("Ingrese el valor de la diagonal menor del rombo: "))
diagmayorR = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
ladoR = float(input("Ingrese el valor del lado del rombo: "))
basemenorTra = float(input("Ingrese el valor de la base menor del trapecio: "))
basemayorTra = float(input("Ingrese el valor de la base mayor del trapecio: "))
alturaTra = float(input("Ingrese el valor de altura del trapecio: "))



circulo1 = circulo(radioCir)
rectangulo1 = rectangulo(baseRec,altRec)
cuadrado1 = cuadrado(ladoCuad)
triangulo1 = triangulo(baseTri,altTri)
rombo1 = rombo(diagmenorR,diagmayorR,ladoR)
trapecio1  =trapecio(basemenorTra,basemayorTra,alturaTra)

#Resultados
print("Area del circulo: ", circulo1.area())
print("Perimetro del circulo: ", circulo1.perimetro())
print()
print("Area del rectangulo: ", rectangulo1.area())
print("Perimetro del rectangulo: ", rectangulo1.perimetro())
print("Hipotenusa del rectangulo: ", rectangulo1.hipotenusa())
print()
print("Area del cuadrado: ", cuadrado1.area())
print("Perimetro del cuadrado: ", cuadrado1.perimetro())
print()
print("Area del triangulo: ", triangulo1.area())
print("Perimetro del triangulo: ", triangulo1.perimetro())
print("Hipotenusa del triangulo: ", triangulo1.hipotenusa())
triangulo1.tipo()
print()
print("Area del rombo: ", rombo1.area())
print("Perimetro del rombo: ", rombo1.perimetro())
print()
print("Area del trapecio: ", trapecio1.area())
print("Perimetro del trapecio: ",trapecio1.perimetro())
print()
