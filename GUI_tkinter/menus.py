import tkinter as tk
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("nuevo archivo", "Creaste un nuevo archivo.")
def guardar_archivo():
    messagebox.showinfo("guardar archivo", "Guardaste un archivo.")
def cortar_a():
    messagebox.showinfo("cortar archivo", "cortaste un texto")
def pegar_a():
    messagebox.showinfo("pegar archivo", "Pegaste un texto.")

ventana=tk.Tk()
ventana.title("Uso de menus")
ventana.geometry("400x300")
barra_menu=tk.Menu(ventana)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Guardar",command=guardar_archivo)

menu_edicion= tk.Menu(barra_menu,tearoff=0)
menu_edicion.add_command(label="Cortar",command=cortar_a)
menu_edicion.add_command(label="Pegar",command=pegar_a)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
ventana.config(menu=barra_menu)

ventana.mainloop()