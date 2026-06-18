class LeerArchivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        with open(self.nombre, "r", encoding="utf-8") as arch:
            for linea in arch:
                print(linea, end="")

    def leer_mayusculas(self):
        with open(self.nombre, "r", encoding="utf-8") as arch:
            for linea in arch:
                print(linea.upper(), end="")


try:
    nom = input("Ingrese el nombre o la ruta del archivo: ")

    arch = LeerArchivo(nom)

    print("\n--- Contenido original del archivo ---")
    arch.leer()

    print("\n\n--- Contenido convertido a mayúsculas ---")
    arch.leer_mayusculas()

except FileNotFoundError:
    print("No se pudo leer el archivo. El archivo no existe.")

except PermissionError:
    print("No tiene permisos para leer el archivo.")

except Exception as error:
    print("Error:", error)