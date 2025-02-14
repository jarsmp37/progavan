import tkinter as tk
from PIL import Image, ImageTk 
from tkinter import messagebox

def registrar():
    nombre = Nombre.get()
    comida = Comida.get()
    color = Color.get()
    print(f"El nombre{nombre} con color {color} y comida {comida} se registró exitosamente")
    messagebox.showinfo("Registro Exitoso", f"Nombre: {nombre}\nComida: {comida}\n Color: {color}")

def mostrar():
    nombre2 = Nombre.get()
    comida2 = Comida.get()
    color2 = Color.get()
    respuesta = messagebox.askyesno("Pregunta", "Quieres que te muestre la información")
    if respuesta:
        messagebox.showinfo("Respuesta", f"Tu nombre es {nombre2},Tu comida favorita es {comida2} y tu color favorito es {color2}" )
    else:
        messagebox.showinfo("Respuesta", "Tu te la pierdes")



ven1=tk.Tk()
ven1.title("Trabajo Clase")
ven1.geometry("800x450")

#ImagenBuap
imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//trabajoclase//logo.png")
imagen = imagen.resize((130, 130))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 
label_imagen = tk.Label(ven1, image=imagen_tk)
label_imagen.grid(row=0, column=0, padx=5, pady=5)

carrera= tk.Label(ven1,text="Ciencia de Datos / Computación",font=("Arial", 20, "bold"), padx=20,pady=10)
carrera.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#ImagenCu2
imagen2 = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//trabajoclase//cu2.jpg")
imagen2 = imagen2.resize((160, 120))  # Redimensionar si es necesario
imagen_tk2 = ImageTk.PhotoImage(imagen2) 
label_imagen2 = tk.Label(ven1, image=imagen_tk2)
label_imagen2.grid(row=0, column=2, padx=5, pady=5)


etiqueta = tk.Label(ven1,text="Nombre",font=("Arial", 14, "bold"), fg="white",bg="navy",padx=20,pady=10)
etiqueta.grid(row=2, column=0, padx=5, pady=5)
# Campo de entrada
Nombre = tk.Entry(ven1, width=30,font=("Arial", 18, "bold"))
Nombre.grid(row=2, column=1, padx=5, pady=5,sticky="w")

etiqueta = tk.Label(ven1,text="Comida",font=("Arial", 14, "bold"), fg="white",bg="navy",padx=20,pady=10)
etiqueta.grid(row=3, column=0, padx=5, pady=5)
# Campo de entrada
Comida = tk.Entry(ven1, width=30)
Comida.grid(row=3, column=1, padx=5, pady=5)
etiqueta = tk.Label(ven1,text="Color",font=("Arial", 14, "bold"), fg="white",bg="navy",padx=20,pady=10)
etiqueta.grid(row=4, column=0, padx=5, pady=5)
# Campo de entrada
Color = tk.Entry(ven1, width=30)
Color.grid(row=4, column=1, padx=5, pady=5)

ven1.config(bg="lightblue")

boton = tk.Button(ven1, text="Registrar", command=registrar)
boton.grid(row=5, column=1, padx=5, pady=5)

boton2 = tk.Button(ven1, text="Mostrar", command=mostrar)
boton2.grid(row=5, column=2, padx=5, pady=5)


ven1.mainloop()