import tkinter as tk
from tkinter import *
from ejemplo1 import personas
from tkinter import messagebox, ttk

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
    ventana_edicion=tk.Toplevel(ventana_usuarios)
    ventana_edicion.title("Edición de usuarios")
    ventana_edicion.geometry("500x400")

    ventana_edicion.mainloop()


def eliminar(usuario):
    ventana_usuarios.destroy()
    respuesta = messagebox.askyesno("Pregunta", f"¿Quieres eliminar al usuario {usuario.nombre}?")
    if respuesta:
        personas.eliminar_usuario(usuario)
        messagebox.showinfo("Eliminar usuario",f"Eliminaste al {usuario.nombre}")
        mostrarusuarios()
    else:
        mostrarusuarios()
     


def mostrarusuarios():
    global ventana_usuarios
    ventana_usuarios=tk.Toplevel(ventana1)
    ventana_usuarios.title("Usuarios Registrados")
    ventana_usuarios.geometry("500x400")

    #canvas=tk.Canvas(ventana_usuarios)
    #scrolbar=ttk.Scrollbar(ventana_usuarios,orient="vertical",command=canvas.yview)
    #frame_usuarios =tk.Frame(canvas)
    #canvas.configure(yscrollcommand=scrolbar.set)
    #canvas.create_window((0,0),window=frame_usuarios,anchor="nw")
    #canvas.pack(side="left",fill="both",expand=True)
    #scrolbar.pack(side="right",fill="y")

    #Jalar lista de la clase
    usuarios=personas.obtener_lista()

    #ciclo for para imprimir los datos
    for i, usuario1 in enumerate(usuarios,start=1):
        frame1=Frame(ventana_usuarios)
        frame1.pack(pady=7)
        etiqueta_usuario=Label(frame1,text=usuario1.mostrardatos())
        etiqueta_usuario.pack(pady=7,side="left")
        boton_editar=Button(frame1,text="editar",command=lambda u=usuario1: editar(u))
        boton_editar.pack(pady=5,side="right")
        boton_eliminar=Button(frame1,text="eliminar",command=lambda u=usuario1: eliminar(u))
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