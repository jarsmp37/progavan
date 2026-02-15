class Alumno():
    def __init__(self,nombre,carrera,semestre):
        self.nombre=nombre
        self.carrera=carrera
        self.sem=semestre
    
    def datos(self):
        print(f"El alumno {self.nombre} estudia la carrera {self.carrera}")

    def restante(self):
        return 10-self.sem