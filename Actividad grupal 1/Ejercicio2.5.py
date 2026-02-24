#Ejercicio 2.5

from enum import Enum
class Tipo_de_cuenta:
    Ahorros = "Ahorros"
    Corriente = "Corriente"

class Cuenta:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo, saldo, tasa_interes):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo = tipo
        self.saldo = saldo
        self.tasa_interes = tasa_interes/100
    
    def mostrar_datos_cuenta(self):
        print("Nombres del titular de la cuenta: ", self.nombres)
        print("Apellidos del titular de la cuenta: ", self.apellidos)
        print("Tipo de cuenta: ", self.tipo)

    def mostrar_saldo_cuenta(self):
        print("Saldo de la cuenta: $", self.saldo)
    
    def consignar(self, consignacion):
        self.saldo = self.saldo + consignacion
        print("El saldo actualizado de la cuenta es: $", self.saldo)
    
    def retirar(self, retiro):
        if retiro > self.saldo:
            print("El monto excede el saldo total de la cuenta, no se puede realizar el retiro")
        else: 
            self.saldo = self.saldo - retiro
            print("Haz retirado: $", retiro)
            print("El saldo actualizado de la cuenta es: $", self.saldo)
    
    def aplicar_interes(self):
        self.saldo = self.saldo + self.saldo*self.tasa_interes
        print("El saldo actualizado (con intereses) de la cuenta es: $", self.saldo)


nombres = input("Ingrese los nombres de la persona: ")      
apellidos = input("Ingrese los apellidos de la persona: ")  

nuevaCuenta = Cuenta(nombres, apellidos, 123456789, Tipo_de_cuenta.Ahorros,0,5)

nuevaCuenta.mostrar_datos_cuenta
nuevaCuenta.consignar(20000)
nuevaCuenta.consignar(30000)
nuevaCuenta.retirar(40000)
nuevaCuenta.aplicar_interes()



