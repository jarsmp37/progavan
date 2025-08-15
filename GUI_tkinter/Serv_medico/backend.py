from datetime import datetime
import json
import os
import sys


# Determinar si estamos ejecutando como .exe o como script
if getattr(sys, 'frozen', False):
    # Si es ejecutable, la ruta es donde está el .exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Si es script, la ruta normal
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta para datos persistentes (se creará si no existe)
DATA_DIR = os.path.join(BASE_DIR, 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "assets", "data")

# Rutas de los archivos JSON
PERSONAS_JSON = os.path.join(DATA_DIR, "personas.json")
PACIENTES_JSON = os.path.join(DATA_DIR, "pacientes.json")
CITAS_JSON = os.path.join(DATA_DIR, "citas.json")
SERVICIOS_JSON = os.path.join(DATA_DIR, "servicios.json")
EXPEDIENTES_JSON = os.path.join(DATA_DIR, "expedientes.json")
DOCTORES_JSON = os.path.join(DATA_DIR, "doctores.json")

class Personas:
    Lista_personas = []

    def __init__(self, Id, Nombre, Rol):
        self.id = Id
        self.nombre = Nombre
        self.rol = Rol
        Personas.Lista_personas.append(self)

    @classmethod
    def cargar_usuarios(cls):
        if os.path.exists(PERSONAS_JSON):
            try:
                with open(PERSONAS_JSON, "r") as file:
                    data = json.load(file)
                    for usuario_data in data:
                        Personas(usuario_data["Id"], usuario_data["Nombre"], usuario_data["Rol"])
            except json.JSONDecodeError:
                print("Advertencia: El archivo de personas está vacío o corrupto. Se inicializó una lista vacía.")

    @classmethod
    def guardar_usuarios(cls):
        data = []
        for usuario in Personas.Lista_personas:
            data.append({
                "Id": usuario.id,
                "Nombre": usuario.nombre,
                "Rol": usuario.rol
            })
        with open(PERSONAS_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Pacientes(Personas):
    Lista_pacientes = []

    def __init__(self, Id, Nombre, Rol, Edad, Tipo_Sangre, Alergias, Peso, Altura):
        super().__init__(Id, Nombre, Rol)
        self.edad = Edad
        self.tipo_sangre = Tipo_Sangre
        self.alergias = Alergias
        self.peso = Peso
        self.altura = Altura
        Pacientes.Lista_pacientes.append(self)

    @classmethod
    def cargar_pacientes(cls):
        if os.path.exists(PACIENTES_JSON):
            try:
                with open(PACIENTES_JSON, "r") as file:
                    data = json.load(file)
                    for paciente_data in data:
                        Pacientes(
                            paciente_data["Id"], paciente_data["Nombre"], paciente_data["Rol"],
                            paciente_data["Edad"], paciente_data["Tipo_Sangre"],
                            paciente_data["Alergias"], paciente_data["Peso"], paciente_data["Altura"]
                        )
            except json.JSONDecodeError:
                print("Advertencia: El archivo de pacientes está vacío o corrupto. Se inicializó una lista vacía.")

    @classmethod
    def guardar_pacientes(cls):
        data = []
        for paciente in Pacientes.Lista_pacientes:
            data.append({
                "Id": paciente.id,
                "Nombre": paciente.nombre,
                "Rol": paciente.rol,
                "Edad": paciente.edad,
                "Tipo_Sangre": paciente.tipo_sangre,
                "Alergias": paciente.alergias,
                "Peso": paciente.peso,
                "Altura": paciente.altura
            })
        with open(PACIENTES_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Doctores(Personas):
    Lista_doctores = []

    def __init__(self, Id, Nombre, Rol, Especialidad):
        super().__init__(Id, Nombre, Rol)
        self.especialidad = Especialidad
        Doctores.Lista_doctores.append(self)

    @classmethod
    def cargar_doctores(cls):
        if os.path.exists(DOCTORES_JSON):
            try:
                with open(DOCTORES_JSON, "r") as file:
                    data = json.load(file)
                    for doctor_data in data:
                        Doctores(doctor_data["Id"], doctor_data["Nombre"], doctor_data["Rol"], doctor_data["Especialidad"])
            except json.JSONDecodeError:
                print("Advertencia: El archivo de doctores está vacío o corrupto. Se inicializó una lista vacía.")

    @classmethod
    def guardar_doctores(cls):
        data = []
        for doctor in Doctores.Lista_doctores:
            data.append({
                "Id": doctor.id,
                "Nombre": doctor.nombre,
                "Rol": doctor.rol,
                "Especialidad": doctor.especialidad
            })
        with open(DOCTORES_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Citas:
    lista_citas = []

    def __init__(self, dia, Hora):
        self.dia = dia
        self.hora = Hora
        self.Disponibilidad = True
        self.paciente = None
        self.doctor = None
        self.estado = "Pendiente" 
        Citas.lista_citas.append(self)

    @classmethod
    def cargar_citas(cls):
        if os.path.exists(CITAS_JSON):
            try:
                with open(CITAS_JSON, "r") as file:
                    data = json.load(file)
                    for cita_data in data:
                        cita = Citas(cita_data["dia"], cita_data["hora"])
                        cita.Disponibilidad = cita_data["Disponibilidad"]
                        cita.estado = cita_data.get("estado", "Pendiente")  # Cargar el estado
                        # Busca el paciente y el doctor por nombre
                        paciente_nombre = cita_data.get("paciente")
                        doctor_nombre = cita_data.get("doctor")
                        cita.paciente = next((p for p in Pacientes.Lista_pacientes if p.nombre == paciente_nombre), None)
                        cita.doctor = next((d for d in Doctores.Lista_doctores if d.nombre == doctor_nombre), None)
            except json.JSONDecodeError:
                print("Advertencia: El archivo de citas está vacío o corrupto. Se inicializó una lista vacía.")

    @classmethod
    def guardar_citas(cls):
        data = []
        for cita in Citas.lista_citas:
            cita_data = {
                "dia": cita.dia,
                "hora": cita.hora,
                "Disponibilidad": cita.Disponibilidad,
                "estado": cita.estado,  # Guardar el estado de la cita
                "paciente": cita.paciente.nombre if cita.paciente else None,
                "doctor": cita.doctor.nombre if cita.doctor else None
            }
            data.append(cita_data)
        with open(CITAS_JSON, "w") as file:
            json.dump(data, file, indent=4)

class Servicios:
    Lista_servicios = []

    def __init__(self, servicio, costo):
        self.servicio = servicio
        self.costo = costo
        Servicios.Lista_servicios.append(self)

    @classmethod
    def cargar_servicios(cls):
        if os.path.exists(SERVICIOS_JSON):
            try:
                with open(SERVICIOS_JSON, "r") as file:
                    data = json.load(file)
                    for servicio_data in data:
                        Servicios(servicio_data["servicio"], servicio_data["costo"])
            except json.JSONDecodeError:
                print("Advertencia: El archivo de servicios está vacío o corrupto. Se inicializó una lista vacía.")

    @classmethod
    def guardar_servicios(cls):
        data = []
        for servicio in Servicios.Lista_servicios:
            data.append({
                "servicio": servicio.servicio,
                "costo": servicio.costo
            })
        with open(SERVICIOS_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Expediente:
    @classmethod
    def cargar_expedientes(cls):
        if os.path.exists(EXPEDIENTES_JSON):
            try:
                with open(EXPEDIENTES_JSON, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Advertencia: El archivo de expedientes está vacío o corrupto. Se inicializó un diccionario vacío.")
        return {}

    @classmethod
    def guardar_expedientes(cls, expedientes):
        with open(EXPEDIENTES_JSON, "w") as file:
            json.dump(expedientes, file, indent=4)