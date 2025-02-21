import tkinter as tk
from tkinter import *
from ejemplo1 import personas
from tkinter import messagebox, ttk

def al_cerrar():
    personas.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oop1//Usuarios.json")
    ventana1.destroy()

def guardar_cambios():
    global usuario_actual

    nuevo_nombre = obt_nombre_editar.get()
    nueva_edad = obt_edad_editar.get()
    
    usuario_actual.nombre = nuevo_nombre
    usuario_actual.edad = nueva_edad
    

    personas.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oop1//Usuarios.json")

    ventana_editar.destroy()

    mostrarusuarios()

def editar(usuario):
    global ventana_editar, obt_nombre_editar, obt_edad_editar, usuario_actual
    ventana_usuarios.destroy()

    usuario_actual = usuario  

    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Usuario")
    ventana_editar.geometry("300x400")

    
    etiqueta_nom_editar = tk.Label(ventana_editar, text="Nombre")
    etiqueta_nom_editar.pack(pady=5)
    obt_nombre_editar = tk.Entry(ventana_editar)
    obt_nombre_editar.insert(0, usuario.nombre)  
    obt_nombre_editar.pack(pady=5)

    etiqueta_edad_editar = tk.Label(ventana_editar, text="Edad")
    etiqueta_edad_editar.pack(pady=5)
    obt_edad_editar = tk.Entry(ventana_editar)
    obt_edad_editar.insert(0, usuario.edad) 
    obt_edad_editar.pack(pady=5)

    boton_guardar = tk.Button(ventana_editar, text="Guardar", command=guardar_cambios)
    boton_guardar.pack(pady=10)

    boton_cancelar = tk.Button(ventana_editar, text="Cancelar", command=ventana_editar.destroy)
    boton_cancelar.pack(pady=10)



def registrar_usuario():
    Nombre=entnombre.get()
    Edad=entedad.get()
    personas(Nombre,Edad)
    messagebox.showinfo("Registro exitoso",f"El usuario {Nombre} se registró")
    entnombre.delete(0,tk.END)
    entedad.delete(0,tk.END)


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

    canvas = tk.Canvas(ventana_usuarios)
    scrollbar = tk.Scrollbar(ventana_usuarios, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Empaquetar el Canvas y el Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")



    usuarios=personas.obtener_lista()

    for i, usuario1 in enumerate(usuarios,start=1):
        frame1=Frame(scrollable_frame)
        frame1.pack(pady=7,fill=tk.X)
        etiqueta_usuario=Label(frame1,text=usuario1.mostrardatos())
        etiqueta_usuario.pack(pady=7,side="left")
        boton_editar=Button(frame1,text="editar",command=lambda u=usuario1: editar(u))
        boton_editar.pack(pady=5,side="right")
        boton_eliminar=Button(frame1,text="eliminar",command=lambda u=usuario1: eliminar(u))
        boton_eliminar.pack(pady=5,side="right")


ventana1=tk.Tk()
ventana1.title("Registro de usuarios")
ventana1.geometry("500x400")
personas.cargar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oop1//Usuarios.json")

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