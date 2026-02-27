import tkinter as tk
def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("ventana principal")
    ven1.geometry("400x300")
    ven1.config(bg="lightblue")
    eti1=tk.Label(ven1,text="Esta es la ventana principal")
    eti1.pack()

    boton1=tk.Button(ven1,text="Ventana 2",command=ventana_2)
    boton1.pack(pady=20)

    ven1.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_2():
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("ventana secundaria")
    ven2.geometry("400x300")
    ven2.config(bg="yellow")
    eti2=tk.Label(ven2,text="Esta es la ventana 2")
    eti2.pack()

    boton2=tk.Button(ven2,text="Ventana principal",command=lambda:destruir_ventana(ven2) )
    boton2.pack(pady=20)



    ven2.mainloop()

ventana_principal()
