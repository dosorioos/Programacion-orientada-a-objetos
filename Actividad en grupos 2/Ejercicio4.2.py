class Vendedor:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido

        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif edad > 120:
            raise ValueError("La edad no puede ser mayor a 120.")

        self.edad = edad

    def imprimir(self):
        print("-- DATOS DEL VENDEDOR --")
        print("Nombre vendedor:\n", self.nombre)
        print("Apellidos vendedor:\n", self.apellido)
        print("Edad vendedor:\n", self.edad)

class Valor_ASCII:
    def get(self, simbolo):
        return ord(simbolo)

    def get_simbolo(self, numero):
        if 0 <= numero <= 31:
            return "Carácter de control (sin símbolo visible)"
        return chr(numero)


try:
    nom = input("Nombre del vendedor: ")
    apll = input("Apellidos del vendedor: ")
    edad = int(input("Edad del vendedor: "))

    vendedor = Vendedor(nom, apll, edad)

    ascii_tabla = Valor_ASCII()
    simbolo = ascii_tabla.get_simbolo(vendedor.edad)

    vendedor.imprimir()
    print(f"El código ASCII {vendedor.edad} corresponde al símbolo: \n{simbolo}")

except ValueError as error:
    print("Error:", error)