import tkinter
import numpy as np
from tkinter import messagebox



class Notas:

    def __init__(self):

        self.ventana = tkinter.Tk()  #Se crea la ventana
        self.ventana.title("Notas Estudiante")

        self.frame = tkinter.Frame(self.ventana)
        self.frame.grid(row=0, column=0, padx=20, pady=20)
        self.frame.columnconfigure(0, minsize=200)
        self.frame.columnconfigure(1, minsize=150)

        self.respuestas = []

        for i in range(5):

            label = tkinter.Label(self.frame, text=f"Nota {i+1}:")
            label.grid(row=i, column=0)

            entry = tkinter.Entry(self.frame, width=12,justify="center")
            entry.grid(row=i, column=1)

    

            self.respuestas.append(entry)

        calculos = tkinter.Button(self.frame, text="Calcular", command=self.calculos,width=15)
        calculos.grid(row=5, column=0)

        limpiar = tkinter.Button(self.frame, text="Limpiar", command=self.limpiar,width=15)
        limpiar.grid(row=5, column=1)

        self.promedio_label = tkinter.Label(self.frame, text="Promedio de las notas:")
        self.promedio_label.grid(row=6, column=0)

        self.desviacion_label = tkinter.Label(self.frame, text="Desviación estandar de las notas:")
        self.desviacion_label.grid(row=7, column=0)

        self.notaMayor_label = tkinter.Label(self.frame, text="Nota mayor:")
        self.notaMayor_label.grid(row=8, column=0)

        self.notaMenor_label = tkinter.Label(self.frame, text="Nota menor:")
        self.notaMenor_label.grid(row=9, column=0)

        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=3, pady=5)

        self.ventana.mainloop()

    def calculos(self):

        notas = []

        for dato in self.respuestas:

            nota = dato.get()

            if nota == "":
                messagebox.showwarning("Campo vacío", "Debe ingresar las 5 notas")
                return

            try:
                notas.append(float(nota))

            except ValueError:
                messagebox.showwarning("Error", "Solo se pueden ingresar números")
                return

        promedio = np.average(notas)
        desviacion_estandar = np.std(notas)
        notaMayor = np.max(notas)
        notaMenor = np.min(notas)

        self.promedio_label.config(text=f"Promedio de las notas: {promedio:.2f}")

        self.desviacion_label.config(
            text=f"Desviación estandar de las notas: {desviacion_estandar:.2f}"
        )

        self.notaMayor_label.config(text=f"Nota mayor: {notaMayor}")

        self.notaMenor_label.config(text=f"Nota menor: {notaMenor}")

    def limpiar(self):

        for entry in self.respuestas:
            entry.delete(0, tkinter.END)

        self.promedio_label.config(text="Promedio de las notas:", width=30, anchor="w")
        self.desviacion_label.config(text="Desviación estandar de las notas:",width=30, anchor="w")
        self.notaMayor_label.config(text="Nota mayor:",width=30, anchor="w")
        self.notaMenor_label.config(text="Nota menor:",width=30, anchor="w")

Notas()

