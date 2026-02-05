class Nombre():
    def __init__(self,nom,edad,carrera):
        self.nombre=nom
        self.edad=edad
        self.carrera=carrera

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.carrera}"
    
    def __repr__(self):
        return f"Nombre(nombre:{self.nombre},edad:{self.edad},Carrera:{self.carrera})"
    
    def __add__(self,otra):
        return f"{self.nombre} y {otra.nombre} se aman"
    
    def __mul__(self,otra):
        return self.edad*otra.edad
    
    def __eq__(self,otra):
        return self.carrera==otra.carrera