import tkinter as tk
from PIL import Image, ImageTk
from backconguardado import *

def ventanainicio():
    venta1 = tk.Tk()
    venta1.title("Inicio de Sesión")
    venta1.geometry("400x400")
    venta1.config(bg="lightblue")

    global entrada1,entrada2

    canvas = tk.Canvas(venta1, width=400, height=400)
    canvas.pack()
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Hotel//imaghotel.jpg")
    fondo = ImageTk.PhotoImage(imagen)
    canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
    canvas.image = fondo 

    
    etiqueta1 = tk.Label(venta1, text="Usuario:", bg="lightblue")
    entrada1 = tk.Entry(venta1)
    etiqueta2 = tk.Label(venta1, text="Contraseña:", bg="lightblue")
    entrada2 = tk.Entry(venta1, show="*")  

    
    canvas.create_window(100, 50, window=etiqueta1)
    canvas.create_window(250, 50, window=entrada1)
    canvas.create_window(100, 100, window=etiqueta2)
    canvas.create_window(250, 100, window=entrada2)

    
    boton_login = tk.Button(venta1, text="Iniciar Sesión", command=inicio)
    canvas.create_window(200, 150, window=boton_login)

    venta1.mainloop()

def inicio():
    usuario=entrada1.get()
    password=entrada2.get()
    usuario_iniciar=Usuario.iniciar_sesion(usuario,password)

    if usuario_iniciar.rol=="Administrador":
        ventanadmin()
    elif usuario_iniciar.rol=="Recepcionista":
        ventanarecep()
    
    

def ventanadmin():
    venta2 = tk.Toplevel()
    venta2.title("Ventana admin")
    venta2.geometry("600x500")
    tk.Label(venta2, text="Bienvenido, Administrador").pack()

def ventanarecep():
    venta3 = tk.Toplevel()
    venta3.title("Ventana recepción")
    venta3.geometry("600x500")
    tk.Label(venta3, text="Bienvenido, Recepcionista").pack()


ventanainicio()