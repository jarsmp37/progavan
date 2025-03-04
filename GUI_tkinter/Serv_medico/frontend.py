import tkinter as tk
from tkinter import messagebox, ttk
from backend import *

Personas.cargar_usuarios()
Pacientes.cargar_pacientes()
Citas.cargar_citas()
Servicios.cargar_servicios()
expedientes = Expediente.cargar_expedientes()

def ventana_principal():
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

def ventana_doctor():
    doctor_window = tk.Tk()
    doctor_window.title("Ventana de Doctor")
    doctor_window.geometry("800x600")

    def crear_receta():
        paciente_nombre = entry_paciente_receta.get()
        medicamentos = entry_medicamentos.get()
        instrucciones = entry_instrucciones.get()
        paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
        if paciente:
            doctor = Doctores(1, "Dr. Ejemplo", "Doctor", "General")
            doctor.Crear_receta(paciente, medicamentos, instrucciones)
            messagebox.showinfo("Éxito", "Receta creada correctamente")
        else:
            messagebox.showerror("Error", "Paciente no encontrado")

    def realizar_consulta():
        cita_dia = entry_cita_dia.get()
        cita_hora = entry_cita_hora.get()
        cita = next((c for c in Citas.lista_citas if c.dia == cita_dia and c.hora == cita_hora), None)
        if cita:
            doctor = Doctores(1, "Dr. Ejemplo", "Doctor", "General")
            doctor.Realizar_Consulta(cita)
            messagebox.showinfo("Éxito", "Consulta realizada correctamente")
        else:
            messagebox.showerror("Error", "Cita no encontrada")

    def verificar_expediente():
        paciente_nombre = entry_paciente_expediente.get()
        paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
        if paciente:
            doctor = Doctores(1, "Dr. Ejemplo", "Doctor", "General")
            doctor.verificar_expediente(paciente, expedientes)
            messagebox.showinfo("Éxito", "Expediente verificado")
        else:
            messagebox.showerror("Error", "Paciente no encontrado")

    tk.Label(doctor_window, text="Crear Receta").pack(pady=10)
    tk.Label(doctor_window, text="Paciente:").pack()
    entry_paciente_receta = tk.Entry(doctor_window)
    entry_paciente_receta.pack()
    tk.Label(doctor_window, text="Medicamentos:").pack()
    entry_medicamentos = tk.Entry(doctor_window)
    entry_medicamentos.pack()
    tk.Label(doctor_window, text="Instrucciones:").pack()
    entry_instrucciones = tk.Entry(doctor_window)
    entry_instrucciones.pack()
    tk.Button(doctor_window, text="Crear Receta", command=crear_receta).pack(pady=10)

    tk.Label(doctor_window, text="Realizar Consulta").pack(pady=10)
    tk.Label(doctor_window, text="Día de la cita:").pack()
    entry_cita_dia = tk.Entry(doctor_window)
    entry_cita_dia.pack()
    tk.Label(doctor_window, text="Hora de la cita:").pack()
    entry_cita_hora = tk.Entry(doctor_window)
    entry_cita_hora.pack()
    tk.Button(doctor_window, text="Realizar Consulta", command=realizar_consulta).pack(pady=10)

    tk.Label(doctor_window, text="Verificar Expediente").pack(pady=10)
    tk.Label(doctor_window, text="Paciente:").pack()
    entry_paciente_expediente = tk.Entry(doctor_window)
    entry_paciente_expediente.pack()
    tk.Button(doctor_window, text="Verificar Expediente", command=verificar_expediente).pack(pady=10)

    menu_principal = tk.Menu(doctor_window)
    doctor_window.config(menu=menu_principal)

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

    doctor_window.mainloop()

def ventana_recepcionista():
    recepcionista_window = tk.Tk()
    recepcionista_window.title("Ventana de Recepcionista")
    recepcionista_window.geometry("800x600")

    def agendar_cita():
        cita_dia = entry_cita_dia.get()
        cita_hora = entry_cita_hora.get()
        paciente_nombre = entry_paciente_cita.get()
        doctor_nombre = entry_doctor_cita.get()
        cita = next((c for c in Citas.lista_citas if c.dia == cita_dia and c.hora == cita_hora), None)
        paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
        doctor = next((d for d in Personas.Lista_personas if d.nombre == doctor_nombre and d.rol == "Doctor"), None)
        if cita and paciente and doctor:
            recepcionista = Recepcionista(2, "Recepcionista Ejemplo", "Recepcionista")
            recepcionista.agendar_cita(cita, paciente, doctor)
            messagebox.showinfo("Éxito", "Cita agendada correctamente")
        else:
            messagebox.showerror("Error", "Datos incorrectos o no encontrados")

    def cancelar_cita():
        cita_dia = entry_cita_dia_cancelar.get()
        cita_hora = entry_cita_hora_cancelar.get()
        cita = next((c for c in Citas.lista_citas if c.dia == cita_dia and c.hora == cita_hora), None)
        if cita:
            recepcionista = Recepcionista(2, "Recepcionista Ejemplo", "Recepcionista")
            recepcionista.cancelar_cita(cita)
            messagebox.showinfo("Éxito", "Cita cancelada correctamente")
        else:
            messagebox.showerror("Error", "Cita no encontrada")

    tk.Label(recepcionista_window, text="Agendar Cita").pack(pady=10)
    tk.Label(recepcionista_window, text="Día de la cita:").pack()
    entry_cita_dia = tk.Entry(recepcionista_window)
    entry_cita_dia.pack()
    tk.Label(recepcionista_window, text="Hora de la cita:").pack()
    entry_cita_hora = tk.Entry(recepcionista_window)
    entry_cita_hora.pack()
    tk.Label(recepcionista_window, text="Paciente:").pack()
    entry_paciente_cita = tk.Entry(recepcionista_window)
    entry_paciente_cita.pack()
    tk.Label(recepcionista_window, text="Doctor:").pack()
    entry_doctor_cita = tk.Entry(recepcionista_window)
    entry_doctor_cita.pack()
    tk.Button(recepcionista_window, text="Agendar Cita", command=agendar_cita).pack(pady=10)

    tk.Label(recepcionista_window, text="Cancelar Cita").pack(pady=10)
    tk.Label(recepcionista_window, text="Día de la cita:").pack()
    entry_cita_dia_cancelar = tk.Entry(recepcionista_window)
    entry_cita_dia_cancelar.pack()
    tk.Label(recepcionista_window, text="Hora de la cita:").pack()
    entry_cita_hora_cancelar = tk.Entry(recepcionista_window)
    entry_cita_hora_cancelar.pack()
    tk.Button(recepcionista_window, text="Cancelar Cita", command=cancelar_cita).pack(pady=10)

    menu_principal = tk.Menu(recepcionista_window)
    recepcionista_window.config(menu=menu_principal)

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

    recepcionista_window.mainloop()

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

ventana_principal()