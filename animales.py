class Animal:
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas
    
    def descripcion(self):
        print(f"Soy un {self.nombre}, tengo color {self.color} y tengo {self.patas} patas")

ani1=Animal("perro","gris",4)
ani1.descripcion()