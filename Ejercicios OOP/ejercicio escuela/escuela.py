class Alumno():
    def __init__(self,nombre,matricula):
        self.nombre=nombre
        self.matricula=matricula
        self.calif=[]
    
    def agregar_calificacion(self,calificacion):
        self.calif.append(calificacion)

    def calcular_promedio(self):
        return sum(self.calif)/len(self.calif)
    
    def estado_final(self):
        promedio = self.calcular_promedio()
        return "Aprobado" if promedio >= 70 else "Reprobado"

    def est_final(self):
        if self.calcular_promedio()>=70:
            return "Aprobado"
        else:
            return "Reprobado"



class Grupo():
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.alumnos = [] 

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_promedios(self):
        print(f"Promedios del grupo {self.nombre_grupo}:")
        for alumno in self.alumnos:
            promedio = alumno.calcular_promedio()
            estado = alumno.estado_final()
            print(f"{alumno.nombre} ({alumno.matricula}): Promedio = {promedio:.2f}, Estado = {estado}")

    def mejor_alumno(self):
        if not self.alumnos:
            print("No hay alumnos en el grupo.")
            return None
        mejor = max(self.alumnos, key=lambda alumno: alumno.calcular_promedio())
        print(f"El mejor alumno es {mejor.nombre} ({mejor.matricula}) con un promedio de {mejor.calcular_promedio():.2f}.")
