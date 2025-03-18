import tkinter as tk
from backendventana import Joaquin
from tkinter import messagebox

def al_cerrar():
    Joaquin.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oopcontkinter//Usuarios2.json")
    ventana1.destroy()

def guardar_cambios():
    global usuario_actual

    nuevo_nombre = obt_nombre_editar.get()
    nueva_edad = obt_edad_editar.get()
    nueva_sangre = obt_sangre_editar.get()

    usuario_actual.nombre = nuevo_nombre
    usuario_actual.edad = nueva_edad
    usuario_actual.tiposangre = nueva_sangre

    Joaquin.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oopcontkinter//Usuarios2.json")

    ventana_editar.destroy()

    mostrarlista()

def editar(usuario):
    global ventana_editar, obt_nombre_editar, obt_edad_editar, obt_sangre_editar, usuario_actual

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

    etiqueta_sangre_editar = tk.Label(ventana_editar, text="Tipo de Sangre")
    etiqueta_sangre_editar.pack(pady=5)
    obt_sangre_editar = tk.Entry(ventana_editar)
    obt_sangre_editar.insert(0, usuario.tiposangre)  
    obt_sangre_editar.pack(pady=5)

    boton_guardar = tk.Button(ventana_editar, text="Guardar", command=guardar_cambios)
    boton_guardar.pack(pady=10)

    boton_cancelar = tk.Button(ventana_editar, text="Cancelar", command=ventana_editar.destroy)
    boton_cancelar.pack(pady=10)

def eliminar(usuario):
    ventana2.destroy()
    respuesta = messagebox.askyesno("Pregunta", f"¿Quieres eliminar al usuario {usuario.nombre}?")
    if respuesta:
        Joaquin.eliminar_usuario(usuario)
        messagebox.showinfo("Eliminar usuario",f"Eliminaste al {usuario.nombre}")
        mostrarlista()
    else:
        mostrarlista()

def registrar():
    Nombre=obt_nombre.get()
    Edad=obt_edad.get()
    Sangre=obt_sangre.get()

    Joaquin(Nombre,Edad,Sangre)
    #messagebox.showinfo("Registro Exitoso",f"El usuario {Nombre} quedó registrado")
    obt_nombre.delete(0,tk.END)
    obt_edad.delete(0,tk.END)
    obt_sangre.delete(0,tk.END)

def mostrarlista():
    global ventana2
    ventana2 = tk.Toplevel()
    ventana2.title("Lista de usuarios")
    ventana2.geometry("500x400")

    # Crear un Canvas y un Scrollbar
    canvas = tk.Canvas(ventana2)
    scrollbar = tk.Scrollbar(ventana2, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configurar el Canvas para que use el Scrollbar
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

    listausuario = Joaquin.mostarusuarios()

    for i, usuario in enumerate(listausuario, start=1):
        frameeti = tk.Frame(scrollable_frame)
        frameeti.pack(pady=6, fill=tk.X)
        etiqueta_usuario = tk.Label(frameeti, text=usuario.mostrarinfo())
        etiqueta_usuario.pack(padx=6, side="left")
        boton3 = tk.Button(frameeti, text="Editar", command=lambda u=usuario: editar(u))
        boton3.pack(padx=5, side="left")
        boton4 = tk.Button(frameeti, text="Eliminar", command=lambda u=usuario: eliminar(u))
        boton4.pack(padx=5, side="left")

    ventana2.mainloop()



ventana1=tk.Tk()
ventana1.title("Ventana de Registro")
ventana1.geometry("500x400")

Joaquin.cargar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oopcontkinter//Usuarios2.json")

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