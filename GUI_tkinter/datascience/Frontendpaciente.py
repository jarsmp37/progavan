import os
import customtkinter as ctk
from tkinter import ttk,messagebox
from Backendpaciente import SistemaPacientes, Paciente
from Analisis import *
from modelo_logistico import *


os.chdir(r"C:\Users\Jaime\Documents\GitHub\Prograavanzada\GUI_tkinter\datascience")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

sistema = SistemaPacientes("pacientes.csv")
# Entrenar el modelo de regresión logística
modelo = entrenar_modelo()



def meter_datos():
    ventana_datos = ctk.CTkToplevel()
    ventana_datos.title("Ingresar Datos del Paciente")
    ventana_datos.geometry("400x500")
    ventana_datos.grab_set()

    campos = [
        "Nombre", "Teléfono", "Embarazos", "Glucosa", 
        "PresionSanguinea", "GrosorPiel", "Insulina", "IMC", "Edad"
    ]

    entries = {}

    label_genero = ctk.CTkLabel(ventana_datos, text="Género:")
    label_genero.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    genero_combobox = ctk.CTkComboBox(ventana_datos, values=["Hombre", "Mujer"])
    genero_combobox.grid(row=2, column=1, padx=10, pady=5)
    genero_combobox.set("Hombre")

    for i, campo in enumerate(campos):
        label = ctk.CTkLabel(ventana_datos, text=f"{campo}:")
        label.grid(row=i + 3, column=0, padx=10, pady=5, sticky="e")

        entry = ctk.CTkEntry(ventana_datos)
        entry.grid(row=i + 3, column=1, padx=10, pady=5)
        entries[campo] = entry

    def guardar_datos():
        try:
            datos = {campo: entries[campo].get() for campo in campos}
            genero = genero_combobox.get()

            paciente = Paciente(
                datos["Nombre"], datos["Teléfono"], genero, int(datos["Embarazos"]),
                int(datos["Glucosa"]), int(datos["PresionSanguinea"]), int(datos["GrosorPiel"]),
                int(datos["Insulina"]), float(datos["IMC"]), int(datos["Edad"])
            )

            sistema.guardar_paciente(paciente)
            messagebox.showinfo("Datos Guardados", "Datos del paciente guardados correctamente.")
            ventana_datos.destroy()
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    btn_guardar = ctk.CTkButton(ventana_datos, text="Guardar", command=guardar_datos)
    btn_guardar.grid(row=len(campos) + 4, column=0, columnspan=2, pady=10)

def visualizar_expediente():
    ventana_expediente = ctk.CTkToplevel()
    ventana_expediente.title("Expediente del Paciente")
    ventana_expediente.geometry("600x400")
    ventana_expediente.grab_set()

    frame = ctk.CTkFrame(ventana_expediente)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=("Nombre"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    pacientes = sistema.obtener_pacientes()
    for paciente in pacientes:
        tree.insert("", "end", values=(paciente.nombre,))

    def ver_paciente():
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un paciente.")
            return

        nombre_paciente = tree.item(seleccion[0], "values")[0]
        paciente = next((p for p in pacientes if p.nombre == nombre_paciente), None)

        if paciente:
            ventana_detalles = ctk.CTkToplevel()
            ventana_detalles.title(f"Detalles de {paciente.nombre}")
            ventana_detalles.geometry("300x500")
            ventana_detalles.grab_set()

            frame = ctk.CTkFrame(ventana_detalles)
            frame.pack(fill="both", expand=True, padx=20, pady=20)

            detalles = paciente.to_dict()
            for i, (k, v) in enumerate(detalles.items()):
                label_titulo = ctk.CTkLabel(frame, text=f"{k}:", font=("Arial", 14, "bold"))
                label_titulo.grid(row=i, column=0, padx=10, pady=5, sticky="e")

                label_valor = ctk.CTkLabel(frame, text=f"{v}", font=("Arial", 14))
                label_valor.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            btn_cerrar = ctk.CTkButton(frame, text="Cerrar", command=ventana_detalles.destroy)
            btn_cerrar.grid(row=len(detalles), column=0, columnspan=2, pady=20)

            global paciente_seleccionado
            paciente_seleccionado = paciente

    btn_ver = ctk.CTkButton(frame, text="Ver", command=ver_paciente)
    btn_ver.pack(pady=10)




def mostrar_analisis():
    if 'paciente_seleccionado' not in globals():
        messagebox.showwarning("Advertencia", "Primero selecciona un paciente en 'Visualizar Expediente'.")
        return

    ventana_analisis = ctk.CTkToplevel()
    ventana_analisis.title("Análisis de Datos")
    ventana_analisis.geometry("400x400")
    ventana_analisis.grab_set()

    btn_embarazos = ctk.CTkButton(ventana_analisis, text="Embarazos", command=lambda: grafico_embarazos(df, paciente_seleccionado.embarazos))
    btn_embarazos.pack(pady=5)

    btn_glucosa = ctk.CTkButton(ventana_analisis, text="Glucosa", command=lambda: grafico_glucosa(df, paciente_seleccionado.glucosa))
    btn_glucosa.pack(pady=5)

    btn_presion = ctk.CTkButton(ventana_analisis, text="Presión Sanguínea", command=lambda: grafico_presion_sanguinea(df, paciente_seleccionado.presion_sanguinea))
    btn_presion.pack(pady=5)

    btn_grosor_piel = ctk.CTkButton(ventana_analisis, text="Grosor de Piel", command=lambda: grafico_grosor_piel(df, paciente_seleccionado.grosor_piel))
    btn_grosor_piel.pack(pady=5)

    btn_insulina = ctk.CTkButton(ventana_analisis, text="Insulina", command=lambda: grafico_insulina(df, paciente_seleccionado.insulina))
    btn_insulina.pack(pady=5)

    btn_imc = ctk.CTkButton(ventana_analisis, text="IMC", command=lambda: grafico_imc(df, paciente_seleccionado.imc))
    btn_imc.pack(pady=5)

    btn_edad = ctk.CTkButton(ventana_analisis, text="Edad", command=lambda: grafico_edad(df, paciente_seleccionado.edad))
    btn_edad.pack(pady=5)

def generar_prediccion():
    if 'paciente_seleccionado' not in globals():
        messagebox.showwarning("Advertencia", "Primero selecciona un paciente en 'Visualizar Expediente'.")
        return

    glucosa = paciente_seleccionado.glucosa

    diagnostico = predecir_diabetes(modelo, glucosa)

    messagebox.showinfo("Predicción de Diabetes", f"Paciente: {paciente_seleccionado.nombre}\nDiagnóstico: {diagnostico}")

ventana_principal = ctk.CTk()
ventana_principal.title("Sistema de Pacientes")
ventana_principal.geometry("400x300")

btn_meter_datos = ctk.CTkButton(ventana_principal, text="Meter Datos de Paciente", command=meter_datos)
btn_meter_datos.pack(pady=10)

btn_visualizar_expediente = ctk.CTkButton(ventana_principal, text="Visualizar Expediente del Paciente", command=visualizar_expediente)
btn_visualizar_expediente.pack(pady=10)

btn_mostrar_analisis = ctk.CTkButton(ventana_principal, text="Mostrar Análisis", command=mostrar_analisis)
btn_mostrar_analisis.pack(pady=10)

btn_generar_prediccion = ctk.CTkButton(ventana_principal, text="Generar Predicción Logística", command=generar_prediccion)
btn_generar_prediccion.pack(pady=10)

ventana_principal.mainloop()