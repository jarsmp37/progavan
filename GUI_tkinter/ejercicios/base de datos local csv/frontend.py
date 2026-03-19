import tkinter as tk
from backend import *
from tkinter import messagebox


def ventana_registrar():
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
        food=entrada3.get()
        nuevo_usuario=Usuario(name,age,food)
        entrada1.delete(0,tk.END)
        entrada2.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        messagebox.showinfo("Registro de usuario","Tu registro fué exitoso")

    boton1=tk.Button(venta1,text="Registrar",command=registrar)
    boton1.pack(pady=15)

    def mostrar():
        usuarios = Usuario.mostrar_usuarios()
        for u in usuarios:
            print(u.mostrar_info())

    boton2=tk.Button(venta1,text="Mostrar lista",command=mostrar)
    boton2.pack(pady=15)

    def al_cerrar():
        print("Guardando datos antes de salir...")
        Usuario.guardar_usuarios()
        venta1.destroy() # Cierra la ventana físicamente
    
    # Configuración de que pasa al cerrar la ventana
    venta1.protocol("WM_DELETE_WINDOW", al_cerrar)

    venta1.mainloop()

def ventana_login():
    global ven2
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
        name = entrada4.get()
        password = entrada5.get()
        usuario_encontrado = None
        for u in Usuario.lista:
            if u.nombre == name:
                usuario_encontrado = u
                break

        if usuario_encontrado:
            if usuario_encontrado.contra == password:
                if name == "Administrador":
                    messagebox.showinfo("Login", "Bienvenido, Administrador")
                    ven2.destroy() 
                    ventana_Administrador()
                if name == "Normal":
                    messagebox.showinfo("Login", "Bienvenido, usuario normal")
                    ven2.destroy() 
                    ventana_Normal()
                if name == "Jaime":
                    messagebox.showinfo("Login", "Bienvenido, Jimmy")
                    ven2.destroy() 
                    ventana_jaime()
                else:
                    messagebox.showinfo("Login", f"Bienvenido {name}")
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            messagebox.showwarning("Login", "El usuario no existe en la base de datos")
    
    boton4=tk.Button(ven2,text="Iniciar sesión",command=iniciar)
    boton4.pack(pady=10)
    ven2.mainloop()

def ventana_Administrador():
    
    ven3=tk.Tk()
    ven3.title("Título")
    ven3.geometry("400x500")

    etiqueta4=tk.Label(ven3,text="Bienvenido Administrador")
    etiqueta4.pack(pady=10)

    boton1=tk.Button(ven3,text="Registrar usuarios", command=ventana_registrar)
    boton1.pack(pady=10)
    boton2=tk.Button(ven3,text="Opción 2")
    boton2.pack(pady=10)
    boton3=tk.Button(ven3,text="Opción 3")
    boton3.pack(pady=10)
    boton4=tk.Button(ven3,text="Opción 4")
    boton4.pack(pady=10)

    ven3.mainloop()

def ventana_Normal():
    
    ven3=tk.Tk()
    ven3.title("Usuario normal")
    ven3.geometry("400x500")

    etiqueta4=tk.Label(ven3,text="Bienvendido usuario normal")
    etiqueta4.pack(pady=10)

    boton1=tk.Button(ven3,text="Opción 1")
    boton1.pack(pady=10)
    boton2=tk.Button(ven3,text="Opción 2")
    boton2.pack(pady=10)
    boton3=tk.Button(ven3,text="Opción 3")
    boton3.pack(pady=10)
    boton4=tk.Button(ven3,text="Opción 4")
    boton4.pack(pady=10)

    ven3.mainloop()


def ventana_jaime():
    
    ven3=tk.Tk()
    ven3.title("Título")
    ven3.geometry("400x500")

    etiqueta4=tk.Label(ven3,text="Esta es mi ventana")
    etiqueta4.pack(pady=10)

    boton1=tk.Button(ven3,text="Opción 1")
    boton1.pack(pady=10)
    boton2=tk.Button(ven3,text="Opción 2")
    boton2.pack(pady=10)
    boton3=tk.Button(ven3,text="Opción 3")
    boton3.pack(pady=10)
    boton4=tk.Button(ven3,text="Opción 4")
    boton4.pack(pady=10)

    ven3.mainloop()

def ventana_plantilla():
    
    ven3=tk.Tk()
    ven3.title("Título")
    ven3.geometry("400x500")

    etiqueta4=tk.Label(ven3,text="Aquí va texto")
    etiqueta4.pack(pady=10)

    boton1=tk.Button(ven3,text="Opción 1")
    boton1.pack(pady=10)
    boton2=tk.Button(ven3,text="Opción 2")
    boton2.pack(pady=10)
    boton3=tk.Button(ven3,text="Opción 3")
    boton3.pack(pady=10)
    boton4=tk.Button(ven3,text="Opción 4")
    boton4.pack(pady=10)

    ven3.mainloop()

ventana_login()