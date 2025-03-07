import json
from datetime import datetime
import os

# Rutas de los archivos JSON
USUARIOS_JSON = "usuarios.json"
HABITACIONES_JSON = "habitaciones.json"
HUESPEDES_JSON = "huespedes.json"
RESERVAS_JSON = "reservas.json"


class Usuario:
    lista_usuario = []

    def __init__(self, Nombre, Rol, Password):
        self.nombre = Nombre
        self.rol = Rol
        self.__pass = Password
        Usuario.lista_usuario.append(self)

    def info(self):
        return f"El usuario se llama {self.nombre}, tiene rol de {self.rol}"

    @classmethod
    def iniciar_sesion(cls, nombre, password):
        for usuario in Usuario.lista_usuario:
            if usuario.nombre == nombre and usuario._Usuario__pass == password:
                print(f"Bienvenido {usuario.nombre}, acabas de iniciar sesión")
                return usuario
        print("Datos incorrectos para inicio de sesión")
        return None

    @classmethod
    def cargar_usuarios(cls):
        Usuario.lista_usuario.clear()
        if os.path.exists(USUARIOS_JSON):
            with open(USUARIOS_JSON, "r") as file:
                data = json.load(file)
                for usuario_data in data:
                    Usuario(usuario_data["nombre"], usuario_data["rol"], usuario_data["password"])

    @classmethod
    def guardar_usuarios(cls):
        data = []
        for usuario in Usuario.lista_usuario:
            data.append({
                "nombre": usuario.nombre,
                "rol": usuario.rol,
                "password": usuario._Usuario__pass
            })
        with open(USUARIOS_JSON, "w") as file:
            json.dump(data, file, indent=4)


class Administrador(Usuario):
    def registrar(self, huesped):
        if isinstance(huesped, Huesped):
            Huesped.lista_huespedes.append(huesped)
            print(f"Huesped {huesped.nombre} registrado exitosamente.")
            Huesped.guardar_huespedes()
        else:
            print("Error: El objeto no es un Huesped válido.")

    def modificarcliente(self, huesped, nuevo_nombre=None, nuevo_telefono=None):
        if huesped in Huesped.lista_huespedes:
            if nuevo_nombre:
                huesped.nombre = nuevo_nombre
            if nuevo_telefono:
                huesped.telefono = nuevo_telefono
            print(f"Huesped {huesped.nombre} modificado exitosamente.")
            Huesped.guardar_huespedes()
        else:
            print("Error: Huesped no encontrado.")

    def eliminarcliente(self, huesped):
        if huesped in Huesped.lista_huespedes:
            Huesped.lista_huespedes.remove(huesped)
            print(f"Huesped {huesped.nombre} eliminado exitosamente.")
            Huesped.guardar_huespedes()
        else:
            print("Error: Huesped no encontrado.")

    def crearhabitaciones(self, numero, tipo, camas, costonoche):
        nueva_habitacion = Habitacion(numero, tipo, camas, costonoche)
        print(f"Habitación {nueva_habitacion.numero} creada exitosamente.")
        Habitacion.guardar_habitaciones()


class Recepcionista(Usuario):
    def reservar(self, habitacion, fecha_entrada, fecha_salida, huesped):
        if habitacion.disponibilidad:
            nueva_reserva = Reserva(len(Reserva.lista_reservas) + 1, habitacion, fecha_entrada, fecha_salida, huesped)
            habitacion.disponibilidad = False
            print(f"Reserva realizada exitosamente para la habitación {habitacion.numero}.")
            Reserva.guardar_reservas()
        else:
            print(f"La habitación {habitacion.numero} no está disponible para reservar.")

    def cancelar(self, reserva):
        if reserva in Reserva.lista_reservas:
            reserva.habitacion.disponibilidad = True
            Reserva.lista_reservas.remove(reserva)
            print(f"Reserva {reserva.id} cancelada exitosamente.")
            Reserva.guardar_reservas()
        else:
            print("Error: Reserva no encontrada.")


class Habitacion:
    lista_Habitaciones = []

    def __init__(self, numero, tipo, camas, costonoche):
        self.numero = numero
        self.tipo = tipo
        self.camas = camas
        self.costo = costonoche
        self.disponibilidad = True
        Habitacion.lista_Habitaciones.append(self)
        

    @classmethod
    def cargar_habitaciones(cls):
        Habitacion.lista_Habitaciones.clear()
        if os.path.exists(HABITACIONES_JSON):
            with open(HABITACIONES_JSON, "r") as file:
                data = json.load(file)
                for habitacion_data in data:
                    habitacion = Habitacion(
                        habitacion_data["numero"],
                        habitacion_data["tipo"],
                        habitacion_data["camas"],
                        habitacion_data["costo"]
                    )
                    habitacion.disponibilidad = habitacion_data["disponibilidad"]
                

    @classmethod
    def guardar_habitaciones(cls):
        data = []
        for habitacion in Habitacion.lista_Habitaciones:
            data.append({
                "numero": habitacion.numero,
                "tipo": habitacion.tipo,
                "camas": habitacion.camas,
                "costo": habitacion.costo,
                "disponibilidad": habitacion.disponibilidad
            })
        with open(HABITACIONES_JSON, "w") as file:
            json.dump(data, file, indent=4)
        


class Huesped:
    lista_huespedes = []

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        Huesped.lista_huespedes.append(self)

    @classmethod
    def cargar_huespedes(cls):
        Huesped.lista_huespedes.clear()
        if os.path.exists(HUESPEDES_JSON):
            with open(HUESPEDES_JSON, "r") as file:
                data = json.load(file)
                for huesped_data in data:
                    Huesped(huesped_data["nombre"], huesped_data["telefono"])

    @classmethod
    def guardar_huespedes(cls):
        data = []
        for huesped in Huesped.lista_huespedes:
            data.append({
                "nombre": huesped.nombre,
                "telefono": huesped.telefono
            })
        with open(HUESPEDES_JSON, "w") as file:
            json.dump(data, file, indent=4)


from datetime import datetime

class Reserva:
    lista_reservas = []

    def __init__(self, id, habitacion, fecha_entrada, fecha_salida, huesped):
        self.id = id
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.huesped = huesped
        Reserva.lista_reservas.append(self)

    @classmethod
    def cargar_reservas(cls):
        Reserva.lista_reservas.clear()
        if os.path.exists(RESERVAS_JSON):
            with open(RESERVAS_JSON, "r") as file:
                data = json.load(file)
                for reserva_data in data:
                    habitacion = next((h for h in Habitacion.lista_Habitaciones if h.numero == reserva_data["habitacion"]), None)
                    huesped = next((h for h in Huesped.lista_huespedes if h.nombre == reserva_data["huesped"]), None)
                    if habitacion and huesped:
                        # Convertir las fechas de cadena a datetime
                        fecha_entrada = datetime.strptime(reserva_data["fecha_entrada"], "%Y-%m-%d")
                        fecha_salida = datetime.strptime(reserva_data["fecha_salida"], "%Y-%m-%d")
                        Reserva(reserva_data["id"], habitacion, fecha_entrada, fecha_salida, huesped)

    @classmethod
    def guardar_reservas(cls):
        data = []
        for reserva in Reserva.lista_reservas:
            data.append({
                "id": reserva.id,
                "habitacion": reserva.habitacion.numero,
                "fecha_entrada": reserva.fecha_entrada.strftime("%Y-%m-%d"),
                "fecha_salida": reserva.fecha_salida.strftime("%Y-%m-%d"),
                "huesped": reserva.huesped.nombre
            })
        with open(RESERVAS_JSON, "w") as file:
            json.dump(data, file, indent=4)