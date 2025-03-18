#Uso de Tkkinter
import tkinter as tk
from tkinter import ttk
#Importamos las librerias

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación con Tkinter")

#Etiqueta
etiqueta=tk.Label(ventana,text="Hola estoy en programación Avanzada creando una interfaz gráfica",
                  font=("Arial",12))
etiqueta.pack(pady=20)

#Botón
boton=tk.Button(ventana,text="Dame Click")
boton.pack()

# Establecer el tamaño de la ventana
ventana.geometry("600x400")

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

