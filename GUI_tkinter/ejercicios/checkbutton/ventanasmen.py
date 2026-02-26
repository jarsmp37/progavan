import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var2.get()==1:
        messagebox.showinfo("Ventana de información","Aca puedes escribir info al usuario")
    elif var2.get()==2:
        messagebox.showwarning("Ventana de advertencia","Esta es una advertencia")
    elif var2.get()==3:
        messagebox.showerror("Ventana de error","Has cometido un error")
    elif var2.get()==4:
        respuesta=messagebox.askyesno("Ventanda de opción","Te gusta esta clase")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Más te vale")
        else:
            messagebox.showinfo("Ventana de respuesta","Por eso vas a reprobar")
    elif var2.get()==5:
        respuesta=messagebox.askokcancel("Ventana de opción","Das tu alma a esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Por eso vas a sacar 10")
        else:
            messagebox.showinfo("Ventana de respuesta","Por eso repruebas")
    else:
        messagebox.showinfo("Ventana de respuesta","No elegiste ningua respuesta")
ven2=tk.Tk()
ven2.title("Uso de las diferentes messagebox")
ven2.geometry("400x500")
ven2.config(bg="lightblue")
etiqueta1=tk.Label(ven2,text="Veremos el uso de las messagebox")
etiqueta1.pack()

var2=tk.IntVar()
mes1=tk.Radiobutton(ven2,text="Mostrar información",variable=var2,value=1)
mes1.pack(pady=20)
mes2=tk.Radiobutton(ven2,text="Advertenica",variable=var2,value=2)
mes2.pack(pady=20)
mes3=tk.Radiobutton(ven2,text="Error",variable=var2,value=3)
mes3.pack(pady=20)
mes4=tk.Radiobutton(ven2,text="Pregunta si o no",variable=var2,value=4)
mes4.pack(pady=20)
mes5=tk.Radiobutton(ven2,text="Pregunta aceptar o cancelar",variable=var2,value=5)
mes5.pack(pady=20)
boton1=tk.Button(ven2,text="Sacar ventana",command=ventanas)
boton1.pack(pady=30)


ven2.mainloop()

