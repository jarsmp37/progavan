#Importamos librerías
import tkinter as tk

#Definimos la ventana
ven1 = tk.Tk()
#Le damos un título a la ventana
ven1.title("Mi primera aplicación con Tkinter")
#Programamos dimensiones
ven1.geometry("800x500")
# Iniciar el bucle principal de la aplicación
etiqueta = tk.Label(ven1,text="¡Hola, Grupo de programación Avanzada!", 
    font=("Arial", 28, "bold"), fg="white",bg="black",padx=20, pady=10)
etiqueta.pack()
etiqueta2 = tk.Label(ven1,text="Mi nombre es jaime", 
    font=("Arial", 23, "bold"),padx=20, pady=10)
etiqueta2.pack()
ven1.mainloop()