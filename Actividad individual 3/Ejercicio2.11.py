class ArticuloCientifico:
    def __init__(self, nombre_articulo, nombre_autor, palabras_clave=None, nombre_publicacion=None, año_publicacion=None, resumen=None):
        self.nombre_articulo = nombre_articulo
        self.nombre_autor = nombre_autor
        self.palabras_clave = palabras_clave if palabras_clave is not None else []
        self.nombre_publicacion = nombre_publicacion
        self.año_publicacion = str(año_publicacion)
        self.resumen = resumen
    
    def imprimir_info(self):
        print(f"Nombre del artículo: {self.nombre_articulo}")
        print(f"Nombre del autor: {self.nombre_autor}")
        if self.palabras_clave is not None:
            print(f"Palabras clave: {', '.join(self.palabras_clave)}")
        if self.nombre_publicacion is not None:
            print(f"Nombre de la publicación: {self.nombre_publicacion}")
        if self.año_publicacion is not None:
            print(f"Año de publicación: {self.año_publicacion}")
        if self.resumen is not None:
            print(f"Resumen: {self.resumen}")

class Empleado:
    def __init__(self, identificador=None, nombre=None, apellidos=None, edad=0):
        self.identificador = identificador
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def imprimir_info(self):
        if self.identificador is not None:
            print(f"Identificador: {self.identificador}")
        if self.nombre is not None:
            print(f"Nombre: {self.nombre}")
        if self.apellidos is not None:
            print(f"Apellidos: {self.apellidos}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")

class Caja:
    def __init__(self, base=0, ancho=0, altura=0, longitud=0, tipo=None):
        self.base = base
        self.ancho = ancho
        self.altura = altura
        self.longitud = longitud
        self.tipo = tipo

    def imprimir_info(self):
        print(f"Base: {self.base}")
        print(f"Ancho: {self.ancho}")
        print(f"Altura: {self.altura}")
        if self.longitud is not None:
            print(f"Longitud: {self.longitud}")
        if self.tipo is not None:
            print(f"Tipo: {self.tipo}")

articulo1 = ArticuloCientifico(
    nombre_articulo="La teoria especial de la relatividad",
    nombre_autor="Albert Einstein",
    palabras_clave = ["Fisica","Espacio","Tiempo"],
    nombre_publicacion="Anuales de fisica",
    año_publicacion=1913,
    resumen="Las leyes de la física son las mismas en todos los sistemas de referencia inerciales.")
articulo1.imprimir_info()
print("\n")
Empleado1 = Empleado(100,"Nuevo Empleado","Nuevo Empleado",18)
Empleado1.imprimir_info()
print("\n")
Caja1 = Caja(10,20,30,40,"Caja de madera")
Caja1.imprimir_info()