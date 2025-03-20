import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def meter_datos():
    ventana_datos = ctk.CTkToplevel()
    ventana_datos.title("Ingresar Datos del Paciente")
    ventana_datos.geometry("400x500")
    ventana_datos.grab_set()  # Enfocar esta ventana

    campos = [
        "Nombre", "Teléfono", "Género", "Embarazos", "Glucosa", 
        "PresionSanguinea", "GrosorPiel", "Insulina", "IMC", "Edad"
    ]

    entries = {}

    for i, campo in enumerate(campos):
        label = ctk.CTkLabel(ventana_datos, text=f"{campo}:")
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        entry = ctk.CTkEntry(ventana_datos)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[campo] = entry

    def guardar_datos():
        datos = {campo: entries[campo].get() for campo in campos}
        messagebox.showinfo("Datos Guardados", "Datos del paciente guardados correctamente.")
        ventana_datos.destroy()

    btn_guardar = ctk.CTkButton(ventana_datos, text="Guardar", command=guardar_datos)
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, pady=10)

def visualizar_expediente():
    ventana_expediente = ctk.CTkToplevel()
    ventana_expediente.title("Expediente del Paciente")
    ventana_expediente.geometry("400x300")
    ventana_expediente.grab_set()  # Enfocar esta ventana

    texto_expediente = ctk.CTkTextbox(ventana_expediente, width=350, height=250)
    texto_expediente.pack(pady=20)

    datos_ejemplo = """
    Nombre: Juan Pérez
    Teléfono: 555-1234
    Género: Masculino
    Embarazos: 0
    Glucosa: 120
    PresionSanguinea: 80
    GrosorPiel: 25
    Insulina: 150
    IMC: 28.5
    Edad: 35
    """
    texto_expediente.insert("1.0", datos_ejemplo)
    texto_expediente.configure(state="disabled")

def mostrar_analisis():
    messagebox.showinfo("Análisis", "Esta funcionalidad estará disponible pronto.")

ventana_principal = ctk.CTk()
ventana_principal.title("Sistema de Pacientes")
ventana_principal.geometry("400x300")

btn_meter_datos = ctk.CTkButton(ventana_principal, text="Meter Datos de Paciente", command=meter_datos)
btn_meter_datos.pack(pady=10)

btn_visualizar_expediente = ctk.CTkButton(ventana_principal, text="Visualizar Expediente del Paciente", command=visualizar_expediente)
btn_visualizar_expediente.pack(pady=10)

btn_mostrar_analisis = ctk.CTkButton(ventana_principal, text="Mostrar Análisis", command=mostrar_analisis)
btn_mostrar_analisis.pack(pady=10)

ventana_principal.mainloop()