from datetime import datetime

class Habitacion():
    color="azul"
    mueble="Escritorio"
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False  

    def descripcion(self):
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio}/noche"


class Reserva():
    def __init__(self, huesped, habitacion, fecha_inicio, fecha_fin):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def calcular_costo(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        return dias * self.habitacion.precio

    def detalle(self):
        costo = self.calcular_costo()
        return (f"Reserva para {self.huesped} en Habitación {self.habitacion.numero} "
                f"del {self.fecha_inicio.date()} al {self.fecha_fin.date()} "
                f"- Total: ${costo}")