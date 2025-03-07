from datetime import datetime
import json
import os

PERSONAS_JSON = "personas.json"
PACIENTES_JSON = "pacientes.json"
CITAS_JSON = "citas.json"
SERVICIOS_JSON = "servicios.json"
EXPEDIENTES_JSON = "expedientes.json"
DOCTORES_JSON = "doctores.json"

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
            with open(PERSONAS_JSON, "r") as file:
                data = json.load(file)
                for usuario_data in data:
                    Personas(usuario_data["Id"], usuario_data["Nombre"], usuario_data["Rol"])

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
            with open(PACIENTES_JSON, "r") as file:
                data = json.load(file)
                for paciente_data in data:
                    Pacientes(paciente_data["Id"], paciente_data["Nombre"], paciente_data["Rol"], paciente_data["Edad"], paciente_data["Tipo_Sangre"], paciente_data["Alergias"], paciente_data["Peso"], paciente_data["Altura"])

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
            with open(DOCTORES_JSON, "r") as file:
                data = json.load(file)
                for doctor_data in data:
                    Doctores(doctor_data["Id"], doctor_data["Nombre"], doctor_data["Rol"], doctor_data["Especialidad"])

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

    def Crear_receta(self, paciente, medicamentos, instrucciones):
        receta = {
            "paciente": paciente.nombre,
            "medicamentos": medicamentos,
            "instrucciones": instrucciones,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Receta creada para {paciente.nombre}: {receta}")

    def Realizar_Consulta(self, cita):
        if cita.Disponibilidad:
            cita.Disponibilidad = False
            print(f"Consulta realizada para {cita.paciente.nombre} el {cita.dia} a las {cita.hora}.")
        else:
            print("La cita no está disponible.")

    def verificar_expediente(self, paciente, expediente):
        if paciente in expediente:
            print(f"Expediente de {paciente.nombre}: {expediente[paciente]}")
        else:
            print(f"No se encontró expediente para {paciente.nombre}.")


class Recepcionista(Personas):
    def agendar_cita(self, cita, paciente, doctor):
        if cita.Disponibilidad:
            cita.paciente = paciente
            cita.doctor = doctor
            cita.Disponibilidad = False
            print(f"Cita agendada para {paciente.nombre} con {doctor.nombre} el {cita.dia} a las {cita.hora}.")
        else:
            print("La cita no está disponible.")

    def cancelar_cita(self, cita):
        if not cita.Disponibilidad:
            cita.Disponibilidad = True
            cita.paciente = None
            cita.doctor = None
            print("Cita cancelada.")
        else:
            print("La cita ya está disponible.")

    def Acceder_registro(self, paciente):
        print(f"Registro de {paciente.nombre}: Edad: {paciente.edad}, Tipo de Sangre: {paciente.tipo_sangre}, Alergias: {paciente.alergias}")

    def consultar_precios(self, servicio):
        for s in Servicios.Lista_servicios:
            if s.servicio == servicio:
                print(f"El costo de {servicio} es: {s.costo}")
                return
        print("Servicio no encontrado.")


class Expediente:
    def Crear_exp(self, paciente):
        expediente = {
            "Nombre": paciente.nombre,
            "Edad": paciente.edad,
            "Tipo_Sangre": paciente.tipo_sangre,
            "Alergias": paciente.alergias,
            "Peso": paciente.peso,
            "Altura": paciente.altura
        }
        print(f"Expediente creado para {paciente.nombre}: {expediente}")
        return expediente

    def Borra_exp(self, paciente, expedientes):
        if paciente in expedientes:
            del expedientes[paciente]
            print(f"Expediente de {paciente.nombre} borrado.")
        else:
            print(f"No se encontró expediente para {paciente.nombre}.")

    @classmethod
    def cargar_expedientes(cls):
        if os.path.exists(EXPEDIENTES_JSON):
            with open(EXPEDIENTES_JSON, "r") as file:
                return json.load(file)
        return {}

    @classmethod
    def guardar_expedientes(cls, expedientes):
        with open(EXPEDIENTES_JSON, "w") as file:
            json.dump(expedientes, file, indent=4)


class Citas:
    lista_citas = []

    def __init__(self, dia, Hora):
        self.dia = dia
        self.hora = Hora
        self.Disponibilidad = True
        self.paciente = None
        self.doctor = None
        Citas.lista_citas.append(self)

    @classmethod
    def cargar_citas(cls):
        if os.path.exists(CITAS_JSON):
            with open(CITAS_JSON, "r") as file:
                data = json.load(file)
                for cita_data in data:
                    cita = Citas(cita_data["dia"], cita_data["hora"])
                    cita.Disponibilidad = cita_data["Disponibilidad"]
                    cita.paciente = cita_data["paciente"]
                    cita.doctor = cita_data["doctor"]

    @classmethod
    def guardar_citas(cls):
        data = []
        for cita in Citas.lista_citas:
            data.append({
                "dia": cita.dia,
                "hora": cita.hora,
                "Disponibilidad": cita.Disponibilidad,
                "paciente": cita.paciente,
                "doctor": cita.doctor
            })
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
            with open(SERVICIOS_JSON, "r") as file:
                data = json.load(file)
                for servicio_data in data:
                    Servicios(servicio_data["servicio"], servicio_data["costo"])

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


class Consulta:
    def __init__(self, cita, paciente, servicio):
        self.cita = cita
        self.paciente = paciente
        self.servicio = servicio

    def diagnosticar(self, diagnostico):
        print(f"Diagnóstico para {self.paciente.nombre}: {diagnostico}")

    def Tratamiento(self, tratamiento):
        print(f"Tratamiento para {self.paciente.nombre}: {tratamiento}")