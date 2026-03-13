import json
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
    
    @classmethod
    def guardar_usuarios(cls,archivo):
        usuarios_guardados=[{"nombre":u.nombre,"edad":u.edad,"tiposangre":u.tiposangre}for u in cls.usuarios]
        with open(archivo,"w") as f:
            json.dump(usuarios_guardados,f)

    @classmethod
    def cargar_usuarios(cls,archivo):
        try:
            with open(archivo,"r") as f:
                usuarios_guardados=json.load(f)
                cls.usuarios=[Joaquin(u["nombre"],u["edad"],u["tiposangre"])for u in usuarios_guardados]
        except FileNotFoundError:
            cls.usuarios=[]

    @classmethod
    def eliminar_usuario(cls,usuario):
        cls.usuarios.remove(usuario)
        cls.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oopcontkinter//Usuarios2.json")


