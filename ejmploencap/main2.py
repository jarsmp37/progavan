from ejercicio1 import Alumno

alu1=Alumno("Michel","Compu",2)
alu2=Alumno("Santi","Ciencia de datos",4)
alu3=Alumno("Fatima","Compu",3)
alu4=Alumno("Orquidia","Ciencia de datos",1)

alu1.datos()
print(f"La alumna {alu1.nombre} le falta {alu1.restante()} semestres")