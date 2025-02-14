import tkinter as tk
from tkinter import *
from ejemplo1 import personas
from tkinter import messagebox

def registrar_usuario():
    Nombre=entnombre.get()
    Edad=entedad.get()
    personas(Nombre,Edad)
    messagebox.showinfo("Registro exitoso",f"El usuario {Nombre} se registró")
    entnombre.delete(0,tk.END)
    entedad.delete(0,tk.END)

ventana1=tk.Tk()
ventana1.title("Registro de usuarios")
ventana1.geometry("500x400")

etinombre=Label(ventana1,text="Nombre")
etinombre.pack(pady=4)
entnombre=Entry(ventana1)
entnombre.pack(pady=4)

etiedad=Label(ventana1,text="Edad")
etiedad.pack(pady=4)
entedad=Entry(ventana1)
entedad.pack(pady=4)

boton_reg=Button(ventana1,text="Registrar",command=registrar_usuario)
boton_reg.pack(pady=6)

ventana1.mainloop()