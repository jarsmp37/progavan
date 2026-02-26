import tkinter as tk
from tkinter import messagebox

def estatus():
    if var.get()==1:
        messagebox.showinfo("Estado", "Checkbutton seleccionado")
    else:
        messagebox.showinfo("Estado", "Checkbutton no está seleccionado")

ven1=tk.Tk()
ven1.title("Uso del checkbutton")
ven1.geometry("400x500")

etiqueta1=tk.Label(ven1,text="Aquí voy a poner un checkbutton")
etiqueta1.pack(pady=20)

var=tk.IntVar()
bcheck=tk.Checkbutton(ven1,text="Elegir opción",variable=var)
bcheck.pack(pady=10)
boton1=tk.Button(ven1,text="Verificar Estatus",command=estatus)
boton1.pack()

ven1.mainloop()