class Perro():
    tipo="Perro"
    def __init__(self,nombre, color):
        self.nombre=nombre
        self.color=color
    
    def sonido(self):
        return "Guau"
    
class Gato():
    tipo="Gato"
    def __init__(self,nombre, color):
        self.nombre=nombre
        self.color=color
    
    def sonido(self):
        return "Miau"
    
class Canguro():
    tipo="canguro"
    def __init__(self,nombre, color):
        self.nombre=nombre
        self.color=color
    
    def sonido(self):
        return "Boing"
    
class Veterinaria():
    def __init__(self,nom):
        self.nombre=nom
        self.lista=[]
    
    def agregar(self,animal):
        self.lista.append(animal)

    def inventario(self):
        for i in self.lista:
            print(f"El animal es un {i.tipo} su nombre es {i.nombre} y es de color {i.color} y hace el sonido {i.sonido()}")


