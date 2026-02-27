import tkinter as tk
from PIL import Image, ImageTk 

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("500x500")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Aquí estoy viendo la primera ventana",bg="lightblue")
    eti1.grid(row=0, column=0, padx=5, pady=5)
    imagen = Image.open("C:/Users/Jaime/Documents/GitHub/progavan/GUI_tkinter/ejercicios/reino.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(ven1, image=imagen_tk)
    label_imagen.grid(row=1, column=0, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(ven1,text="Elefante",variable=var,value=1)
    ele.grid(row=2, column=0, padx=5, pady=5)
    jirafa=tk.Radiobutton(ven1,text="Jirafa",variable=var,value=2)
    jirafa.grid(row=3, column=0, padx=5, pady=5)
    castor=tk.Radiobutton(ven1,text="Castor",variable=var,value=3)
    castor.grid(row=4, column=0, padx=5, pady=5)
    leon=tk.Radiobutton(ven1,text="León",variable=var,value=4)
    leon.grid(row=5, column=0, padx=5, pady=5)

    def informacion():
        seleccion=var.get()
        if seleccion==1:
            ventana_2()


    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.grid(row=6, column=0, padx=5, pady=5)

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()  # Cerrar la segunda ventana
    ventana_principal()  # Volver a abrir la ventana principal

def ventana_2():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Esta es mi ventana principal")
    ven2.geometry("500x500")
    ven2.config(bg="yellow")

    eti2=tk.Label(ven2,text="Aquí estoy viendo la segunda ventana",bg="yellow")
    eti2.pack(pady=10)
    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()

ventana_principal()