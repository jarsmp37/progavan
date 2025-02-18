class Joaquin:
    usuarios=[]
    
    def __init__(self,nombre,edad, tiposangre):
        self.nombre=nombre
        self.edad=edad
        self.tiposangre=tiposangre
        Joaquin.usuarios.append(self)

    def mostrarinfo(self):
        return f"El usuario {self.nombre}, tiene {self.edad} años y su tipo de sangre es {self.tiposangre}"
    
    @classmethod
    def mostarusuarios(cls):
        return cls.usuarios