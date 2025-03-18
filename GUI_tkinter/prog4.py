import tkinter as tk
from PIL import Image, ImageTk 

root = tk.Tk()
root.title("Imagen en Tkinter")

# Cargar la imagen
imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//pythonimg.jpg")
imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 

label_imagen = tk.Label(root,
                        text="estoy probando ubicación", 
                        font=("Arial", 14,"italic"), 
                        fg="white", 
                        bg="black",
                        padx=20,
                        pady=10,
                        image=imagen_tk,
                        compound="center")
label_imagen.pack(pady=20) 

root.mainloop()