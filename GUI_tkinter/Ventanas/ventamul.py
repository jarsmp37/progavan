import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk 

def decision():
    variable = opcion.get()
    if variable == "Perro":
        ventanaperro()
    elif variable == "Gato":
        ventanagato()
    elif variable == "Elefante":
        ventanaelefante()
    elif variable == "Cocodrilo":
        ventanacoco()

def ventanaperro():
    ventana1.destroy()  
    ventap = tk.Tk()
    ventap.title("Esta es la ventana del perro")
    ventap.geometry("500x400")
    frame1=tk.Frame(ventap)
    frame1.pack(fill=tk.X,side=tk.LEFT, padx=5)
    frame2=tk.Frame(ventap)
    frame2.pack(side="top", padx=5)

    global imagen_tk  
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Ventanas//perro.jpg")
    imagen = imagen.resize((300, 400))  
    imagen_tk = ImageTk.PhotoImage(imagen) 

    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.pack(pady=20)

    texto1=("El perro es un mamífero doméstico que pertenece a la familia de los cánidos. Es un animal cuadrúpedo, carnívoro y sociable"
            "Características físicas:"
            "Su tamaño, forma y pelaje varían según la raza."
            "Tienen un olfato muy agudo."
            "Tienen un amplio espectro auditivo."
            "Son capaces de detectar el movimiento y la luz a la distancia."
            "Tienen una membrana nictitante, también llamada tercer párpado."
            "Nacen sordos y ciegos.")

    label_texto= Label(frame2,text=texto1,wraplength=180)
    label_texto.pack(padx=3)

    boton_regresar = tk.Button(frame2, text="Regresar", command=lambda: regresar_a_principal(ventap))
    boton_regresar.pack(pady=20)

def ventanagato():
    ventana1.destroy()  
    ventap = tk.Tk()
    ventap.title("Esta es la ventana del gato")
    ventap.geometry("500x400")
    frame1=tk.Frame(ventap)
    frame1.pack(fill=tk.X,side=tk.LEFT, padx=5)
    frame2=tk.Frame(ventap)
    frame2.pack(side="top", padx=5)

    global imagen_tk  
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Ventanas//gato.jpg")
    imagen = imagen.resize((300, 400))  
    imagen_tk = ImageTk.PhotoImage(imagen) 

    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.pack(pady=20)

    texto1=("Los gatos son mamíferos carnívoros que se caracterizan por tener un cuerpo cubierto de pelo, cuatro patas, rabo, y uñas afiladas. Son animales ágiles, rápidos y con un excelente sentido del olfato, oído y vista." 
    "Características físicas"
    "Tienen un cuerpo flexible, ligero, musculoso y compacto." 
    "Sus patas delanteras tienen cinco dígitos y las traseras cuatro." 
    "Sus garras son retráctiles, largas, afiladas, muy curvadas y comprimidas lateralmente." 
    "Su pelaje suele ser suave, dando lugar a una amplia gama de colores y patrones." 
    "Sus ojos son muy variados en colores, destacando el verde, el amarillo. ")

    label_texto= Label(frame2,text=texto1,wraplength=180)
    label_texto.pack(padx=3)

    boton_regresar = tk.Button(frame2, text="Regresar", command=lambda: regresar_a_principal(ventap))
    boton_regresar.pack(pady=20)

def ventanaelefante():
    ventana1.destroy()  
    ventap = tk.Tk()
    ventap.title("Esta es la ventana del gato")
    ventap.geometry("500x400")
    frame1=tk.Frame(ventap)
    frame1.pack(fill=tk.X,side=tk.LEFT, padx=5)
    frame2=tk.Frame(ventap)
    frame2.pack(side="top", padx=5)

    global imagen_tk  
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Ventanas//elefante.jpg")
    imagen = imagen.resize((300, 400))  
    imagen_tk = ImageTk.PhotoImage(imagen) 

    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.pack(pady=20)

    texto1=("Los gatos son mamíferos carnívoros que se caracterizan por tener un cuerpo cubierto de pelo, cuatro patas, rabo, y uñas afiladas. Son animales ágiles, rápidos y con un excelente sentido del olfato, oído y vista." 
    "Características físicas"
    "Tienen un cuerpo flexible, ligero, musculoso y compacto." 
    "Sus patas delanteras tienen cinco dígitos y las traseras cuatro." 
    "Sus garras son retráctiles, largas, afiladas, muy curvadas y comprimidas lateralmente." 
    "Su pelaje suele ser suave, dando lugar a una amplia gama de colores y patrones." 
    "Sus ojos son muy variados en colores, destacando el verde, el amarillo. ")

    label_texto= Label(frame2,text=texto1,wraplength=180)
    label_texto.pack(padx=3)

    boton_regresar = tk.Button(frame2, text="Regresar", command=lambda: regresar_a_principal(ventap))
    boton_regresar.pack(pady=20)

def ventanacoco():
    ventana1.destroy()  
    ventap = tk.Tk()
    ventap.title("Esta es la ventana del gato")
    ventap.geometry("500x400")
    frame1=tk.Frame(ventap)
    frame1.pack(fill=tk.X,side=tk.LEFT, padx=5)
    frame2=tk.Frame(ventap)
    frame2.pack(side="top", padx=5)

    global imagen_tk  
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Ventanas//cocodrilo.jpg")
    imagen = imagen.resize((300, 400))  
    imagen_tk = ImageTk.PhotoImage(imagen) 

    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.pack(pady=20)

    texto1=("Los gatos son mamíferos carnívoros que se caracterizan por tener un cuerpo cubierto de pelo, cuatro patas, rabo, y uñas afiladas. Son animales ágiles, rápidos y con un excelente sentido del olfato, oído y vista." 
    "Características físicas"
    "Tienen un cuerpo flexible, ligero, musculoso y compacto." 
    "Sus patas delanteras tienen cinco dígitos y las traseras cuatro." 
    "Sus garras son retráctiles, largas, afiladas, muy curvadas y comprimidas lateralmente." 
    "Su pelaje suele ser suave, dando lugar a una amplia gama de colores y patrones." 
    "Sus ojos son muy variados en colores, destacando el verde, el amarillo. ")

    label_texto= Label(frame2,text=texto1,wraplength=180)
    label_texto.pack(padx=3)

    boton_regresar = tk.Button(frame2, text="Regresar", command=lambda: regresar_a_principal(ventap))
    boton_regresar.pack(pady=20)

def regresar_a_principal(ventana_actual):
    ventana_actual.destroy()  
    venprincipal()  

def venprincipal():
    global ventana1, opcion
    ventana1 = tk.Tk()
    ventana1.title("Trabajo Clase de animales")
    ventana1.geometry("800x450")

    opcion = tk.StringVar(value="Perro")
    radiobutton1 = tk.Radiobutton(ventana1, text="Perro", variable=opcion, value="Perro")
    radiobutton1.pack(pady=5)
    radiobutton2 = tk.Radiobutton(ventana1, text="Gato", variable=opcion, value="Gato")
    radiobutton2.pack(pady=5)
    radiobutton3 = tk.Radiobutton(ventana1, text="Elefante", variable=opcion, value="Elefante")
    radiobutton3.pack(pady=5)
    radiobutton4 = tk.Radiobutton(ventana1, text="Cocodrilo", variable=opcion, value="Cocodrilo")
    radiobutton4.pack(pady=5)

    Boton = tk.Button(ventana1, text="Descripción", command=decision)
    Boton.pack()

    ventana1.mainloop()

venprincipal()