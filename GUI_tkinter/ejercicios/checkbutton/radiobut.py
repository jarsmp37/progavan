import tkinter as tk
from tkinter import messagebox
def opcion():
    if var.get()==1:
        messagebox.showinfo("Opción elegida","Te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("Opción elegida","Te gustan las chanclas")
    elif var.get()==3:
        messagebox.showinfo("Opción elegida","Te gustan las milanesas")
    elif var.get()==4:
        messagebox.showinfo("Opción elegida","Te gustan las pizzas")
    else:
        messagebox.showinfo("Opción elegida","No seleccionaste nada")

ventana=tk.Tk()
ventana.title("Radio Button")
ventana.geometry("300x400")
etiqueta1=tk.Label(ventana,text="¿Cuál es tu comida favorita")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ventana,text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ventana,text="Chanclas",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ventana,text="Milanesas",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ventana,text="Pizza",variable=var,value=4)
rad4.pack()

boton1=tk.Button(ventana,text="Verificar",command=opcion)
boton1.pack(pady=30)

ventana.mainloop()