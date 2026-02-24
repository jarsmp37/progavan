import tkinter as tk
from tkinter import messagebox

def seleccionados():
    lista=[]
    if var1.get()==1:
        lista.append("Python")
    if var2.get()==1:
        lista.append("Java")
    if var3.get()==1:
        lista.append("C++")
    print(f"Los programas que dominas son: {lista}")

ventana1=tk.Tk()
ventana1.title=("Lenguaje de programación")
ventana1.geometry("400x500")

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

etiqueta1=tk.Label(ventana1,text="Selecciona el lenguaje que sabes ocupar:")
etiqueta1.pack(pady=20)

python=tk.Checkbutton(ventana1,text="Python",variable=var1)
python.pack(padx=10,pady=20)

java=tk.Checkbutton(ventana1,text="Java",variable=var2)
java.pack(padx=10,pady=20)

cmas=tk.Checkbutton(ventana1,text="C++",variable=var3)
cmas.pack(padx=10,pady=20)

tk.Button(ventana1,text="Enviar",command=seleccionados).pack(pady=10)

ventana1.mainloop()