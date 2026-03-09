import tkinter as tk

def ventana_principal():
    venta1=tk.Tk()
    venta1.title("Base de datos")
    venta1.geometry("400x400")

    etiqueta1=tk.Label(venta1,text="Nombre")
    etiqueta1.pack()
    entrada1=tk.Entry(venta1,width=40)
    entrada1.pack(pady=15)

    etiqueta2=tk.Label(venta1,text="Edad")
    etiqueta2.pack()
    entrada2=tk.Entry(venta1,width=40)
    entrada2.pack(pady=15)

    etiqueta3=tk.Label(venta1,text="Comida favorita")
    etiqueta3.pack()
    entrada3=tk.Entry(venta1,width=40)
    entrada3.pack(pady=15)
    
    boton1=tk.Button(venta1,text="Registrar")
    boton1.pack(pady=15)

    boton2=tk.Button(venta1,text="Mostrar lista")
    boton2.pack(pady=15)

    venta1.mainloop()


ventana_principal()