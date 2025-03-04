import tkinter as tk
from tkinter import messagebox, ttk
from backend import *
from tkcalendar import Calendar

def obtener_fecha():
    fecha_selec=cal.get_date()
    messagebox.showinfo("Fecha seleccionada",f"Has seleccionado: {fecha_selec}")


ventanacalendario=tk.Tk()
ventanacalendario.title("Muestra de uso de calendario")
ventanacalendario.geometry("500x400")

cal=Calendar(ventanacalendario,selectmode="day",year=2025, month=3, day=4)
cal.pack(pady=10)

btn_obtner_fecha=tk.Button(ventanacalendario,text="Obtener fecha",command=obtener_fecha)
btn_obtner_fecha.pack(pady=10)

ventanacalendario.mainloop()