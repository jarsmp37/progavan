class Habitacion:
    color="azul"
    mueble="Escritorio"
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False  

    def descripcion(self):
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio}/noche"