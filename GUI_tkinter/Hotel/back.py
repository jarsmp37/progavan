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


class Administrador(Usuario):
    def registrar(self, huesped):
        if isinstance(huesped, Huesped):
            Huesped.lista_huespedes.append(huesped)
            print(f"Huesped {huesped.nombre} registrado exitosamente.")
        else:
            print("Error: El objeto no es un Huesped válido.")

    def modificarcliente(self, huesped, nuevo_nombre=None, nuevo_telefono=None):
        if huesped in Huesped.lista_huespedes:
            if nuevo_nombre:
                huesped.nombre = nuevo_nombre
            if nuevo_telefono:
                huesped.telefono = nuevo_telefono
            print(f"Huesped {huesped.nombre} modificado exitosamente.")
        else:
            print("Error: Huesped no encontrado.")

    def eliminarcliente(self, huesped):
        if huesped in Huesped.lista_huespedes:
            Huesped.lista_huespedes.remove(huesped)
            print(f"Huesped {huesped.nombre} eliminado exitosamente.")
        else:
            print("Error: Huesped no encontrado.")

    def crearhabitaciones(self, numero, tipo, camas, costonoche):
        nueva_habitacion = Habitacion(numero, tipo, camas, costonoche)
        print(f"Habitación {nueva_habitacion.numero} creada exitosamente.")


class Recepcionista(Usuario):
    def checardisponibilidad(self, habitacion):
        if habitacion.disponibilidad:
            print(f"La habitación {habitacion.numero} está disponible.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible.")

    def reservar(self, habitacion, fecha_entrada, fecha_salida, huesped):
        if habitacion.disponibilidad:
            nueva_reserva = Reserva(len(Reserva.lista_reservas) + 1, habitacion, fecha_entrada, fecha_salida, huesped)
            habitacion.disponibilidad = False
            print(f"Reserva realizada exitosamente para la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible para reservar.")

    def cancelar(self, reserva):
        if reserva in Reserva.lista_reservas:
            reserva.habitacion.disponibilidad = True
            Reserva.lista_reservas.remove(reserva)
            print(f"Reserva {reserva.id} cancelada exitosamente.")
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


class Huesped:
    lista_huespedes = []

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        Huesped.lista_huespedes.append(self)


from datetime import datetime  

class Reserva:
    lista_reservas = []

    def __init__(self, id, habitacion, fecha_entrada, fecha_salida, huesped):
        self.id = id
        self.habitacion = habitacion
        self.fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()  
        self.fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()    
        self.huesped = huesped
        Reserva.lista_reservas.append(self)

    def costo_total(self):
        dias = (self.fecha_salida - self.fecha_entrada).days  
        costototal = self.habitacion.costo * dias
        return f"El costo total de la habitación {self.habitacion.numero} será {costototal}."



admin = Administrador("Jaime", "Administrador", "admin123")

huesped1 = Huesped("Juan Perez", "123456789")
habitacion1 = Habitacion(101, "Individual", 1, 100)

admin.registrar(huesped1)
admin.crearhabitaciones(102, "Doble", 2, 150)

recepcionista = Recepcionista("Recepcionista1", "Recepcionista", "recepcion123")
recepcionista.reservar(habitacion1, "2023-10-01", "2023-10-05", huesped1)

reserva = Reserva.lista_reservas[0]
print(reserva.costo_total())

recepcionista.cancelar(reserva)