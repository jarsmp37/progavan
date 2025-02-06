import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Básico")
ventana.geometry("600x450")

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
etiqueta.grid(row=0,column=0)
#etiqueta.pack(side=tk.RIGHT)
#etiqueta.place(x=0,y=0)
# Crear etiqueta
etiqueta2 = tk.Label(
    ventana,
    text="Esta es mi segunda etiqueta", 
    font=("Arial", 14,"underline"), 
    fg="white", 
    bg="green",
    padx=20,
    pady=10
)
etiqueta2.grid(row=0,column=1)
#etiqueta2.pack(side=tk.LEFT)
#etiqueta.place(x=0,y=0)
# Crear etiqueta
etiqueta3 = tk.Label(
    ventana,
    text="estoy probando ubicación", 
    font=("Arial", 14,"italic"), 
    fg="white", 
    bg="black",
    padx=20,
    pady=10
)
etiqueta3.grid(row=1,column=2)
#etiqueta3.pack(side=tk.TOP)
#etiqueta.place(x=0,y=0)

ventana.mainloop()