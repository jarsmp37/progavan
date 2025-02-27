from datetime import datetime
import json
import os

PERSONAS_JSON = "personas.json"

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


class Doctores(Personas):
    def __init__(self, Id, Nombre, Rol, Especialidad):
        super().__init__(Id, Nombre, Rol)
        self.especialidad = Especialidad

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


class Citas:
    lista_citas = []

    def __init__(self, dia, Hora):
        self.dia = dia
        self.hora = Hora
        self.Disponibilidad = True
        self.paciente = None
        self.doctor = None
        Citas.lista_citas.append(self)


class Servicios:
    Lista_servicios = []

    def __init__(self, servicio, costo):
        self.servicio = servicio
        self.costo = costo
        Servicios.Lista_servicios.append(self)


class Consulta:
    def __init__(self, cita, paciente, servicio):
        self.cita = cita
        self.paciente = paciente
        self.servicio = servicio

    def diagnosticar(self, diagnostico):
        print(f"Diagnóstico para {self.paciente.nombre}: {diagnostico}")

    def Tratamiento(self, tratamiento):
        print(f"Tratamiento para {self.paciente.nombre}: {tratamiento}")