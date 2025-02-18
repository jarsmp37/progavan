import tkinter as tk
from backendventana import Joaquin
from tkinter import messagebox

def al_cerrar():
    Joaquin.guardar_usuarios("Usuarios.json")
    ventana1.destroy()

def registrar():
    Nombre=obt_nombre.get()
    Edad=obt_edad.get()
    Sangre=obt_sangre.get()

    Joaquin(Nombre,Edad,Sangre)
    messagebox.showinfo("Registro Exitoso",f"El usuario {Nombre} quedó registrado")
    obt_nombre.delete(0,tk.END)
    obt_edad.delete(0,tk.END)
    obt_sangre.delete(0,tk.END)

def mostrarlista():
    ventana2=tk.Toplevel()
    ventana2.title("Lista de usuarios")
    ventana2.geometry("400x400")
    listausuario=Joaquin.mostarusuarios()

    for i,usuario in enumerate(listausuario,start=1):
        etiqueta_usuario=tk.Label(ventana2,text=usuario.mostrarinfo())
        etiqueta_usuario.pack(pady=6)


    ventana2.mainloop()



ventana1=tk.Tk()
ventana1.title("Ventana de Registro")
ventana1.geometry("500x400")

Joaquin.cargar_usuarios("Usuarios.json")

etiqueta_nom=tk.Label(ventana1,text="Nombre")
etiqueta_nom.pack(pady=8)
obt_nombre=tk.Entry(ventana1)
obt_nombre.pack(pady=8)

etiqueta_edad=tk.Label(ventana1,text="Edad")
etiqueta_edad.pack(pady=8)
obt_edad=tk.Entry(ventana1)
obt_edad.pack(pady=8)

etiqueta_sangre=tk.Label(ventana1,text="Tipo de Sagre")
etiqueta_sangre.pack(pady=8)
obt_sangre=tk.Entry(ventana1)
obt_sangre.pack(pady=8)

boton1=tk.Button(ventana1,text="Registrar",command=registrar)
boton1.pack(pady=8)

boton2=tk.Button(ventana1,text="Mostrar lista",command=mostrarlista)
boton2.pack(pady=7)

ventana1.protocol("WM_DELETE_WINDOW",al_cerrar)

ventana1.mainloop()