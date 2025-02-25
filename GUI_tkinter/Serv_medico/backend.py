from datetime import datetime
import json
import os

PERSONAS_JSON = "personas.json"
class Personas:
    Lista_personas=[]
    def __init__(self,Id,Nombre,Rol):
        self.id=Id
        self.nombre=Nombre
        self.rol=Rol
        Personas.Lista_personas.append(self)

    @classmethod
    def cargar_usuarios(cls):
        if os.path.exists(PERSONAS_JSON):
            with open(PERSONAS_JSON, "r") as file:
                data = json.load(file)
                for usuario_data in data:
                    Usuario(usuario_data["Id"], usuario_data["Nombre"], usuario_data["Rol"])

    @classmethod
    def guardar_usuarios(cls):
        data = []
        for usuario in Usuario.lista_usuario:
            data.append({
                "Id": usuario.id,
                "Nombre": usuario.nombre,
                "Rol": usuario.rol
            })
        with open(PERSONAS_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Pacientes(Personas):
    Lista_pacientes=[]
    def __init__(self,Id,Nombre,Rol,Edad,Tipo_Sangre,Alergias,Peso,Altura):
        super().__init__(Id,Nombre,Rol)
        self.edad=Edad
        self.tipo_sangre=Tipo_Sangre
        self.alregias=Alergias
        self.peso=Peso
        self.altura=Altura
        Pacientes.Lista_pacientes.append(self)

class Doctores(Personas):
    def __init__(self,Id,Nombre,Rol,Especialidad):
        super().__init__(Id,Nombre,Rol)
        self.especialidad=Especialidad

    def Crear_receta(self):
        pass

    def Realizar_Consulta(self,cita):
        pass

    def verificar_expediente(self,paciente,expediente):
        pass

class Recepcionista(Personas):
    def agendar_cita(self,cita):
        pass

    def cancelar_cita(self,cita):
        pass

    def Acceder_registro(self,paciente):
        pass

    def consultar_precios(self,servicio):
        pass

class Expediente:
    def Crear_exp(self,paciente):
        #datos del paciente
        pass

    def Borra_exp(self,paciente):
        #expediente
        pass

class Citas:
    lista_citas=[]
    def __init__(self,dia,Hora):
        self.dia=dia
        self.hora=Hora
        self.Disponibilidad=True
        Citas.lista_citas.append(self)

class Servicios:
    Lista_servicios=[]
    def __init__(self,servicio,costo):
        self.servicio=servicio
        self.costo=costo
        Servicios.Lista_servicios.append(self)

class Consulta:
    def __init__(self,cita,paciente,servicio):
        self.cita=cita
        self.paciente=paciente
        self.servicio=servicio

    def diagnosticar(self):
        pass

    def Tratamiento(self):
        pass


