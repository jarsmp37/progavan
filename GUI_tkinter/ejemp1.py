import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para manejar imágenes

# Función para el botón "Registrarse"
def registrar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()
    print(f"El nombre{nombre} con correo {correo} se registró exitosamente")
    messagebox.showinfo("Registro Exitoso", f"Nombre: {nombre}\nCorreo: {correo}\nContraseña: {contraseña}")

# Función para el botón "Cancelar"
def cancelar():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x600")

# Cargar la imagen
imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//pythonimg.jpg")
imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 

label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(pady=20) 

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5,side="left")
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5,side="right")

# Etiqueta y campo de entrada para el correo electrónico
label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.pack(pady=5)

# Etiqueta y campo de entrada para la contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")  # Ocultar la contraseña
entry_contraseña.pack(pady=5)

# Botones
boton_registrar = tk.Button(ventana, text="Registrarse", command=registrar)
boton_registrar.pack(pady=10)

boton_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar)
boton_cancelar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()