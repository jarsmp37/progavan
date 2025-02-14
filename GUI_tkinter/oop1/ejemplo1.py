class personas:
    usuarios=[]
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
        personas.usuarios.append(self)
    
    def mostrardatos(self):
        return f" Usuario:{self.nombre}, edad:{self.edad}"
    
    @classmethod
    def obtener_lista(cls):
        return cls.usuarios
    

    
