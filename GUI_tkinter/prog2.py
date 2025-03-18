import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Básico")
ventana.geometry("400x150")

# Crear etiqueta
etiqueta = tk.Label(
    ventana,
    text="¡Hola, Grupo de programación Avanzada!", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="navy",
    padx=20,
    pady=10
)
#etiqueta.pack()
#etiqueta.place(x=0,y=0)

ventana.mainloop()
