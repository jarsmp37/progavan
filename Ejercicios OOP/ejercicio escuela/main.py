from escuela import *

alumno1 = Alumno("Estefania Juárez", 34214213)
alumno2 = Alumno("Michell Flores", 39283)
alumno3 = Alumno("Joaquin Guerrero", 12314)
alumno4 = Alumno("Dana Domínguez", 12314)
alumno5 = Alumno("Alondra Alemán",44234139)

alumno1.agregar_calificacion(95)
alumno1.agregar_calificacion(90)

alumno2.agregar_calificacion(95)
alumno2.agregar_calificacion(70)
alumno2.agregar_calificacion(98)

alumno3.agregar_calificacion(65)
alumno3.agregar_calificacion(72)
alumno3.agregar_calificacion(61)
alumno3.agregar_calificacion(65)

alumno4.agregar_calificacion(85)
alumno4.agregar_calificacion(92)
alumno4.agregar_calificacion(100)

alumno5.agregar_calificacion(92)
alumno5.agregar_calificacion(72)
alumno5.agregar_calificacion(61)

print(f"La alumna {alumno1.nombre} tiene promedio de: {alumno1.calcular_promedio():.2f} y esta: {alumno1.estado_final()}")
print(f"La alumna {alumno2.nombre} tiene promedio de: {alumno2.calcular_promedio():.2f} y esta: {alumno2.estado_final()}")
print(f"La alumna {alumno3.nombre} tiene promedio de: {alumno3.calcular_promedio():.2f} y esta: {alumno3.estado_final()}")
print(f"La alumna {alumno4.nombre} tiene promedio de: {alumno4.calcular_promedio():.2f} y esta: {alumno4.estado_final()}")
print(f"La alumna {alumno5.nombre} tiene promedio de: {alumno5.calcular_promedio():.2f} y esta: {alumno5.estado_final()}")


grupo1=Grupo("Progra")
