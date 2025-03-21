import customtkinter as ctk
from tkinter import ttk
from backend import Reservacion, ReservacionManager
from tkcalendar import Calendar
from datetime import datetime

manager = ReservacionManager()

def abrir_ventana_reservar():
    ventana_reservar = ctk.CTkToplevel(root)
    ventana_reservar.title("Reservar")
    ventana_reservar.geometry("1000x600")
    ventana_reservar.geometry("+0+0") 
    ventana_reservar.lift()
    ventana_reservar.grab_set()

    ctk.CTkLabel(ventana_reservar, text="Nombre del Huésped:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(ventana_reservar)
    entry_nombre.pack(pady=5)

    frame_calendarios = ctk.CTkFrame(ventana_reservar)
    frame_calendarios.pack(pady=10)

    ctk.CTkLabel(frame_calendarios, text="Fecha de Entrada:").grid(row=0, column=0, padx=10)
    cal_fecha_entrada = Calendar(frame_calendarios, date_pattern="dd/mm/yyyy")
    cal_fecha_entrada.grid(row=1, column=0, padx=10)

    ctk.CTkLabel(frame_calendarios, text="Fecha de Salida:").grid(row=0, column=1, padx=10)
    cal_fecha_salida = Calendar(frame_calendarios, date_pattern="dd/mm/yyyy")
    cal_fecha_salida.grid(row=1, column=1, padx=10)

    ctk.CTkLabel(ventana_reservar, text="Solicitudes Especiales:").pack(pady=5)
    solicitudes = [
        "Cuna para bebé",
        "Comida vegetariana",
        "Habitación con vista al mar",
        "Transporte al aeropuerto"
    ]
    checkboxes = {}
    for solicitud in solicitudes:
        checkboxes[solicitud] = ctk.CTkCheckBox(ventana_reservar, text=solicitud)
        checkboxes[solicitud].pack(pady=2)

    def guardar_reservacion():
        nombre = entry_nombre.get()
        fecha_entrada = cal_fecha_entrada.get_date()
        fecha_salida = cal_fecha_salida.get_date()
        fecha_actual = datetime.now().date()
        fecha_entrada = datetime.strptime(fecha_entrada, "%d/%m/%Y").date()
        fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y").date()
        dias_antelacion = (fecha_entrada - fecha_actual).days
        solicitudes_especiales = [solicitud for solicitud, checkbox in checkboxes.items() if checkbox.get() == 1]
        num_solicitudes = len(solicitudes_especiales)
        huesped_repetido = manager.es_huesped_repetido(nombre)
        reservacion = Reservacion(nombre, dias_antelacion, ", ".join(solicitudes_especiales), fecha_entrada.strftime("%d/%m/%Y"), fecha_salida.strftime("%d/%m/%Y"), huesped_repetido)
        manager.guardar_reservacion(reservacion)
        print("Reservación guardada exitosamente.")
        ventana_reservar.destroy()

    ctk.CTkButton(ventana_reservar, text="Hacer Reservación", command=guardar_reservacion).pack(pady=20)

def abrir_ventana_ver_reservacion():
    ventana_ver = ctk.CTkToplevel(root)
    ventana_ver.title("Ver Reservaciones")
    ventana_ver.geometry("800x400")
    ventana_ver.lift()
    ventana_ver.grab_set()

    columns = ("Nombre", "Fecha Entrada", "Fecha Salida")
    tree = ttk.Treeview(ventana_ver, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    reservaciones = manager.obtener_reservaciones()
    for reservacion in reservaciones:
        tree.insert("", "end", values=(
            reservacion["Nombre"],
            reservacion["Fecha_Entrada"],
            reservacion["Fecha_Salida"]
        ))

    def mostrar_detalles():
    
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            nombre = item["values"][0]
            reservacion = next((r for r in reservaciones if r["Nombre"] == nombre), None)
            if reservacion:
                ventana_detalles = ctk.CTkToplevel(ventana_ver)
                ventana_detalles.title("Detalles de la Reservación")
                ventana_detalles.geometry("800x600+0+0")
                ventana_detalles.lift()
                ventana_detalles.grab_set()

                # Frame principal para organizar los elementos
                frame_principal = ctk.CTkFrame(ventana_detalles)
                frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

                # Frame para el calendario y las etiquetas de fechas
                frame_calendario = ctk.CTkFrame(frame_principal)
                frame_calendario.pack(fill="x", pady=10)

                # Calendario
                cal_detalles = Calendar(frame_calendario, date_pattern="dd/mm/yyyy")
                cal_detalles.pack(side="left", padx=10)

                # Frame para las etiquetas de fechas
                frame_fechas = ctk.CTkFrame(frame_calendario)
                frame_fechas.pack(side="left", padx=10)

                ctk.CTkLabel(frame_fechas, text=f"Fecha de Entrada: {reservacion['Fecha_Entrada']}", font=("Arial", 14)).pack(pady=5)
                ctk.CTkLabel(frame_fechas, text=f"Fecha de Salida: {reservacion['Fecha_Salida']}", font=("Arial", 14)).pack(pady=5)

                # Colorear fechas de entrada y salida
                fecha_entrada = datetime.strptime(reservacion["Fecha_Entrada"], "%d/%m/%Y").date()
                fecha_salida = datetime.strptime(reservacion["Fecha_Salida"], "%d/%m/%Y").date()

                cal_detalles.calevent_create(fecha_entrada, "Entrada", "entrada")
                cal_detalles.calevent_create(fecha_salida, "Salida", "salida")
                cal_detalles.tag_config("entrada", background="green", foreground="white")
                cal_detalles.tag_config("salida", background="red", foreground="white")

                # Frame para los detalles adicionales
                frame_detalles = ctk.CTkFrame(frame_principal)
                frame_detalles.pack(fill="x", pady=10)

                ctk.CTkLabel(frame_detalles, text=f"Nombre: {reservacion['Nombre']}", font=("Arial", 14)).pack(pady=5)

                ctk.CTkLabel(frame_detalles, text="Servicios Seleccionados:", font=("Arial", 14)).pack(pady=5)
                servicios = reservacion["Solicitudes_Especiales"].split(", ")
                for servicio in servicios:
                    ctk.CTkLabel(frame_detalles, text=f"- {servicio}", font=("Arial", 12)).pack()

                # Detalles adicionales (las 4 variables que necesitas)
                ctk.CTkLabel(frame_detalles, text="Datos Adicionales:", font=("Arial", 14)).pack(pady=10)
                ctk.CTkLabel(frame_detalles, text=f"Días de Antelación: {reservacion['Dias_Antelacion']}", font=("Arial", 12)).pack()
                ctk.CTkLabel(frame_detalles, text=f"Solicitudes Especiales: {len(servicios)}", font=("Arial", 12)).pack()
                
                # Mes de llegada en número
                mes_llegada = datetime.strptime(reservacion["Fecha_Entrada"], "%d/%m/%Y").month
                ctk.CTkLabel(frame_detalles, text=f"Mes de Llegada: {mes_llegada}", font=("Arial", 12)).pack()
                
                # Huésped repetido (0 o 1)
                huesped_repetido = 1 if reservacion["Huesped_Repetido"] == "True" else 0
                ctk.CTkLabel(frame_detalles, text=f"Huésped Repetido: {huesped_repetido}", font=("Arial", 12)).pack()
        else:
            print("Selecciona una reservación para ver los detalles.")

    ctk.CTkButton(ventana_ver, text="Mostrar Detalles", command=mostrar_detalles).pack(pady=20)

root = ctk.CTk()
root.title("Sistema de Reservaciones")
root.geometry("600x400")

ctk.CTkButton(root, text="Reservar", command=abrir_ventana_reservar).pack(pady=20)
ctk.CTkButton(root, text="Ver Reservación", command=abrir_ventana_ver_reservacion).pack(pady=20)

root.mainloop()