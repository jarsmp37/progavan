import tkinter as tk
from tkinter import *
from ejemplo1 import personas
from tkinter import messagebox

def al_cerrar():
    personas.guardar_usuarios("Usuarios.json")
    ventana1.destroy()

def registrar_usuario():
    Nombre=entnombre.get()
    Edad=entedad.get()
    personas(Nombre,Edad)
    messagebox.showinfo("Registro exitoso",f"El usuario {Nombre} se registró")
    entnombre.delete(0,tk.END)
    entedad.delete(0,tk.END)

def editar():
    pass

def eliminar():
    pass


def mostrarusuarios():
    ventana_usuarios=tk.Toplevel(ventana1)
    ventana_usuarios.title("Usuarios Registrados")
    ventana_usuarios.geometry("500x400")

    #Jalar lista de la clase
    usuarios=personas.obtener_lista()

    #ciclo for para imprimir los datos
    for i, usuario in enumerate(usuarios,start=1):
        etiqueta_usuario=Label(ventana_usuarios,text=usuario.mostrardatos())
        etiqueta_usuario.pack(pady=7,side="left")
        boton_editar=Button(ventana_usuarios,text="editar",command=editar)
        boton_editar.pack(pady=5,side="right")
        boton_eliminar=Button(ventana_usuarios,text="eliminar",command=eliminar)
        boton_eliminar.pack(pady=5,side="right")


ventana1=tk.Tk()
ventana1.title("Registro de usuarios")
ventana1.geometry("500x400")
personas.cargar_usuarios("Usuarios.json")

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

boton_mostrar=Button(ventana1,text="Mostrar usuarios",command=mostrarusuarios)
boton_mostrar.pack(pady=6)

ventana1.protocol("WM_DELETE_WINDOW",al_cerrar)
ventana1.mainloop()