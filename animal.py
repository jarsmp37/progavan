class Persona:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
    
    def descrip(self):
        print(f"Hola mi nombre es {self.nombre} y mi color favorito es {self.color}")