from backend import *

# Crear algunos objetos
paciente1 = Pacientes(1, "Juan Pérez", "Paciente", 30, "O+", "Ninguna", 70, 1.75)
doctor1 = Doctores(2, "Dr. García", "Doctor", "Cardiólogo")
recepcionista1 = Recepcionista(3, "Ana López", "Recepcionista")
cita1 = Citas("2023-10-15", "10:00")
servicio1 = Servicios("Consulta General", 500)

# Agendar cita
recepcionista1.agendar_cita(cita1, paciente1, doctor1)

# Realizar consulta
doctor1.Realizar_Consulta(cita1)

# Crear expediente
expedientes = {}
expediente = Expediente()
expedientes[paciente1] = expediente.Crear_exp(paciente1)

# Diagnosticar y tratamiento
consulta1 = Consulta(cita1, paciente1, servicio1)
consulta1.diagnosticar("Hipertensión")
consulta1.Tratamiento("Medicamentos y dieta baja en sal")

# Verificar expediente
doctor1.verificar_expediente(paciente1, expedientes)

# Cancelar cita
recepcionista1.cancelar_cita(cita1)