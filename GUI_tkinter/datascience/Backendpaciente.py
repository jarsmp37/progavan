import csv
import os
os.chdir(r"C:\Users\Jaime\Documents\GitHub\Prograavanzada\GUI_tkinter\datascience")

class Paciente:
    def __init__(self, nombre, telefono, genero, embarazos, glucosa, presion_sanguinea, grosor_piel, insulina, imc, edad):
        self.nombre = nombre
        self.telefono = telefono
        self.genero = genero
        self.embarazos = embarazos
        self.glucosa = glucosa
        self.presion_sanguinea = presion_sanguinea
        self.grosor_piel = grosor_piel
        self.insulina = insulina
        self.imc = imc
        self.edad = edad

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Teléfono": self.telefono,
            "Género": self.genero,
            "Embarazos": self.embarazos,
            "Glucosa": self.glucosa,
            "PresionSanguinea": self.presion_sanguinea,
            "GrosorPiel": self.grosor_piel,
            "Insulina": self.insulina,
            "IMC": self.imc,
            "Edad": self.edad
        }

class SistemaPacientes:
    def __init__(self, archivo_csv="pacientes.csv"):
        self.archivo_csv = archivo_csv
        self.pacientes = []
        self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode="w", newline="", encoding="utf-8") as file:
                campos = ["Nombre", "Teléfono", "Género", "Embarazos", "Glucosa", "PresionSanguinea", "GrosorPiel", "Insulina", "IMC", "Edad"]
                writer = csv.DictWriter(file, fieldnames=campos)
                writer.writeheader()
            return

        with open(self.archivo_csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    paciente = Paciente(
                        row["Nombre"], 
                        row["Teléfono"], 
                        row["Género"], 
                        int(row["Embarazos"]),
                        int(row["Glucosa"]), 
                        int(row["PresionSanguinea"]), 
                        int(row["GrosorPiel"]),
                        int(row["Insulina"]), 
                        float(row["IMC"]), 
                        int(row["Edad"])
                    )
                    self.pacientes.append(paciente)
                except KeyError as e:
                    print(f"Error en la fila: {row}. Falta la columna: {e}")
                except ValueError as e:
                    print(f"Error en la fila: {row}. Valor incorrecto: {e}")

    def guardar_paciente(self, paciente):
        if isinstance(paciente, Paciente):  
            self.pacientes.append(paciente)
            self.guardar_datos()
        else:
            raise ValueError("El objeto proporcionado no es una instancia de Paciente.")

    def guardar_datos(self):
        with open(self.archivo_csv, mode="w", newline="", encoding="utf-8") as file:
            campos = ["Nombre", "Teléfono", "Género", "Embarazos", "Glucosa", "PresionSanguinea", "GrosorPiel", "Insulina", "IMC", "Edad"]
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for paciente in self.pacientes:
                writer.writerow(paciente.to_dict())

    def obtener_pacientes(self):
        return self.pacientes