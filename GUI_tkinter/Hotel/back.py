class Usuario:
    lista_usuario=[]
    def __init__(self,Nombre,Rol,Password):
        self.nombre=Nombre
        self.rol=Rol
        self.__pass=Password
        Usuario.lista_usuario.append(self)

    def info(self):
        return f"El usuario se llama {self.nombre}, tiene rol de {self.rol}"
    
    @classmethod
    def iniciar_sesion(cls,nombre,password):
        for usuario in Usuario.lista_usuario:
            if usuario.nombre==nombre and usuario.__pass==password:
                print (f"Bienvenido {usuario.nombre} acabas de iniciar sesión")
            else:
                print("Datos incorrectos para inicio de sesión")


class Administrador(Usuario):
    def registrar(self,huesped):
        pass
    def modificarcliente(self, huesped):
        pass

    def eliminarcliente(self,huesped):
        pass

    def crearhabitaciones(self, huesped):
        pass

class Recepcionista(Usuario):
    def checardisponibilidad(self,habitacion):
        pass

    def reservar(self, habitacion, fecha):
        pass

    def cancelar(self,habitacion, fecha):
        pass


class Habitacion:
    lista_Habitaciones=[]
    def __init__(self,numero,tipo,camas,costonoche):
        self.numero=numero
        self.tipo=tipo
        self.camas=camas
        self.costo=costonoche
        self.disponibilidad=True
        Habitacion.lista_Habitaciones.append(self)














us1=Usuario("Jaime","Administrador",1234)
us2=Usuario("Mafer","Recepcionista","abc") 
us3=Usuario("Pao","Huesped",4823) 
us4=Usuario("Omar","Recepcionista","hola") 
us5=Usuario("Abraham","Huesped",7654)     
print(us1.info())
print(us2.info())
print(us3.info())
print(us4.info())
print(us5.info())

Usuario.iniciar_sesion("Jaime",1234)
Usuario.iniciar_sesion("Jaime",1235)
