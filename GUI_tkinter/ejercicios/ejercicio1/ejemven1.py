#Importamos librerías
import tkinter as tk
from PIL import Image, ImageTk 

def boton_clic():
    print("Hiciste Click!")
def actualizar_etiqueta():
    nuevo_texto = entrada.get() #Obtiene el texto en el cuadro
    etiqueta.config(text=nuevo_texto)  # Actualiza el texto
#Definimos la ventana
ven1 = tk.Tk()
#Le damos un título a la ventana
ven1.title("Mi primera aplicación con Tkinter")
#Programamos dimensiones
ven1.geometry("800x500")
# Iniciar el bucle principal de la aplicación
entrada = tk.Entry(ven1, width=30)
entrada.pack(pady=10)
# Botón
boton = tk.Button(ven1, text="Actualizar", command=actualizar_etiqueta)
boton.pack()
# Etiqueta
etiqueta = tk.Label(ven1, text="Texto inicial", font=("Arial", 12))
etiqueta.pack(pady=10)

imagen = Image.open("images.jpg")
imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 
label_imagen = tk.Label(ven1, image=imagen_tk)
label_imagen.pack(pady=20) 
boton = tk.Button(ven1, text="Haz clic aquí", command=boton_clic,
                  font=("Comic Sans",30))#,fg="Green",bg="black")
boton.pack(pady=20) 



ven1.mainloop()