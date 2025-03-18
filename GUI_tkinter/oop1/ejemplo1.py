import json
class personas:
    usuarios=[]
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
        personas.usuarios.append(self)
    
    def mostrardatos(self):
        return f" Usuario:{self.nombre},     edad:{self.edad}"
    
    @classmethod
    def obtener_lista(cls):
        return cls.usuarios
    
    @classmethod
    def guardar_usuarios(cls,archivo):
        usuarios_guardados=[{"nombre":u.nombre,"edad":u.edad}for u in cls.usuarios]
        with open(archivo,"w") as f:
            json.dump(usuarios_guardados,f)

    @classmethod
    def cargar_usuarios(cls,archivo):
        try:
            with open(archivo,"r") as f:
                usuarios_guardados=json.load(f)
                cls.usuarios=[personas(u["nombre"],u["edad"])for u in usuarios_guardados]
        except FileNotFoundError:
            cls.usuarios=[]

    @classmethod
    def eliminar_usuario(cls,usuario):
        cls.usuarios.remove(usuario)
        cls.guardar_usuarios("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//oop1//Usuarios.json")
    

    
