class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def saludo(self):
        print(f"Soy un {self.nombre} y rujo")