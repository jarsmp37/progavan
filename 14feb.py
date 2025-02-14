import tkinter as tk
import random

def mover_boton(event):
    ventana_ancho = ventana.winfo_width()
    ventana_alto = ventana.winfo_height()

    
    boton_ancho = boton_no.winfo_width()
    boton_alto = boton_no.winfo_height()

    
    nueva_x = random.randint(0, ventana_ancho - boton_ancho)
    nueva_y = random.randint(0, ventana_alto - boton_alto)

    
    boton_no.place(x=nueva_x, y=nueva_y)

def aceptar():
    etiqueta.config(text="¡Sabía que dirías que sí! ❤️")


ventana = tk.Tk()
ventana.title("¿Pregunta seria?")
ventana.geometry("400x300")


etiqueta = tk.Label(ventana, text="¿Quieres ser mi San Valentín?", font=("Arial", 16))
etiqueta.pack(pady=20)


boton_si = tk.Button(ventana, text="Sí", font=("Arial", 14), command=aceptar)
boton_si.pack(pady=10)


boton_no = tk.Button(ventana, text="No", font=("Arial", 14))
boton_no.pack(pady=10)


boton_no.bind("<Enter>", mover_boton)


ventana.mainloop()