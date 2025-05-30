import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from backend import *
from datetime import datetime
from PIL import Image, ImageTk

Personas.cargar_usuarios()
Pacientes.cargar_pacientes()
Servicios.cargar_servicios()
Doctores.cargar_doctores()
Citas.cargar_citas()
expedientes = Expediente.cargar_expedientes()

def ventana_principal():
    global root
    root = tk.Tk()
    root.title("Sistema de Consultorio Médico")
    root.geometry("800x600+0+0")
    root.iconbitmap("C://Users//Jaime//Documents//GitHub//Prograavanzada//GUI_tkinter//Serv_medico//medicina.ico")

    imagen_fondo = Image.open("C://Users//Jaime//Documents//GitHub//Prograavanzada//GUI_tkinter//Serv_medico//fondo_inicio.jpg")
    imagen_fondo = imagen_fondo.resize((800, 600))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(root, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    titulo = tk.Label(root, text="Hospital de Programación Avanzada", font=("Arial", 24, "bold"), bg="white", fg="navy")
    titulo.place(relx=0.5, rely=0.1, anchor="center")

    frame_botones = tk.Frame(root, bg="white", bd=5, relief="ridge")
    frame_botones.place(relx=0.5, rely=0.5, anchor="center")

    def abrir_doctor():
        root.destroy()
        ventana_doctor()

    def abrir_recepcionista():
        root.destroy()
        ventana_recepcionista()

    boton_doctor = tk.Button(frame_botones, text="Doctor", command=abrir_doctor, width=20, height=3, font=("Arial", 14, "bold"), bg="lightblue", fg="black")
    boton_doctor.pack(pady=10)

    boton_recepcionista = tk.Button(frame_botones, text="Recepcionista", command=abrir_recepcionista, width=20, height=3, font=("Arial", 14, "bold"), bg="lightgreen", fg="black")
    boton_recepcionista.pack(pady=10)

    root.mainloop()

def ventana_doctor():
    doctor_window = tk.Tk()
    doctor_window.title("Ventana de Doctor")
    doctor_window.geometry("800x600")

    imagen_fondo = Image.open("C://Users//Jaime//Documents//GitHub//Prograavanzada//GUI_tkinter//Serv_medico//fondo_doctor.jpg")
    imagen_fondo = imagen_fondo.resize((800, 600))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(doctor_window, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    def ver_citas_pendientes():
        ventana_citas = tk.Toplevel(doctor_window)
        ventana_citas.title("Citas Pendientes")
        
        # Crear un Treeview para mostrar las citas
        tree = ttk.Treeview(ventana_citas, columns=("Día", "Hora", "Paciente", "Estado"), show="headings")
        tree.heading("Día", text="Día")
        tree.heading("Hora", text="Hora")
        tree.heading("Paciente", text="Paciente")
        tree.heading("Estado", text="Estado")
        tree.column("Día", width=150, anchor="center")
        tree.column("Hora", width=100, anchor="center")
        tree.column("Paciente", width=200, anchor="center")
        tree.column("Estado", width=100, anchor="center")
        tree.pack(pady=10)

        # Llenar el Treeview con las citas pendientes
        for cita in Citas.lista_citas:
            if not cita.Disponibilidad:  # Muestra solo las citas no disponibles (asignadas)
                paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
                estado = "Pendiente"  # Estado inicial
                if hasattr(cita, "estado"):  # Si la cita ya tiene un estado (Atendida/Cancelada)
                    estado = cita.estado
                tree.insert("", "end", values=(cita.dia, cita.hora, paciente_nombre, estado))

        # Función para atender una cita
        def atender_cita():
            seleccion = tree.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione una cita para atender.")
                return
            cita_seleccionada = tree.item(seleccion, "values")
            dia, hora, paciente_nombre, _ = cita_seleccionada

            # Buscar la cita en la lista
            cita = next((c for c in Citas.lista_citas if c.dia == dia and c.hora == hora), None)
            if cita:
                cita.estado = "Atendida"  # Cambiar el estado de la cita
                Citas.guardar_citas()  # Guardar los cambios
                messagebox.showinfo("Éxito", "Cita marcada como Atendida.")
                # Actualizar el Treeview
                tree.item(seleccion, values=(cita.dia, cita.hora, paciente_nombre, "Atendida"))
            else:
                messagebox.showerror("Error", "No se encontró la cita seleccionada.")

        # Función para cancelar una cita
        def cancelar_cita():
            seleccion = tree.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione una cita para cancelar.")
                return
            cita_seleccionada = tree.item(seleccion, "values")
            dia, hora, paciente_nombre, _ = cita_seleccionada

            # Buscar la cita en la lista
            cita = next((c for c in Citas.lista_citas if c.dia == dia and c.hora == hora), None)
            if cita:
                cita.estado = "Cancelada"  # Cambiar el estado de la cita
                Citas.guardar_citas()  # Guardar los cambios
                messagebox.showinfo("Éxito", "Cita marcada como Cancelada.")
                # Actualizar el Treeview
                tree.item(seleccion, values=(cita.dia, cita.hora, paciente_nombre, "Cancelada"))
            else:
                messagebox.showerror("Error", "No se encontró la cita seleccionada.")

        # Botones para atender y cancelar citas
        frame_botones = tk.Frame(ventana_citas)
        frame_botones.pack(pady=10)

        boton_atender = tk.Button(frame_botones, text="Atender Cita", command=atender_cita, width=15, height=2)
        boton_atender.pack(side="left", padx=10)

        boton_cancelar = tk.Button(frame_botones, text="Cancelar Cita", command=cancelar_cita, width=15, height=2)
        boton_cancelar.pack(side="left", padx=10)

    def ver_expediente_paciente():
        def mostrar_expediente():
            paciente_nombre = combo_paciente_expediente.get()
            paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
            if paciente:
                ventana_expediente = tk.Toplevel(doctor_window)
                ventana_expediente.title(f"Expediente de {paciente.nombre}")
                ventana_expediente.geometry("800x600")

                frame_datos = tk.Frame(ventana_expediente)
                frame_datos.pack(pady=10, padx=10, fill="x")

                tk.Label(frame_datos, text="Nombre:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
                tk.Label(frame_datos, text=paciente.nombre, font=("Arial", 12)).grid(row=0, column=1, sticky="w")

                tk.Label(frame_datos, text="Edad:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w")
                tk.Label(frame_datos, text=paciente.edad, font=("Arial", 12)).grid(row=1, column=1, sticky="w")

                tk.Label(frame_datos, text="Tipo de Sangre:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w")
                tk.Label(frame_datos, text=paciente.tipo_sangre, font=("Arial", 12)).grid(row=2, column=1, sticky="w")

                tk.Label(frame_datos, text="Alergias:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w")
                tk.Label(frame_datos, text=paciente.alergias, font=("Arial", 12)).grid(row=3, column=1, sticky="w")

                tk.Label(frame_datos, text="Peso:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w")
                tk.Label(frame_datos, text=f"{paciente.peso} kg", font=("Arial", 12)).grid(row=4, column=1, sticky="w")

                tk.Label(frame_datos, text="Altura:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w")
                tk.Label(frame_datos, text=f"{paciente.altura} cm", font=("Arial", 12)).grid(row=5, column=1, sticky="w")

                frame_citas = tk.Frame(ventana_expediente)
                frame_citas.pack(pady=10, padx=10, fill="both", expand=True)

                tk.Label(frame_citas, text="Citas Anteriores:", font=("Arial", 12, "bold")).pack(anchor="w")

                tree_citas = ttk.Treeview(frame_citas, columns=("Día", "Hora", "Doctor", "Estado"), show="headings")
                tree_citas.heading("Día", text="Día")
                tree_citas.heading("Hora", text="Hora")
                tree_citas.heading("Doctor", text="Doctor")
                tree_citas.heading("Estado", text="Estado")
                tree_citas.column("Día", width=150, anchor="center")
                tree_citas.column("Hora", width=100, anchor="center")
                tree_citas.column("Doctor", width=200, anchor="center")
                tree_citas.column("Estado", width=100, anchor="center")
                tree_citas.pack(fill="both", expand=True)

                for cita in Citas.lista_citas:
                    if cita.paciente and cita.paciente.nombre == paciente.nombre:
                        doctor_nombre = cita.doctor.nombre if cita.doctor else "N/A"
                        tree_citas.insert("", "end", values=(cita.dia, cita.hora, doctor_nombre, cita.estado))

                frame_diagnosticos = tk.Frame(ventana_expediente)
                frame_diagnosticos.pack(pady=10, padx=10, fill="both", expand=True)

                tk.Label(frame_diagnosticos, text="Diagnósticos:", font=("Arial", 12, "bold")).pack(anchor="w")

                tree_diagnosticos = ttk.Treeview(frame_diagnosticos, columns=("Fecha", "Diagnóstico"), show="headings")
                tree_diagnosticos.heading("Fecha", text="Fecha")
                tree_diagnosticos.heading("Diagnóstico", text="Diagnóstico")
                tree_diagnosticos.column("Fecha", width=150, anchor="center")
                tree_diagnosticos.column("Diagnóstico", width=500, anchor="w")
                tree_diagnosticos.pack(fill="both", expand=True)

                expedientes = Expediente.cargar_expedientes()
                if paciente_nombre in expedientes:
                    for registro in expedientes[paciente_nombre]:
                        if "diagnostico" in registro:
                            tree_diagnosticos.insert("", "end", values=(registro["fecha"], registro["diagnostico"]))
                else:
                    tree_diagnosticos.insert("", "end", values=("No hay diagnósticos registrados.", ""))

            else:
                messagebox.showerror("Error", "Paciente no encontrado.")

        ventana_seleccion = tk.Toplevel(doctor_window)
        ventana_seleccion.title("Seleccionar Paciente")
        ventana_seleccion.geometry("300x150")

        tk.Label(ventana_seleccion, text="Seleccione el paciente:", font=("Arial", 12)).pack(pady=10)
        nombres_pacientes = [p.nombre for p in Pacientes.Lista_pacientes]
        combo_paciente_expediente = ttk.Combobox(ventana_seleccion, values=nombres_pacientes, state="readonly", font=("Arial", 12))
        combo_paciente_expediente.pack(pady=10)
        tk.Button(ventana_seleccion, text="Ver Expediente", command=mostrar_expediente, font=("Arial", 12)).pack(pady=10)
            
    def agregar_diagnostico():
        def guardar_diagnostico():
            seleccion = tree.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione una cita para agregar el diagnóstico.")
                return
            cita_seleccionada = tree.item(seleccion, "values")
            dia, hora, paciente_nombre, _ = cita_seleccionada

            cita = next((c for c in Citas.lista_citas if c.dia == dia and c.hora == hora), None)
            if cita:
                diagnostico = entry_diagnostico.get("1.0", tk.END).strip()
                if diagnostico:
                    expedientes = Expediente.cargar_expedientes()
                    if paciente_nombre in expedientes:
                        expedientes[paciente_nombre].append({
                            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "diagnostico": diagnostico,
                            "cita": f"{dia} {hora}"
                        })
                    else:
                        expedientes[paciente_nombre] = [{
                            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "diagnostico": diagnostico,
                            "cita": f"{dia} {hora}"
                        }]
                    Expediente.guardar_expedientes(expedientes)
                    messagebox.showinfo("Éxito", "Diagnóstico agregado correctamente.")
                    ventana_diagnostico.destroy()
                else:
                    messagebox.showerror("Error", "El diagnóstico no puede estar vacío.")
            else:
                messagebox.showerror("Error", "No se encontró la cita seleccionada.")

        ventana_diagnostico = tk.Toplevel(doctor_window)
        ventana_diagnostico.title("Agregar Diagnóstico")

        tree = ttk.Treeview(ventana_diagnostico, columns=("Día", "Hora", "Paciente", "Estado"), show="headings")
        tree.heading("Día", text="Día")
        tree.heading("Hora", text="Hora")
        tree.heading("Paciente", text="Paciente")
        tree.heading("Estado", text="Estado")
        tree.column("Día", width=150, anchor="center")
        tree.column("Hora", width=100, anchor="center")
        tree.column("Paciente", width=200, anchor="center")
        tree.column("Estado", width=100, anchor="center")
        tree.pack(pady=10)

        for cita in Citas.lista_citas:
            if not cita.Disponibilidad:
                paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
                estado = cita.estado
                tree.insert("", "end", values=(cita.dia, cita.hora, paciente_nombre, estado))

        tk.Label(ventana_diagnostico, text="Diagnóstico:").pack(pady=10)
        entry_diagnostico = tk.Text(ventana_diagnostico, width=50, height=10)
        entry_diagnostico.pack(pady=10)
        tk.Button(ventana_diagnostico, text="Guardar Diagnóstico", command=guardar_diagnostico).pack(pady=20)

    def generar_receta():
        def guardar_receta():
            paciente_nombre = combo_paciente_receta.get()
            medicamento = entry_medicamento.get("1.0", tk.END).strip()
            dosis = entry_dosis.get("1.0", tk.END).strip()
            indicaciones = entry_indicaciones.get("1.0", tk.END).strip()
            if paciente_nombre and medicamento and dosis and indicaciones:
                expedientes = Expediente.cargar_expedientes()
                if paciente_nombre in expedientes:
                    expedientes[paciente_nombre].append({
                        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "tipo": "receta",
                        "medicamento": medicamento,
                        "dosis": dosis,
                        "indicaciones": indicaciones
                    })
                else:
                    expedientes[paciente_nombre] = [{
                        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "tipo": "receta",
                        "medicamento": medicamento,
                        "dosis": dosis,
                        "indicaciones": indicaciones
                    }]
                Expediente.guardar_expedientes(expedientes)
                messagebox.showinfo("Éxito", "Receta guardada correctamente.")
                ventana_receta.destroy()
            else:
                messagebox.showerror("Error", "Complete todos los campos.")

        ventana_receta = tk.Toplevel(doctor_window)
        ventana_receta.title("Generar Receta")
        tk.Label(ventana_receta, text="Seleccione el paciente:").pack(pady=10)
        nombres_pacientes = [p.nombre for p in Pacientes.Lista_pacientes]
        combo_paciente_receta = ttk.Combobox(ventana_receta, values=nombres_pacientes, state="readonly")
        combo_paciente_receta.pack(pady=10)
        tk.Label(ventana_receta, text="Medicamento:").pack(pady=10)
        entry_medicamento = tk.Text(ventana_receta, width=50, height=3)
        entry_medicamento.pack(pady=10)
        tk.Label(ventana_receta, text="Dosis:").pack(pady=10)
        entry_dosis = tk.Text(ventana_receta, width=50, height=3)
        entry_dosis.pack(pady=10)
        tk.Label(ventana_receta, text="Indicaciones:").pack(pady=10)
        entry_indicaciones = tk.Text(ventana_receta, width=50, height=5)
        entry_indicaciones.pack(pady=10)
        tk.Button(ventana_receta, text="Guardar Receta", command=guardar_receta).pack(pady=20)

    # Botones principales
    boton_ver_citas = tk.Button(doctor_window, text="Ver Citas Pendientes", command=ver_citas_pendientes, width=20, height=3)
    boton_ver_citas.place(x=50, y=50)

    boton_ver_expediente = tk.Button(doctor_window, text="Ver Expediente", command=ver_expediente_paciente, width=20, height=3)
    boton_ver_expediente.place(x=50, y=150)

    boton_agregar_diagnostico = tk.Button(doctor_window, text="Agregar Diagnóstico", command=agregar_diagnostico, width=20, height=3)
    boton_agregar_diagnostico.place(x=50, y=250)

    boton_generar_receta = tk.Button(doctor_window, text="Generar Receta", command=generar_receta, width=20, height=3)
    boton_generar_receta.place(x=50, y=350)


    def on_closing():
        doctor_window.destroy()

    doctor_window.protocol("WM_DELETE_WINDOW", on_closing)
    doctor_window.mainloop()


def ventana_recepcionista():
    recepcionista_window = tk.Tk()
    recepcionista_window.title("Ventana de Recepcionista")
    recepcionista_window.geometry("800x600")

    imagen_fondo = Image.open("C://Users//Jaime//Documents//GitHub//Prograavanzada//GUI_tkinter//Serv_medico//fondo.jpg")
    imagen_fondo = imagen_fondo.resize((800, 600))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(recepcionista_window, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    def agendar_cita():
        def guardar_cita():
            cita_dia = cal.get_date()
            cita_hora = combo_hora.get()
            paciente_nombre = combo_paciente.get()
            doctor_nombre = combo_doctor.get()
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
        tk.Label(ventana_agendar, text="Seleccione el paciente:").pack(pady=10)
        nombres_pacientes = [p.nombre for p in Pacientes.Lista_pacientes]
        combo_paciente = ttk.Combobox(ventana_agendar, values=nombres_pacientes, state="readonly")
        combo_paciente.pack(pady=10)
        tk.Label(ventana_agendar, text="Seleccione el doctor:").pack(pady=10)
        nombres_doctores = [d.nombre for d in Doctores.Lista_doctores]
        combo_doctor = ttk.Combobox(ventana_agendar, values=nombres_doctores, state="readonly")
        combo_doctor.pack(pady=10)
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
            if not cita.Disponibilidad:
                paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
                doctor_nombre = cita.doctor.nombre if cita.doctor else "N/A"
                tree.insert("", "end", values=(cita.dia, cita.hora, paciente_nombre, doctor_nombre))
        tree.pack(pady=10)

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
            id = len(Doctores.Lista_doctores) + 1
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

    def cancelar_cita():
        def confirmar_cancelacion():
            seleccion = tree.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione una cita para cancelar.")
                return
            cita_seleccionada = tree.item(seleccion, "values")
            dia, hora, paciente_nombre, doctor_nombre = cita_seleccionada
            cita = next((c for c in Citas.lista_citas if c.dia == dia and c.hora == hora), None)
            if cita:
                cita.Disponibilidad = True
                cita.paciente = None
                cita.doctor = None
                Citas.guardar_citas()
                messagebox.showinfo("Éxito", "Cita cancelada correctamente.")
                ventana_cancelar.destroy()
            else:
                messagebox.showerror("Error", "No se encontró la cita seleccionada.")

        ventana_cancelar = tk.Toplevel(recepcionista_window)
        ventana_cancelar.title("Cancelar Cita")
        tree = ttk.Treeview(ventana_cancelar, columns=("Día", "Hora", "Paciente", "Doctor"), show="headings")
        tree.heading("Día", text="Día")
        tree.heading("Hora", text="Hora")
        tree.heading("Paciente", text="Paciente")
        tree.heading("Doctor", text="Doctor")
        tree.column("Día", width=100, anchor="center")
        tree.column("Hora", width=80, anchor="center")
        tree.column("Paciente", width=150, anchor="center")
        tree.column("Doctor", width=150, anchor="center")
        for cita in Citas.lista_citas:
            if not cita.Disponibilidad:
                paciente_nombre = cita.paciente.nombre if cita.paciente else "N/A"
                doctor_nombre = cita.doctor.nombre if cita.doctor else "N/A"
                tree.insert("", "end", values=(cita.dia, cita.hora, paciente_nombre, doctor_nombre))
        tree.pack(pady=10)
        tk.Button(ventana_cancelar, text="Cancelar Cita", command=confirmar_cancelacion).pack(pady=10)

    def ver_expediente():
        def mostrar_expediente():
            paciente_nombre = combo_paciente_expediente.get()
            paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
            if paciente:
                ventana_expediente = tk.Toplevel(recepcionista_window)
                ventana_expediente.title(f"Expediente de {paciente.nombre}")
                tk.Label(ventana_expediente, text=f"Nombre: {paciente.nombre}").pack(pady=5)
                tk.Label(ventana_expediente, text=f"Edad: {paciente.edad}").pack(pady=5)
                tk.Label(ventana_expediente, text=f"Tipo de Sangre: {paciente.tipo_sangre}").pack(pady=5)
                tk.Label(ventana_expediente, text=f"Alergias: {paciente.alergias}").pack(pady=5)
                tk.Label(ventana_expediente, text=f"Peso: {paciente.peso} kg").pack(pady=5)
                tk.Label(ventana_expediente, text=f"Altura: {paciente.altura} cm").pack(pady=5)
                tk.Label(ventana_expediente, text="Citas anteriores:").pack(pady=10)
                for cita in Citas.lista_citas:
                    if cita.paciente and cita.paciente.nombre == paciente.nombre:
                        tk.Label(ventana_expediente, text=f"{cita.dia} {cita.hora} - Dr. {cita.doctor.nombre if cita.doctor else 'N/A'}").pack(pady=5)
            else:
                messagebox.showerror("Error", "Paciente no encontrado.")

        ventana_seleccion = tk.Toplevel(recepcionista_window)
        ventana_seleccion.title("Seleccionar Paciente")
        tk.Label(ventana_seleccion, text="Seleccione el paciente:").pack(pady=10)
        nombres_pacientes = [p.nombre for p in Pacientes.Lista_pacientes]
        combo_paciente_expediente = ttk.Combobox(ventana_seleccion, values=nombres_pacientes, state="readonly")
        combo_paciente_expediente.pack(pady=10)
        tk.Button(ventana_seleccion, text="Ver Expediente", command=mostrar_expediente).pack(pady=20)

    def generar_recibo():
        def crear_recibo():
            paciente_nombre = combo_paciente_recibo.get()
            servicio_nombre = combo_servicio_recibo.get()
            costo = next((s.costo for s in Servicios.Lista_servicios if s.servicio == servicio_nombre), 0)
            if paciente_nombre and servicio_nombre:
                ventana_recibo = tk.Toplevel(recepcionista_window)
                ventana_recibo.title("Recibo")
                tk.Label(ventana_recibo, text="Recibo Médico", font=("Arial", 16)).pack(pady=10)
                tk.Label(ventana_recibo, text=f"Paciente: {paciente_nombre}").pack(pady=5)
                tk.Label(ventana_recibo, text=f"Servicio: {servicio_nombre}").pack(pady=5)
                tk.Label(ventana_recibo, text=f"Costo: ${costo:.2f}").pack(pady=5)
                tk.Label(ventana_recibo, text=f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}").pack(pady=10)
            else:
                messagebox.showerror("Error", "Complete todos los campos.")

        ventana_recibo = tk.Toplevel(recepcionista_window)
        ventana_recibo.title("Generar Recibo")
        tk.Label(ventana_recibo, text="Seleccione el paciente:").pack(pady=10)
        nombres_pacientes = [p.nombre for p in Pacientes.Lista_pacientes]
        combo_paciente_recibo = ttk.Combobox(ventana_recibo, values=nombres_pacientes, state="readonly")
        combo_paciente_recibo.pack(pady=10)
        tk.Label(ventana_recibo, text="Seleccione el servicio:").pack(pady=10)
        nombres_servicios = [s.servicio for s in Servicios.Lista_servicios]
        combo_servicio_recibo = ttk.Combobox(ventana_recibo, values=nombres_servicios, state="readonly")
        combo_servicio_recibo.pack(pady=10)
        tk.Button(ventana_recibo, text="Generar Recibo", command=crear_recibo).pack(pady=20)


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

    boton_agendar_cita = tk.Button(recepcionista_window, text="Agendar Cita", command=agendar_cita, width=20, height=3)
    boton_agendar_cita.place(x=50, y=50)

    boton_cancelar_cita = tk.Button(recepcionista_window, text="Cancelar Cita", command=cancelar_cita, width=20, height=3)
    boton_cancelar_cita.place(x=50, y=150)

    boton_ver_expediente = tk.Button(recepcionista_window, text="Ver Expediente", command=ver_expediente, width=20, height=3)
    boton_ver_expediente.place(x=50, y=250)

    boton_generar_recibo = tk.Button(recepcionista_window, text="Generar Recibo", command=generar_recibo, width=20, height=3)
    boton_generar_recibo.place(x=50, y=350)

    menu_principal = tk.Menu(recepcionista_window)
    recepcionista_window.config(menu=menu_principal)

    menu_pacientes = tk.Menu(menu_principal, tearoff=0)
    menu_pacientes.add_command(label="Agregar Paciente", command=agregar_paciente)
    menu_pacientes.add_command(label="Listar Pacientes", command=listar_pacientes)
    menu_principal.add_cascade(label="Pacientes", menu=menu_pacientes)

    menu_citas = tk.Menu(menu_principal, tearoff=0)
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

    

    def on_closing():
        Doctores.guardar_doctores()
        Pacientes.guardar_pacientes()
        Citas.guardar_citas()
        Servicios.guardar_servicios()
        recepcionista_window.destroy()

    recepcionista_window.protocol("WM_DELETE_WINDOW", on_closing)
    recepcionista_window.mainloop()

ventana_principal()



#Instalar la libreria pip install pyinstaller
#crear autoejecutable
#poner en su directorio actual
#correr pyinstaller --onefile --windowed frontend.py