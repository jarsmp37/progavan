import tkinter as tk
from tkinter import messagebox, ttk
from backend import *

root = tk.Tk()
root.title("Sistema de Consultorio Médico")
root.geometry("800x600")


Personas.cargar_usuarios()
Pacientes.cargar_pacientes()
Citas.cargar_citas()
Servicios.cargar_servicios()
expedientes = Expediente.cargar_expedientes()


def agregar_paciente():
    def guardar_paciente():
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        tipo_sangre = entry_tipo_sangre.get()
        alergias = entry_alergias.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        paciente = Pacientes(id, nombre, "Paciente", edad, tipo_sangre, alergias, peso, altura)
        Pacientes.guardar_pacientes()
        messagebox.showinfo("Éxito", "Paciente agregado correctamente")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Paciente")

    tk.Label(ventana_agregar, text="ID:").grid(row=0, column=0)
    entry_id = tk.Entry(ventana_agregar)
    entry_id.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Nombre:").grid(row=1, column=0)
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Edad:").grid(row=2, column=0)
    entry_edad = tk.Entry(ventana_agregar)
    entry_edad.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Tipo de Sangre:").grid(row=3, column=0)
    entry_tipo_sangre = tk.Entry(ventana_agregar)
    entry_tipo_sangre.grid(row=3, column=1)

    tk.Label(ventana_agregar, text="Alergias:").grid(row=4, column=0)
    entry_alergias = tk.Entry(ventana_agregar)
    entry_alergias.grid(row=4, column=1)

    tk.Label(ventana_agregar, text="Peso:").grid(row=5, column=0)
    entry_peso = tk.Entry(ventana_agregar)
    entry_peso.grid(row=5, column=1)

    tk.Label(ventana_agregar, text="Altura:").grid(row=6, column=0)
    entry_altura = tk.Entry(ventana_agregar)
    entry_altura.grid(row=6, column=1)

    tk.Button(ventana_agregar, text="Guardar", command=guardar_paciente).grid(row=7, column=0, columnspan=2)


def listar_pacientes():
    ventana_listar = tk.Toplevel(root)
    ventana_listar.title("Lista de Pacientes")

    tree = ttk.Treeview(ventana_listar, columns=("ID", "Nombre", "Edad", "Tipo de Sangre", "Alergias", "Peso", "Altura"))
    tree.heading("#0", text="ID")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Edad", text="Edad")
    tree.heading("Tipo de Sangre", text="Tipo de Sangre")
    tree.heading("Alergias", text="Alergias")
    tree.heading("Peso", text="Peso")
    tree.heading("Altura", text="Altura")

    for paciente in Pacientes.Lista_pacientes:
        tree.insert("", "end", text=paciente.id, values=(paciente.id, paciente.nombre, paciente.edad, paciente.tipo_sangre, paciente.alergias, paciente.peso, paciente.altura))

    tree.pack(expand=True, fill="both")


def agregar_cita():
    def guardar_cita():
        dia = entry_dia.get()
        hora = entry_hora.get()
        cita = Citas(dia, hora)
        Citas.guardar_citas()
        messagebox.showinfo("Éxito", "Cita agregada correctamente")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Cita")

    tk.Label(ventana_agregar, text="Día:").grid(row=0, column=0)
    entry_dia = tk.Entry(ventana_agregar)
    entry_dia.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Hora:").grid(row=1, column=0)
    entry_hora = tk.Entry(ventana_agregar)
    entry_hora.grid(row=1, column=1)

    tk.Button(ventana_agregar, text="Guardar", command=guardar_cita).grid(row=2, column=0, columnspan=2)


def listar_citas():
    ventana_listar = tk.Toplevel(root)
    ventana_listar.title("Lista de Citas")

    tree = ttk.Treeview(ventana_listar, columns=("Día", "Hora", "Disponibilidad", "Paciente", "Doctor"))
    tree.heading("#0", text="ID")
    tree.heading("Día", text="Día")
    tree.heading("Hora", text="Hora")
    tree.heading("Disponibilidad", text="Disponibilidad")
    tree.heading("Paciente", text="Paciente")
    tree.heading("Doctor", text="Doctor")

    for cita in Citas.lista_citas:
        paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
        doctor_nombre = cita.doctor.nombre if cita.doctor else "N/A"
        tree.insert("", "end", text=cita.dia, values=(cita.dia, cita.hora, "No" if not cita.Disponibilidad else "Sí", paciente_nombre, doctor_nombre))

    tree.pack(expand=True, fill="both")


def agregar_servicio():
    def guardar_servicio():
        servicio = entry_servicio.get()
        costo = float(entry_costo.get())
        Servicios(servicio, costo)
        Servicios.guardar_servicios()
        messagebox.showinfo("Éxito", "Servicio agregado correctamente")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Servicio")

    tk.Label(ventana_agregar, text="Servicio:").grid(row=0, column=0)
    entry_servicio = tk.Entry(ventana_agregar)
    entry_servicio.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Costo:").grid(row=1, column=0)
    entry_costo = tk.Entry(ventana_agregar)
    entry_costo.grid(row=1, column=1)

    tk.Button(ventana_agregar, text="Guardar", command=guardar_servicio).grid(row=2, column=0, columnspan=2)


def listar_servicios():
    ventana_listar = tk.Toplevel(root)
    ventana_listar.title("Lista de Servicios")

    tree = ttk.Treeview(ventana_listar, columns=("Servicio", "Costo"))
    tree.heading("#0", text="ID")
    tree.heading("Servicio", text="Servicio")
    tree.heading("Costo", text="Costo")

    for servicio in Servicios.Lista_servicios:
        tree.insert("", "end", text=servicio.servicio, values=(servicio.servicio, servicio.costo))

    tree.pack(expand=True, fill="both")


# Menú principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_pacientes = tk.Menu(menu_principal, tearoff=0)
menu_pacientes.add_command(label="Agregar Paciente", command=agregar_paciente)
menu_pacientes.add_command(label="Listar Pacientes", command=listar_pacientes)
menu_principal.add_cascade(label="Pacientes", menu=menu_pacientes)

menu_citas = tk.Menu(menu_principal, tearoff=0)
menu_citas.add_command(label="Agregar Cita", command=agregar_cita)
menu_citas.add_command(label="Listar Citas", command=listar_citas)
menu_principal.add_cascade(label="Citas", menu=menu_citas)

menu_servicios = tk.Menu(menu_principal, tearoff=0)
menu_servicios.add_command(label="Agregar Servicio", command=agregar_servicio)
menu_servicios.add_command(label="Listar Servicios", command=listar_servicios)
menu_principal.add_cascade(label="Servicios", menu=menu_servicios)

# Iniciar la aplicación
root.mainloop()