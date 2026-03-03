import tkinter as tk
from PIL import Image, ImageTk 

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("600x300")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Reino Animal",bg="lightblue",font=("Arial",23,"bold"))
    eti1.pack()
    frame1= tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("C:/Users/Jaime/Documents/GitHub/progavan/GUI_tkinter/ejercicios/reino.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2,text="Elefante",variable=var,value=1)
    ele.pack()
    jirafa=tk.Radiobutton(frame2,text="Jirafa",variable=var,value=2)
    jirafa.pack()
    castor=tk.Radiobutton(frame2,text="Castor",variable=var,value=3)
    castor.pack()
    leon=tk.Radiobutton(frame2,text="León",variable=var,value=4)
    leon.pack()

    def informacion():
        seleccion=var.get()
        if seleccion==1:
            ventana_elefante()


    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()  # Cerrar la segunda ventana
    ventana_principal()  # Volver a abrir la ventana principal

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("500x500")
    ven2.config(bg="gray")

    eti2=tk.Label(ven2,text="Elefante",bg="gray",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)
    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()

ventana_principal()