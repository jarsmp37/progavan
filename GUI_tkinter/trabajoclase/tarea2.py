import tkinter as tk
from PIL import Image, ImageTk 
from tkinter import messagebox

def decision():
    variable=opcion.get()
    if variable=="Perro":
        ventanaperro()

def ventanaperro():
    ventap=tk.Tk()
    ventap.title("Esta es la ventana del perro")
    ventap.geometry("300x200")


def venprincipal():
    global opcion
    ventana1=tk.Tk()
    ventana1.title("Trabajo Clase de animales")
    ventana1.geometry("800x450")

    opcion=tk.StringVar()
    radiobutton1 = tk.Radiobutton(ventana1, text="Perro", variable=opcion, value="Perro")
    radiobutton1.pack(pady=5)
    radiobutton2 = tk.Radiobutton(ventana1, text="Gato", variable=opcion, value=2)
    radiobutton2.pack(pady=5)
    radiobutton3 = tk.Radiobutton(ventana1, text="Elefante", variable=opcion, value=3)
    radiobutton3.pack(pady=5)
    radiobutton4 = tk.Radiobutton(ventana1, text="Cocodrilo", variable=opcion, value=4)
    radiobutton4.pack(pady=5)

    Boton=tk.Button(ventana1,text="Descripción",command=decision)
    Boton.pack()

    ventana1.mainloop()

venprincipal()