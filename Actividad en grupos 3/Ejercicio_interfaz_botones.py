import tkinter
from tkinter import messagebox

class Create:
    def __init__(self):
        name = Name_entry.get().strip().lower()
        number = Number_entry.get().strip()

        if name == "" or number =="":
            messagebox.showwarning ("Campo vacío", "Debes ingresar la información del contacto (nombre/número)")
            return
        
        if not name.replace(" ", "").isalpha():
            messagebox.showwarning ("Nombre inválido", "El nombre del contacto no puede contener números o símbolos")
            return
        
        try:
            number = int(Number_entry.get())

        except ValueError:
            messagebox.showwarning ("Número inválido", "El número de contacto no puede contener letras o símbolos")
            return

        try: 
            with open("Controlu.txt", "r") as file:
                for line in file:
                    Existing_name = line.split("!")[0]

                if Existing_name == name.lower():
                    messagebox.showwarning ("Contacto existente","Este contacto ya existe, si quieres actualizarlo por favor usa el botón de actualizar")
                    return
                
        except FileNotFoundError:
            pass

        try:
            with open("Controlu.txt", "r") as file:
                for line in file:
                    Existing_number = line.strip().split("!")[1]

                    if Existing_number == str(number):
                        messagebox.showwarning ("Número existente","Este número ya ha sido asignado a alguien más, si quieres actualizarlo por favor usa el botón de actualizar")
                        return
                
        except FileNotFoundError:
            pass


        with open ("Controlu.txt", "a") as file:
            file.write(f"{name}!{number}\n")

        messagebox.showinfo("Agregado", "Tu contacto ha sido creado exitosamente")

class Update: 
    def __init__(self):
        name = Name_entry.get().strip().lower()
        number = Number_entry.get().strip()

        if name == "" or number =="":
            messagebox.showwarning ("Campo vacío", "Debes ingresar la información del contacto (nombre/número)")
            return
        
        if not name.replace(" ", "").isalpha():
            messagebox.showwarning ("Nombre inválido", "El nombre del contacto no puede contener números o símbolos")
            return
        
        try:
            number = int(Number_entry.get())

        except ValueError:
            messagebox.showwarning ("Número inválido", "El número de contacto no puede contener letras o símbolos" )
            return
        
        try: 
            with open("Controlu.txt", "r") as file:
                lines = file.readlines()

            found = False

            for i in range(len(lines)):
                existing_name = lines[i].split("!")[0]

                if existing_name == name:
                    lines[i] = f"{name}!{number}\n"
                    found = True
                    break

            if not found:
                messagebox.showwarning("Contacto no encontrado", "Este contacto no existe, si querías crearlo por favor usa el botón de crear")
                return
            
            with open("Controlu.txt", "w") as file:
                file.writelines(lines)

            messagebox.showinfo("Actualizado", "El número de contacto ha sido actualizado")

        except FileNotFoundError:
            messagebox.showwarning("Error","El archivo de contactos no existe")
            return

class Delete:
    def __init__(self):
        name = Name_entry.get().strip().lower()
        number = Number_entry.get().strip()

        if name == "" or number =="":
            messagebox.showwarning ("Campo vacío", "Debes ingresar la información del contacto (nombre/número)")
            return
        
        if not name.replace(" ", "").isalpha():
            messagebox.showwarning ("Nombre inválido", "El nombre del contacto no puede contener números o símbolos")
            return
        
        try:
            number = int(Number_entry.get())

        except ValueError:
            messagebox.showwarning ("Número inválido", "El número de contacto no puede contener letras o símbolos" )
            return
        
        try: 
            with open("Controlu.txt", "r") as file:
                lines = file.readlines()

            found = False

            for i in range(len(lines)):
                existing_name = lines[i].split("!")[0]

                if existing_name == name:
                    del lines[i]
                    found = True
                    break

            if not found:
                messagebox.showwarning("Contacto no encontrado", "Este contacto no existe, si quieres crearlo por favor usa el botón de crear")
                return
            
            with open("Controlu.txt", "w") as file:
                file.writelines(lines)

            messagebox.showinfo("Eliminado", "El número de contacto ha sido eliminado")

        except FileNotFoundError:
            messagebox.showwarning("Error","El archivo de contactos no existe")
            return

class Clear:
    def __init__(self):
        Name_entry.delete(0, tkinter.END)
        Number_entry.delete(0, tkinter.END)
        
class Read:
    def __init__(self):
        try: 
            with open("Controlu.txt", "r") as file:
                lineas = file.readlines()
        except FileNotFoundError:
            messagebox.showwarning("Error", "El archivo de contactos no existe.")
            return

        ventana_contactos = tkinter.Toplevel(window_main)
        ventana_contactos.title("contactos")
        ventana_contactos.geometry("300x350")

        cuadro_texto = tkinter.Text(ventana_contactos, wrap=tkinter.WORD, width=35, height=18)
        cuadro_texto.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

        cuadro_texto.insert(tkinter.END, "CONTACTOS EN LA LISTA\n\n")
        
        try:
            for linea in lineas:
                if "!" in linea: #Separar nombre y numero
                    
                    datos = linea.strip().split("!")
                    nombre = datos[0].title() 
                    numero = datos[1]
                    cuadro_texto.insert(tkinter.END, f"Nombre: {nombre}\n Número: {numero}\n")
                    cuadro_texto.insert(tkinter.END, "---------------------------\n")

        except Exception as e:
            messagebox.showwarning("Error","Ocurrió un error al leer los contactos o el archivo está vacío.")
        cuadro_texto.config(state=tkinter.DISABLED)
        
class Exit:
    def __init__(self):
        window_main.destroy()
    

window_main = tkinter.Tk()
window_main.title ("Formulario pro max")
frame = tkinter.Frame(window_main)
frame.grid (row=0,column=0, padx=20, pady=20)

Name_label = tkinter.Label (frame, text = "Name:")
Name_label.grid (row = 0, column = 0)
Name_entry = tkinter.Entry (frame)
Name_entry.grid (row = 0, column = 1)

Number_label =tkinter.Label (frame, text = "Number:")
Number_label.grid (row = 1, column = 0)
Number_entry = tkinter.Entry (frame)
Number_entry.grid (row = 1, column = 1)

create_button = tkinter.Button (frame, text = "Create", command = Create, bg = "#7F7BB7")
create_button.grid (row = 2, column = 0)

Update_button = tkinter.Button (frame, text ="Update", command = Update, bg = "#7F7BB7")
Update_button.grid (row = 2, column = 1)

delete_button = tkinter.Button (frame, text = "Delete", command = Delete, bg = "#7F7BB7")
delete_button.grid (row = 2, column = 2)

read_button = tkinter.Button (frame, text = "Read", command = Read, bg = "#ADDDFF")
read_button.grid (row = 3, column = 0)

clear_button = tkinter.Button (frame, text ="Clear", command = Clear, bg = "#ADDDFF")
clear_button.grid (row = 3, column = 1)

exit_button = tkinter.Button (frame, text = "Exit", command = Exit, bg = "#ADDDFF")
exit_button.grid (row = 3, column = 2)

window_main.mainloop()