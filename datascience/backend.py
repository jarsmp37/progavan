import csv
import os
from datetime import datetime

class Reservacion:
    def __init__(self, nombre, dias_antelacion, solicitudes_especiales, fecha_entrada, fecha_salida, huesped_repetido):
        self.nombre = nombre
        self.dias_antelacion = dias_antelacion
        self.solicitudes_especiales = solicitudes_especiales
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.huesped_repetido = huesped_repetido

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Dias_Antelacion": self.dias_antelacion,
            "Solicitudes_Especiales": self.solicitudes_especiales,
            "Fecha_Entrada": self.fecha_entrada,
            "Fecha_Salida": self.fecha_salida,
            "Huesped_Repetido": self.huesped_repetido,
            "Fecha_Reservacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

class ReservacionManager:
    def __init__(self, filename="reservaciones.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=[
                    "Nombre", "Dias_Antelacion", "Solicitudes_Especiales", "Fecha_Entrada", "Fecha_Salida", "Huesped_Repetido", "Fecha_Reservacion"
                ])
                writer.writeheader()

    def guardar_reservacion(self, reservacion):
        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "Nombre", "Dias_Antelacion", "Solicitudes_Especiales", "Fecha_Entrada", "Fecha_Salida", "Huesped_Repetido", "Fecha_Reservacion"
            ])
            writer.writerow(reservacion.to_dict())

    def obtener_reservaciones(self):
        with open(self.filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def es_huesped_repetido(self, nombre):
        reservaciones = self.obtener_reservaciones()
        return any(reservacion["Nombre"] == nombre for reservacion in reservaciones)