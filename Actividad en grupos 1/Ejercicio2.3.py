#Ejercicio 2.3 POO
#Daniel Osorio - Isabella Caro - Laura Gomez

from enum import Enum


valor_multa = 500000

class tipo_de_combustible:
    Gasolina = "Gasolina"
    Bioetanol = "Bioetanol"
    Diesel = "Diesel"
    Biodesel = "Biodiesel"
    Gas_natural = "Gas natural"


class tipo_automovil:
    Ciudad = "Carro de ciudad"
    Subcompacto = "Subcompacto"
    Compacto = "Compacto"
    Familiar = "Familiar"
    Ejecutivo = "Ejecutivo"
    Suv = "SUV"

class color_automovil:
    Blanco = "Blanco"
    Negro = "Negro"
    Rojo = "Rojo"
    Naranja = "Naranja"
    Amarillo = "Amarillo"
    Verde = "Verde"
    Azul = "Azul"
    Violeta = "Violeta" 

class automoviles:
    def __init__(self, marca, modelo, motor, combustible, tipo, cantidad_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual, caja_automatica):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.cantidad_puertas = cantidad_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual
        self.caja_automatica = caja_automatica
        self.contador_multas = 0

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_motor(self):
        return self.motor   
    
    def get_combustible(self):
        return self.combustible
    
    def get_tipo(self):
        return self.tipo
    
    def get_cantidad_puertas(self):
        return self.cantidad_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos
    
    def get_velocidad_maxima(self):
        return self.velocidad_maxima
    
    def get_color(self):
        return self.color
    
    def get_velocidad_actual(self):
        return self.velocidad_actual
    
    def get_caja_automatica(self):
        return self.caja_automatica
    
    def set_marca(self, marca):
        self.marca = marca
        return self.marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo
        return self.modelo
    
    def set_motor(self, motor):
        self.motor = motor
        return self.motor   
    
    def set_combustible(self, combustible):
        self.combustible = combustible
        return self.combustible
    
    def set_tipo(self, tipo):
        self.tipo = tipo
        return self.tipo
    
    def set_cantidad_puertas(self, cantidad_puertas):
        self.cantidad_puertas = cantidad_puertas
        return self.cantidad_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos
        return self.cantidad_asientos
    
    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima
        return self.velocidad_maxima
    
    def set_color(self, color):
        self.color = color
        return self.color
    
    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual
        return self.velocidad_actual
    
    def set_caja_automatica(self, caja_automatica):
        self.caja_automatica = caja_automatica
        return self.caja_automatica
    
    def acelerar(self, aumento_velocidad):
        if self.velocidad_actual + aumento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_actual + aumento_velocidad
            print("Velocidad actual del automovil: ", self.velocidad_actual)
        else:
            print("No se puede superar la velocidad maxima del automovil")
            self.contador_multas =  self.contador_multas + 1
            
    def desacelerar(self, decremento_velocidad):
        if self.velocidad_actual - decremento_velocidad <0:
            print("No se puede desacelerar a una velocidad negativa")
        else:
            self.velocidad_actual = self.velocidad_actual - decremento_velocidad
            print("Velocidad actual del automovil: ", self.velocidad_actual)

    def frenar(self):
        self.velocidad_actual = 0
        print("Velocidad actual del automovil: ", self.velocidad_actual)
        
    def tiempo_de_llegada(self, distancia):
        if self.velocidad_actual != 0:
            tiempo_restante = distancia/self.velocidad_actual
            return tiempo_restante
        else:
            print("El auto esta detenido")

    def multas(self):
        if self.contador_multas == 0:
            print("El automovil esta libre de multas")
        else:
            print("El automovil tiene multas")
        
    def valor_multas(self):
        valor = self.contador_multas*valor_multa
        print("El valor total de las multas del automovil es:", valor)
    
    def mostrar_datos_automovil(self):
        print("Marca del automovil: ", self.marca)
        print("Modelo del automovil: ", self.modelo)
        print("Cilindraje en litros del motor del automovil: ", self.motor)
        print("Tipo de combustible del automovil: ", self.combustible)
        print("Tipo del automovil: ", self.tipo)
        print("Cantidad de puertas del automovil: ", self.cantidad_puertas)
        print("Cantidad de asientos del automovil: ", self.cantidad_asientos)
        print("Velocidad maxima del automovil: ", self.velocidad_maxima)
        print("Color del automovil: ", self.color)
        print("Velocidad actual del automovil: ", self.velocidad_actual)


marca = input("Ingrese la marca del automovil: ")
modelo = input("Ingrese el modelo del automovil: ")
motor = float(input("Ingrese el volumento (en Litros) del cilindraje del automovil: "))
cantidad_puertas = int(input("Ingrese la cantidad de puertas del automovil: "))
cantidad_asientos = int(input("Ingrese la cantidad de asientos del automovil: "))
velocidad_maxima = 150
velocidad_actual = 80

print()
Auto_nuevo = automoviles(marca, modelo, motor, tipo_de_combustible.Gasolina, tipo_automovil.Compacto, cantidad_puertas, cantidad_asientos, velocidad_maxima, color_automovil.Negro, velocidad_actual, False)
Auto_nuevo.mostrar_datos_automovil()
Auto_nuevo.set_velocidad_actual(100)
print("Velocidad actual del automovil: ", Auto_nuevo.velocidad_actual)
Auto_nuevo.acelerar(60)
Auto_nuevo.desacelerar(50)
Auto_nuevo.acelerar(120)
Auto_nuevo.multas()
Auto_nuevo.valor_multas()
print(Auto_nuevo.contador_multas)







  
