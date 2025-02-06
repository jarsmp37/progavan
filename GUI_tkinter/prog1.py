import tkinter as tk

# Función que se ejecuta cuando se hace clic en el botón
def boton_clic():
    print("Hiciste Click!")

# Crear la ventana principal
root = tk.Tk()
root.title("Botones en Tkinter")

# Crear un botón
boton = tk.Button(root, 
                  text="Haz clic aquí", 
                  command=boton_clic,
                  font=("Comic Sans",30),
                  #fg="Green",
                  #bg="black"
                  )
boton.pack(pady=20) 

# Iniciar el bucle principal de la ventana
root.mainloop()