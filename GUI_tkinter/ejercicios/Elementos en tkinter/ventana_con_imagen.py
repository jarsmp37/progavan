import tkinter as tk
from PIL import Image, ImageTk 

root = tk.Tk()
root.title("Imagen en Tkinter")
# Cargar la imagen
imagen = Image.open("progavan/GUI_tkinter/ejercicios/Elementos en tkinter/04.jpg")
imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 
label_imagen = tk.Label(root, image=imagen_tk)
label_imagen.pack(pady=20) 

root.mainloop()