import csv
import os

class Usuario():
    lista=[]
    ruta_csv=r"C:/Users/Jaime/Documents/GitHub/progavan/GUI_tkinter/ejercicios/base2/personas.csv"
    def __init__(self,name,age,pasword):
        self.nombre=name
        self.edad=age
        self.contra=pasword
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} y su pasword es {self.contra}"
    
    @classmethod
    def mostrar_lista(cls):
        return cls.lista
    
    @classmethod
    def guardar_usuarios(cls):
        campos=["nombre","edad","contraseña"] #Nombres de las columnas en la tabla

        # Crear el directorio si no existe
        directorio = os.path.dirname(cls.ruta_csv)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"Directorio creado: {directorio}")
            except Exception as e:
                print(f"Error al crear directorio: {e}")
                return False
            
        #Guardar el archivo
        with open(cls.ruta_csv,"w", newline='',encoding="utf-8") as f:
            escritor=csv.DictWriter(f, fieldnames=campos, delimiter=',')
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"contraseña":u.contra})
    @classmethod
    def cargar_usuarios(cls):
        if not os.path.exists(cls.ruta_csv):
            print("No hay base de datos previa.")
            return

        with open(cls.ruta_csv, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            # Limpiamos la lista actual para no duplicar si se llama varias veces
            cls.lista = []
            for fila in lector:
                # Al instanciarlo, el __init__ lo agrega a la lista automáticamente
                Usuario(fila["nombre"], fila["edad"], fila["contraseña"])
        print("Datos cargados exitosamente.")    