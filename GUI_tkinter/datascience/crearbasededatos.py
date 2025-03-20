import csv
import random

# Datos ficticios para generar pacientes
nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Sofía", "Diego", "Elena"]
generos = ["Masculino", "Femenino"]

# Función para generar datos ficticios
def generar_paciente():
    nombre = random.choice(nombres)
    telefono = f"55{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
    genero = random.choice(generos)
    embarazos = random.randint(0, 5) if genero == "Femenino" else 0
    glucosa = random.randint(70, 200)
    presion_sanguinea = random.randint(60, 120)
    grosor_piel = random.randint(10, 50)
    insulina = random.randint(0, 200)
    imc = round(random.uniform(18.5, 35.0), 1)
    edad = random.randint(18, 70)

    return [nombre, telefono, genero, embarazos, glucosa, presion_sanguinea, grosor_piel, insulina, imc, edad]

# Crear el archivo CSV con 10 pacientes
with open("pacientes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Teléfono", "Género", "Embarazos", "Glucosa", "PresionSanguinea", "GrosorPiel", "Insulina", "IMC", "Edad"])
    for _ in range(10):
        writer.writerow(generar_paciente())

print("Archivo 'pacientes.csv' generado con 10 pacientes ficticios.")