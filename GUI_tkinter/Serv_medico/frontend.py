import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from backend import *

Personas.cargar_usuarios()
Pacientes.cargar_pacientes()
Citas.cargar_citas()
Servicios.cargar_servicios()
expedientes = Expediente.cargar_expedientes()

def ventana_principal():
    global root
    root = tk.Tk()
    root.title("Sistema de Consultorio Médico")
    root.geometry("800x600")
    root.iconbitmap("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Serv_medico//medicina.ico")

    def abrir_doctor():
        root.destroy()
        ventana_doctor()

    def abrir_recepcionista():
        root.destroy()
        ventana_recepcionista()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    boton_doctor = tk.Button(frame, text="Doctor", command=abrir_doctor, width=20, height=5)
    boton_doctor.pack(pady=10)

    boton_recepcionista = tk.Button(frame, text="Recepcionista", command=abrir_recepcionista, width=20, height=5)
    boton_recepcionista.pack(pady=10)

    root.mainloop()

def ventana_recepcionista():
    recepcionista_window = tk.Tk()
    recepcionista_window.title("Ventana de Recepcionista")
    recepcionista_window.geometry("800x600")

    def agendar_cita():
        def guardar_cita():
            cita_dia = cal.get_date()
            cita_hora = combo_hora.get()
            paciente_nombre = entry_paciente.get()
            doctor_nombre = entry_doctor.get()

            cita_existente = next((c for c in Citas.lista_citas if c.dia == cita_dia and c.hora == cita_hora), None)
            if cita_existente:
                messagebox.showerror("Error", "Ya existe una cita en esa fecha y hora.")
                return

            paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
            doctor = next((d for d in Doctores.Lista_doctores if d.nombre == doctor_nombre), None)

            if paciente and doctor:
                cita = Citas(cita_dia, cita_hora)
                cita.paciente = paciente
                cita.doctor = doctor
                cita.Disponibilidad = False
                Citas.guardar_citas()
                messagebox.showinfo("Éxito", "Cita agendada correctamente")
                ventana_agendar.destroy()
            else:
                messagebox.showerror("Error", "Paciente o doctor no encontrado.")

        ventana_agendar = tk.Toplevel(recepcionista_window)
        ventana_agendar.title("Agendar Cita")

        tk.Label(ventana_agendar, text="Seleccione el día:").pack(pady=10)
        cal = Calendar(ventana_agendar, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack(pady=10)

        tk.Label(ventana_agendar, text="Seleccione la hora:").pack(pady=10)
        horas_disponibles = [f"{h:02d}:{m:02d}" for h in range(9, 17) for m in [0, 30]]
        combo_hora = ttk.Combobox(ventana_agendar, values=horas_disponibles, state="readonly")
        combo_hora.pack(pady=10)

        tk.Label(ventana_agendar, text="Nombre del paciente:").pack(pady=10)
        entry_paciente = tk.Entry(ventana_agendar)
        entry_paciente.pack(pady=10)

        tk.Label(ventana_agendar, text="Nombre del doctor:").pack(pady=10)
        entry_doctor = tk.Entry(ventana_agendar)
        entry_doctor.pack(pady=10)

        tk.Button(ventana_agendar, text="Agendar Cita", command=guardar_cita).pack(pady=20)

    def listar_citas():
        ventana_listar = tk.Toplevel(recepcionista_window)
        ventana_listar.title("Lista de Citas")

        tree = ttk.Treeview(ventana_listar, columns=("Día", "Hora", "Paciente", "Doctor"), show="headings")
        tree.heading("Día", text="Día")
        tree.heading("Hora", text="Hora")
        tree.heading("Paciente", text="Paciente")
        tree.heading("Doctor", text="Doctor")

        tree.column("Día", width=100, anchor="center")
        tree.column("Hora", width=80, anchor="center")
        tree.column("Paciente", width=150, anchor="center")
        tree.column("Doctor", width=150, anchor="center")

        for cita in Citas.lista_citas:
            paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
            doctor_nombre = cita.doctor.nombre if cita.doctor else "N/A"
            tree.insert("", "end", values=(cita.dia, cita.hora, paciente_nombre, doctor_nombre))

        tree.pack(expand=True, fill="both")

    def agregar_paciente():
        def guardar_paciente():
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

        ventana_agregar = tk.Toplevel(recepcionista_window)
        ventana_agregar.title("Agregar Paciente")

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
        ventana_listar = tk.Toplevel(recepcionista_window)
        ventana_listar.title("Lista de Pacientes")

        tree = ttk.Treeview(ventana_listar, columns=("Nombre", "Edad", "Tipo de Sangre", "Alergias", "Peso", "Altura"), show="headings")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Edad", text="Edad")
        tree.heading("Tipo de Sangre", text="Tipo de Sangre")
        tree.heading("Alergias", text="Alergias")
        tree.heading("Peso", text="Peso")
        tree.heading("Altura", text="Altura")

        tree.column("Nombre", width=150, anchor="center")
        tree.column("Edad", width=50, anchor="center")
        tree.column("Tipo de Sangre", width=100, anchor="center")
        tree.column("Alergias", width=150, anchor="center")
        tree.column("Peso", width=50, anchor="center")
        tree.column("Altura", width=50, anchor="center")

        for paciente in Pacientes.Lista_pacientes:
            tree.insert("", "end", values=(paciente.nombre, paciente.edad, paciente.tipo_sangre, paciente.alergias, paciente.peso, paciente.altura))

        tree.pack(expand=True, fill="both")

    def agregar_servicio():
        def guardar_servicio():
            servicio = entry_servicio.get()
            costo = float(entry_costo.get())
            Servicios(servicio, costo)
            Servicios.guardar_servicios()
            messagebox.showinfo("Éxito", "Servicio agregado correctamente")
            ventana_agregar.destroy()

        ventana_agregar = tk.Toplevel(recepcionista_window)
        ventana_agregar.title("Agregar Servicio")

        tk.Label(ventana_agregar, text="Servicio:").grid(row=0, column=0)
        entry_servicio = tk.Entry(ventana_agregar)
        entry_servicio.grid(row=0, column=1)

        tk.Label(ventana_agregar, text="Costo:").grid(row=1, column=0)
        entry_costo = tk.Entry(ventana_agregar)
        entry_costo.grid(row=1, column=1)

        tk.Button(ventana_agregar, text="Guardar", command=guardar_servicio).grid(row=2, column=0, columnspan=2)

    def listar_servicios():
        ventana_listar = tk.Toplevel(recepcionista_window)
        ventana_listar.title("Lista de Servicios")

        tree = ttk.Treeview(ventana_listar, columns=("Servicio", "Costo"), show="headings")
        tree.heading("Servicio", text="Servicio")
        tree.heading("Costo", text="Costo")

        tree.column("Servicio", width=200, anchor="center")
        tree.column("Costo", width=100, anchor="center")

        for servicio in Servicios.Lista_servicios:
            tree.insert("", "end", values=(servicio.servicio, servicio.costo))

        tree.pack(expand=True, fill="both")

    def agregar_doctor():
        def guardar_doctor():
            nombre = entry_nombre.get()
            especialidad = entry_especialidad.get()
            doctor = Doctores(id, nombre, "Doctor", especialidad)
            Doctores.guardar_doctores()
            messagebox.showinfo("Éxito", "Doctor agregado correctamente")
            ventana_agregar.destroy()

        ventana_agregar = tk.Toplevel(recepcionista_window)
        ventana_agregar.title("Agregar Doctor")

        tk.Label(ventana_agregar, text="Nombre:").grid(row=0, column=0)
        entry_nombre = tk.Entry(ventana_agregar)
        entry_nombre.grid(row=0, column=1)

        tk.Label(ventana_agregar, text="Especialidad:").grid(row=1, column=0)
        entry_especialidad = tk.Entry(ventana_agregar)
        entry_especialidad.grid(row=1, column=1)

        tk.Button(ventana_agregar, text="Guardar", command=guardar_doctor).grid(row=2, column=0, columnspan=2)

    def listar_doctores():
        ventana_listar = tk.Toplevel(recepcionista_window)
        ventana_listar.title("Lista de Doctores")

        tree = ttk.Treeview(ventana_listar, columns=("Nombre", "Especialidad"), show="headings")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Especialidad", text="Especialidad")

        tree.column("Nombre", width=150, anchor="center")
        tree.column("Especialidad", width=150, anchor="center")

        for doctor in Doctores.Lista_doctores:
            tree.insert("", "end", values=(doctor.nombre, doctor.especialidad))

        tree.pack(expand=True, fill="both")

    menu_principal = tk.Menu(recepcionista_window)
    recepcionista_window.config(menu=menu_principal)

    menu_pacientes = tk.Menu(menu_principal, tearoff=0)
    menu_pacientes.add_command(label="Agregar Paciente", command=agregar_paciente)
    menu_pacientes.add_command(label="Listar Pacientes", command=listar_pacientes)
    menu_principal.add_cascade(label="Pacientes", menu=menu_pacientes)

    menu_citas = tk.Menu(menu_principal, tearoff=0)
    menu_citas.add_command(label="Agendar Cita", command=agendar_cita)
    menu_citas.add_command(label="Listar Citas", command=listar_citas)
    menu_principal.add_cascade(label="Citas", menu=menu_citas)

    menu_servicios = tk.Menu(menu_principal, tearoff=0)
    menu_servicios.add_command(label="Agregar Servicio", command=agregar_servicio)
    menu_servicios.add_command(label="Listar Servicios", command=listar_servicios)
    menu_principal.add_cascade(label="Servicios", menu=menu_servicios)

    menu_doctores = tk.Menu(menu_principal, tearoff=0)
    menu_doctores.add_command(label="Agregar Doctor", command=agregar_doctor)
    menu_doctores.add_command(label="Listar Doctores", command=listar_doctores)
    menu_principal.add_cascade(label="Doctores", menu=menu_doctores)

    recepcionista_window.mainloop()
ventana_principal()