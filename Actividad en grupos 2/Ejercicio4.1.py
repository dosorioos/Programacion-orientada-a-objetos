import tkinter as tk
from tkinter import scrolledtext


class PruebaExcepciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de Excepciones")
        self.ventana.geometry("600x650")

        titulo = tk.Label(
            ventana,
            text="Manejo de Excepciones",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        #First Try
        tk.Label(ventana, text="Numerador").pack()
        self.numerador = tk.Entry(ventana)
        self.numerador.pack()

        tk.Label(ventana, text="Denominador").pack()
        self.denominador = tk.Entry(ventana)
        self.denominador.pack()

        boton_first_try = tk.Button(
            ventana,
            text="Ejecutar primer Try - División por cero",
            command=self.first_try
        )
        boton_first_try.pack(pady=5)

        #Second Try
        tk.Label(ventana, text="Objeto").pack()
        self.objeto = tk.Entry(ventana)
        self.objeto.pack()

        boton_second_try = tk.Button(
            ventana,
            text="Ejecutar segundo Try - Objeto nulo",
            command=self.second_try
        )
        boton_second_try.pack(pady=5)

        #Third Try
        tk.Label(ventana, text="Texto para prueba fuera de rango").pack()
        self.texto_rango = tk.Entry(ventana)
        self.texto_rango.pack()

        boton_third_try = tk.Button(
            ventana,
            text="Ejecutar tercer Try - Fuera de rango",
            command=self.off_range
        )
        boton_third_try.pack(pady=5)

        #Fourth Try
        tk.Label(ventana, text="Número").pack()
        self.numero_texto = tk.Entry(ventana)
        self.numero_texto.pack()

        boton_fourth_try = tk.Button(
            ventana,
            text="Ejecutar cuarto Try - Formato incorrecto",
            command=self.wrong_format
        )
        boton_fourth_try.pack(pady=5)

        self.area_texto = scrolledtext.ScrolledText(
            ventana,
            width=70,
            height=15
        )
        self.area_texto.pack(padx=10, pady=10)

    def escribir(self, mensaje):
        self.area_texto.insert(tk.END, mensaje + "\n")
        self.area_texto.see(tk.END)

    def first_try(self):
        try:
            self.escribir(
                "Ingresando al primer try - Error de división por cero"
            )

            numerador = float(self.numerador.get())
            denominador = float(self.denominador.get())

            resultado = numerador / denominador #Si denominador es 0 genera el error

            self.escribir(f"Resultado de la división: {resultado}")

        except ZeroDivisionError:
            self.escribir("División por cero")

        except ValueError:
            self.escribir("Debe ingresar números válidos")

        finally:
            self.escribir("Ingresando al primer finally")

    def second_try(self):
        try:
            self.escribir(
                "Ingresando al segundo try - Error de objeto nulo"
            )

            objeto = self.objeto.get()

            if objeto == "":
                objeto = None

            nombre = objeto.upper()

            self.escribir(f"Nombre del objeto: {nombre}")

        except AttributeError:
            self.escribir("Objeto nulo")

        except Exception:
            self.escribir("Ocurrió una excepción")

        finally:
            self.escribir("Ingresando al segundo finally")

    def off_range(self):
        try:
            self.escribir(
                "Ingresando al tercer try - Error fuera de límite"
            )

            texto = self.texto_rango.get()

            caracter = texto[14]

            self.escribir(f"Carácter encontrado: {caracter}")

        except IndexError:
            self.escribir("Índice del string fuera de rango")

        finally:
            self.escribir("Ingresando al tercer finally")

    def wrong_format(self):
        try:
            self.escribir(
                "Ingresando al cuarto try - Error de formato"
            )

            numero = int(self.numero_texto.get())

            self.escribir(f"Número ingresado: {numero}")

        except ValueError:
            self.escribir("Formato incorrecto")

        finally:
            self.escribir("Ingresando al cuarto finally")


ventana = tk.Tk()
PruebaExcepciones(ventana)
ventana.mainloop()