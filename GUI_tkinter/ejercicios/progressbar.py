import tkinter as tk
from tkinter import ttk

ventana1=tk.Tk()
ventana1.title("Uso de progress bar")
ventana1.geometry("600x300")
ventana1.config(bg="Blue")

etiqueta1=tk.Label(ventana1,text="Uso de la progressbar se muestra en esta ventana",bg="blue",fg="white",
                   font=("Arial", 16))
etiqueta1.pack()

# Progressbar en modo determinate
progress = ttk.Progressbar(ventana1, orient="horizontal", length=100, mode="determinate")
progress.pack(pady=20)


def avanzar():
    progress.step(10)  # Aumenta el progreso en 10 unidades

# Botón para iniciar el progreso
btn = tk.Button(ventana1, text="Avanzar", command=avanzar)
btn.pack()
ventana1.mainloop()