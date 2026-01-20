class Coche():
    def __init__(self,marca,modelo,año,color):
        self.mark=marca
        self.model=modelo
        self.year=año
        self.color=color

    def descripcion(self):
        print(f"Este coche es de color {self.color} de la marca {self.mark} y modelo {self.model} del año {self.year}.")