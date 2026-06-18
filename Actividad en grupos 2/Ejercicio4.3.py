import math

class CalculosNumericos:

    def calcular_logaritmo_neperiano(self, valor):
        if valor <= 0:
            raise ValueError("El número debe ser positivo para calcular el logaritmo.")

        return math.log(valor)

    def calcular_raiz_cuadrada(self, valor):
        if valor < 0:
            raise ValueError("El número debe ser positivo para calcular la raíz cuadrada.")

        return math.sqrt(valor)

    def calcular_pendiente(self, x1, y1, x2, y2):
        if x1 == x2:
            raise ValueError("La pendiente es indefinida porque la recta es vertical." )

        return (y2 - y1) / (x2 - x1)

    def calcular_punto_medio(self, x1, y1, x2, y2):
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2
        return (xm, ym)

    def calcular_raices_cuadraticas(self, a, b, c):
        if a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero.")

        discriminante = b**2 - 4 * a * c

        if discriminante < 0:
            raise ValueError("La ecuación no tiene raíces reales.")

        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)

        return (x1, x2)

    def convertir_base(self, numero, base):
        if base < 2 or base > 36:
            raise ValueError("La base debe estar entre 2 y 36.")

        if numero == 0:
            return "0"

        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""

        while numero > 0:
            residuo = numero % base
            resultado = caracteres[residuo] + resultado
            numero //= base

        return resultado

try:
    calculos = CalculosNumericos()

    valor = float(input("Ingrese un número para calcular su logaritmo neperiano y su raiz cuadrada: "))
    x1 = float(input("Para calcular la pendiente y el punto medio: \nIngrese x1: "))
    y1 = float(input("Ingrese y1: "))
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))
    punto = calculos.calcular_punto_medio(x1, y1, x2, y2)

    a = float(input("Para calcular las raices de una ecuación cuadrática: \nIngrese a: "))
    b = float(input("Ingrese b: "))
    c = float(input("Ingrese c: "))
    raices = calculos.calcular_raices_cuadraticas(a, b, c)
    numero = int(input("Ingrese un número en base 10: "))
    base = int(input("Ingrese la base destino: "))

    print("Logaritmo:", calculos.calcular_logaritmo_neperiano(valor))
    print("Raíz cuadrada:", calculos.calcular_raiz_cuadrada(valor))
    print("Pendiente:",calculos.calcular_pendiente(x1, y1, x2, y2))
    print("Punto medio:", punto)
    print("Raíces:", raices)
    print(f"El número en base {base} es:",calculos.convertir_base(numero, base))

except ValueError as error:
    print("Error:", error)