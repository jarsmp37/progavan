import tkinter as tk
from backend import *
from tkinter import messagebox

from basedatos import *

# 1. Instancia el gestor globalmente
gestor = GestorUsuarios()

def ventana_principal():
    venta1=tk.Tk()
    venta1.title("Base de datos")
    venta1.geometry("400x400")
    

    etiqueta1=tk.Label(venta1,text="Nombre")
    etiqueta1.pack()
    entrada1=tk.Entry(venta1,width=40)
    entrada1.pack(pady=15)

    etiqueta2=tk.Label(venta1,text="Edad")
    etiqueta2.pack()
    entrada2=tk.Entry(venta1,width=40)
    entrada2.pack(pady=15)

    etiqueta3=tk.Label(venta1,text="Contraseña")
    etiqueta3.pack()
    entrada3=tk.Entry(venta1,width=40)
    entrada3.pack(pady=15)
    
    def registrar():
        name=entrada1.get()
        age=entrada2.get()
        contra=entrada3.get()
        newuser=Usuario(name,age,contra)
        gestor.usuarios_nuevos.append(newuser)
        entrada1.delete(0,tk.END)
        entrada2.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        messagebox.showinfo("Registro de usuario","Tu registro fué exitoso")


    boton1=tk.Button(venta1,text="Registrar",command=registrar)
    boton1.pack(pady=15)
    def mostrar():
        usuarios = Usuario.mostrar_lista()
        for u in usuarios:
            print(u.mostrar_datos())

    boton2=tk.Button(venta1,text="Mostrar lista",command=mostrar)
    boton2.pack(pady=15)

    def al_cerrar():
        print("Guardando datos antes de salir...")
        Usuario.guardar_usuarios()
        gestor.guardar_en_supabase()
        venta1.destroy() # Cierra la ventana físicamente
    
    # Configuración de que pasa al cerrar la ventana
    venta1.protocol("WM_DELETE_WINDOW", al_cerrar)

    venta1.mainloop()

def ventana_login():
    ven2=tk.Tk()
    ven2.title("Inicio de Sesión")
    ven2.geometry("400x300")
    Usuario.cargar_usuarios()
    etiqueta3=tk.Label(ven2,text="Usuario")
    etiqueta3.pack()
    entrada4=tk.Entry(ven2,width=60)
    entrada4.pack(pady=10)
    etiqueta4=tk.Label(ven2,text="Password")
    etiqueta4.pack(pady=10)
    entrada5=tk.Entry(ven2,width=60)
    entrada5.pack(pady=10)

    def iniciar():
        name=entrada4.get()
        password=entrada5.get()
        for x in Usuario.lista:
            if name == x.nombre:
                if password==x.contra:
                    ventana_principal()
            else:
                messagebox.showwarning("inicio de sesión","El usuario no existe")
    
    

    boton4=tk.Button(ven2,text="Iniciar sesión",command=iniciar)
    boton4.pack(pady=10)

    ven2.mainloop()

ventana_login()