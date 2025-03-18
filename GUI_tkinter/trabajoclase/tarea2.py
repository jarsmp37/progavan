import tkinter as tk
from tkinter import messagebox

def decision():
    variable = opcion.get()
    if variable == "Perro":
        ventanaperro()

def ventanaperro():
    ventana1.destroy()  
    ventap = tk.Tk()
    ventap.title("Esta es la ventana del perro")
    ventap.geometry("300x200")

    boton_regresar = tk.Button(ventap, text="Regresar", command=lambda: regresar_a_principal(ventap))
    boton_regresar.pack(pady=20)

def regresar_a_principal(ventana_actual):
    ventana_actual.destroy()  
    venprincipal()  

def venprincipal():
    global ventana1, opcion
    ventana1 = tk.Tk()
    ventana1.title("Trabajo Clase de animales")
    ventana1.geometry("800x450")

    opcion = tk.StringVar(value="")
    radiobutton1 = tk.Radiobutton(ventana1, text="Perro", variable=opcion, value="Perro")
    radiobutton1.pack(pady=5)
    radiobutton2 = tk.Radiobutton(ventana1, text="Gato", variable=opcion, value="Gato")
    radiobutton2.pack(pady=5)
    radiobutton3 = tk.Radiobutton(ventana1, text="Elefante", variable=opcion, value="Elefante")
    radiobutton3.pack(pady=5)
    radiobutton4 = tk.Radiobutton(ventana1, text="Cocodrilo", variable=opcion, value="Cocodrilo")
    radiobutton4.pack(pady=5)

    Boton = tk.Button(ventana1, text="Descripción", command=decision)
    Boton.pack()

    ventana1.mainloop()

venprincipal()