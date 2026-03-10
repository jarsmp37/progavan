import tkinter as tk
from backend import *
from tkinter import messagebox

def ventana_principal():
    venta1=tk.Tk()
    venta1.title("Base de datos")
    venta1.geometry("400x400")
    Usuario.cargar_usuarios()

    etiqueta1=tk.Label(venta1,text="Nombre")
    etiqueta1.pack()
    entrada1=tk.Entry(venta1,width=40)
    entrada1.pack(pady=15)

    etiqueta2=tk.Label(venta1,text="Edad")
    etiqueta2.pack()
    entrada2=tk.Entry(venta1,width=40)
    entrada2.pack(pady=15)

    etiqueta3=tk.Label(venta1,text="Comida favorita")
    etiqueta3.pack()
    entrada3=tk.Entry(venta1,width=40)
    entrada3.pack(pady=15)
    
    def registrar():
        name=entrada1.get()
        age=entrada2.get()
        food=entrada3.get()
        newuser=Usuario(name,age,food)
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
        venta1.destroy() # Cierra la ventana físicamente
    
    # Configuración de que pasa al cerrar la ventana
    venta1.protocol("WM_DELETE_WINDOW", al_cerrar)

    venta1.mainloop()


ventana_principal()