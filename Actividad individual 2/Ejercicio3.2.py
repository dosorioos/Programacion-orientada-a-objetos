import tkinter
import numpy as np


class Figuras:

    def __init__(self, titulo, grafica):

        self.ventana = tkinter.Toplevel()
        self.ventana.title(titulo)

        self.frame = tkinter.Frame(self.ventana)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.frame_grafica = tkinter.Frame(self.ventana)
        self.frame_grafica.grid(row=1, column=0, padx=20, pady=20)

        self.imagen = tkinter.PhotoImage(file=grafica)
        self.imagen = self.imagen.subsample(2,2)

        self.label_grafica = tkinter.Label(self.frame_grafica, image=self.imagen)
        self.label_grafica.image = self.imagen
        self.label_grafica.grid(row=0, column=0)

        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=3, pady=5)

class Cilindro(Figuras):

    def __init__(self):

        super().__init__("Cilindro", "imagenesE3/cilindro.png")

        tkinter.Label(self.frame, text="Radio en centimentros:").grid(row=0, column=0)
        self.radio = tkinter.Entry(self.frame)
        self.radio.grid(row=0, column=1)

        tkinter.Label(self.frame, text="Altura en centimentros:").grid(row=1, column=0)
        self.altura = tkinter.Entry(self.frame)
        self.altura.grid(row=1, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=2, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen del cilindro:")
        self.volumen_label.grid(row=3, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie del cilindro:")
        self.superficie_label.grid(row=4, column=0)

    def valores(self):

        radio = float(self.radio.get())
        altura = float(self.altura.get())

        volumen = np.pi*(radio**2)*altura
        superficie = (2*np.pi*radio*altura) + (2*np.pi*(radio**2))

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm^3")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Esfera(Figuras):

    def __init__(self):

        super().__init__("Esfera", "imagenesE3/esfera.png")

        tkinter.Label(self.frame, text="Radio en centimentros:").grid(row=0, column=0)
        self.radio = tkinter.Entry(self.frame)
        self.radio.grid(row=0, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=1, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen de la esfera:")
        self.volumen_label.grid(row=2, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie de la esfera:")
        self.superficie_label.grid(row=3, column=0)

    def valores(self):

        radio = float(self.radio.get())

        volumen = (4/3)*np.pi*(radio**3)
        superficie = 4*np.pi*(radio**2)

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm^3")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Piramide(Figuras):

    def __init__(self):

        super().__init__("Pirámide", "imagenesE3/piramide.png")

        tkinter.Label(self.frame, text="Base en centimetros:").grid(row=0, column=0)
        self.base = tkinter.Entry(self.frame)
        self.base.grid(row=0, column=1)

        tkinter.Label(self.frame, text="Altura en centimetros:").grid(row=1, column=0)
        self.altura = tkinter.Entry(self.frame)
        self.altura.grid(row=1, column=1)

        tkinter.Label(self.frame, text="Apotema en centimetros:").grid(row=2, column=0)
        self.apotema = tkinter.Entry(self.frame)
        self.apotema.grid(row=2, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=3, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen de la piramide:")
        self.volumen_label.grid(row=4, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie de la piramide:")
        self.superficie_label.grid(row=5, column=0)

    def valores(self):

        base = float(self.base.get())
        altura = float(self.altura.get())
        apotema = float(self.apotema.get())

        volumen = ((base**2)*altura)/3
        superficie = (base**2) + (2*base*apotema)

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm^3")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Cubo(Figuras):

    def __init__(self):

        super().__init__("Cubo", "imagenesE3/cubo.png")

        tkinter.Label(self.frame, text="Lado en centimetros:").grid(row=0, column=0)
        self.lado = tkinter.Entry(self.frame)
        self.lado.grid(row=0, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=1, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen del cubo:")
        self.volumen_label.grid(row=2, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie del cubo:")
        self.superficie_label.grid(row=3, column=0)

    def valores(self):

        lado = float(self.lado.get())

        volumen = lado**3
        superficie = 6*(lado**2)

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm^3")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Prisma(Figuras):

    def __init__(self):

        super().__init__("Prisma", "imagenesE3/prisma.png")

        tkinter.Label(self.frame, text="Base en centimetros:").grid(row=0, column=0)
        self.base = tkinter.Entry(self.frame)
        self.base.grid(row=0, column=1)

        tkinter.Label(self.frame, text="Altura en centimetros:").grid(row=1, column=0)
        self.altura = tkinter.Entry(self.frame)
        self.altura.grid(row=1, column=1)

        tkinter.Label(self.frame, text="Longitud lateral en centimetros:").grid(row=2, column=0)
        self.longitud = tkinter.Entry(self.frame)
        self.longitud.grid(row=2, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=3, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen del prisma:")
        self.volumen_label.grid(row=4, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie del prisma:")
        self.superficie_label.grid(row=5, column=0)

    def valores(self):

        base = float(self.base.get())
        altura = float(self.altura.get())
        longitud_lateral = float(self.longitud.get())

        volumen = base*altura*longitud_lateral
        superficie = 2*((base*altura) + (base*longitud_lateral) + (altura*longitud_lateral))

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm3^")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Cono(Figuras):

    def __init__(self):

        super().__init__("Cono", "imagenesE3/cono.png")

        tkinter.Label(self.frame, text="Radio en centimetros:").grid(row=0, column=0)
        self.radio = tkinter.Entry(self.frame)
        self.radio.grid(row=0, column=1)

        tkinter.Label(self.frame, text="Altura en centimetros:").grid(row=1, column=0)
        self.altura = tkinter.Entry(self.frame)
        self.altura.grid(row=1, column=1)

        tkinter.Label(self.frame, text="Generatriz en centimetros:").grid(row=2, column=0)
        self.generatriz = tkinter.Entry(self.frame)
        self.generatriz.grid(row=2, column=1)

        tkinter.Button(self.frame, text="Calcular", command=self.valores).grid(row=3, column=1)
        self.volumen_label = tkinter.Label(self.frame, text="Volumen del cono:")
        self.volumen_label.grid(row=4, column=0)

        self.superficie_label = tkinter.Label(self.frame, text="Superficie del cono:")
        self.superficie_label.grid(row=5, column=0)

    def valores(self):

        radio = float(self.radio.get())
        altura = float(self.altura.get())
        generatriz = float(self.generatriz.get())

        volumen = (np.pi*(radio**2)*altura)/3
        superficie = np.pi*radio*(radio + generatriz)

        self.volumen_label.config(text=f"Volumen: {volumen:.2f} Cm^^3")
        self.superficie_label.config(text=f"Superficie: {superficie:.2f} Cm^2")

class Mostrar:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Volumen y superficie de figuras geométricas")

        self.frame = tkinter.Frame(self.window)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        tkinter.Button(self.frame, text="Cilindro", command=Cilindro).grid(row=0, column=0)
        tkinter.Button(self.frame, text="Esfera", command=Esfera).grid(row=0, column=1)
        tkinter.Button(self.frame, text="Pirámide", command=Piramide).grid(row=0, column=2)
        tkinter.Button(self.frame, text="Cubo", command=Cubo).grid(row=0, column=3)
        tkinter.Button(self.frame, text="Prisma", command=Prisma).grid(row=0, column=4)
        tkinter.Button(self.frame, text="Cono", command=Cono).grid(row=0, column=5)

        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=3, pady=5)

        self.window.mainloop()


Mostrar()