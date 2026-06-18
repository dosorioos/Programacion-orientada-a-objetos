class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre, universidad, lenguaje):
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) == 3

    def anadir(self, prog):
        if self.esta_lleno():
            raise ValueError("El equipo está completo.")

        self.programadores.append(prog)
    
    def validar_campo(self, campo):
        if any(c.isdigit() for c in campo):
            raise ValueError("El nombre no puede tener dígitos.")

        if len(campo) > 20:
            raise ValueError("La longitud no debe ser superior a 20 caracteres.")


class Contrasena:
    def validar(self, clave):
        errores = []

        if len(clave) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if " " in clave:
            errores.append("La contraseña no puede tener espacios.")

        if not any(c.islower() for c in clave):
            errores.append("Debe tener una letra minúscula.")

        if not any(c.isupper() for c in clave):
            errores.append("Debe tener una letra mayúscula.")

        if not any(c.isdigit() for c in clave):
            errores.append("Debe tener un número.")

        if not any(not c.isalnum() for c in clave):
            errores.append("Debe tener un carácter especial.")

        return errores


try:
    nom_eq = input("Nombre del equipo: ")
    uni = input("Universidad: ")
    leng = input("Lenguaje de programación: ")

    equipo = EquipoMaratonProgramacion(nom_eq, uni, leng)

    print("\nDatos de los integrantes:")
    for i in range(3):
        nom = input(f"\nNombre integrante {i + 1}: ")
        equipo.validar_campo(nom)

        ape = input("Apellidos:")
        equipo.validar_campo(ape)

        prog = Programador(nom, ape)
        equipo.anadir(prog)

    c = Contrasena()
    clave = input("\nIngrese la contraseña: ")

    errores = c.validar(clave)

    if errores:
        print("\nLa contraseña tiene los siguientes errores:")
        for e in errores:
            print("-", e)
    else:
        conf = input("Confirme la contraseña: ")

        if clave != conf:
            raise ValueError("Las contraseñas no coinciden.")

        print("\nEquipo y contraseña registrados correctamente.")

except ValueError as error:
    print("Error:", error)