from clasess import *

h101 = Habitacion(101, "Doble", 150)
h102 = Habitacion(102, "Individual", 100)
h103 = Habitacion(103, "Suite", 250)
print(h101.color)
print(h102.color)
print(h103.color)
print(f"la habitación {h101.numero} cuenta con {h101.mueble}")
print(f"la habitación {h102.numero} cuenta con {h102.mueble}")
print(f"la habitación {h103.numero} cuenta con {h103.mueble}")

reserva = Reserva("Brian Hernández", h101, datetime(2026, 2, 14), datetime(2026, 2, 21))
print(reserva.detalle())