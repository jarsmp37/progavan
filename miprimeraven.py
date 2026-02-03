import tkinter as tk

ventana=tk.Tk()
ventana.title("Mi primera ventana")
etiqueta=tk.Label(ventana,text="Hola mundo!")
etiqueta.pack(pady=20)

ventana.mainloop()