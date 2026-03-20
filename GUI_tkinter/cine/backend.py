import csv
import os

class Usuario:
    """Clase para representar a un usuario del sistema mediante Programación Orientada a Objetos."""
    def __init__(self, nombre, rol, password):
        self.nombre = nombre
        self.rol = rol
        self.password = password

class Pelicula:
    def __init__(self,id,titulo,clasif,dura,genero,direc_img):
        self.id_pelicula=id
        self.titulo=titulo
        self.clasificacion=clasif
        self.duracion=dura
        self.genero=genero
        self.dir_img=direc_img

class Funcion:
    def __init__(self,id_fun,pelicula,sala,hora_ini,precio):
        self.id_funcion=id_fun
        self.peli=pelicula
        self.sala=sala
        self.hora_inicio=hora_ini
        self.precio=precio

class Producto:
    def __init__(self,id_prod,nombre,categoria,precio,stock):
        self.id_producto=id_prod
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock

class Sala:
    def __init__(self,idsala,numero,filas,columnas,tipo):
        self.idsala=idsala
        self.numero=numero
        self.asientos=[[False for _ in range(columnas)] for _ in range(filas)]
        self.tipo=tipo

    def mostrar_disponibilidad(self):
        return self.asientos
    
    def reservar_asientos(self,fila,columna):
        if not self.asientos[fila][columna]:
            self.asientos[fila][columna]=True
            return True
        return False
    
class CineControlador:
    def __init__(self):
        self.cartelera=[]
        self.inventario_dulceria=[]
        self.ventas_totales=0.0
    
    def agregar_funcion(self,funcion):
        self.cartelera.append(funcion)
    def agregar_producto(self,producto):
        self.inventario_dulceria.append(producto)
    

class SistemaAutenticacion:
    """Clase encargada de gestionar los usuarios y la autenticación leyendo desde un archivo CSV."""
    def __init__(self, archivo_usuarios="usuarios.csv"):
        # Usamos la ruta absoluta basada en donde esté este script
        self.archivo_usuarios = os.path.join(os.path.dirname(__file__), archivo_usuarios)
        self.usuarios = {} # Diccionario para almacenar objetos Usuario
        self._cargar_usuarios()

    def _cargar_usuarios(self):
        """Carga los usuarios exclusivamente desde el archivo CSV."""
        # Solo leemos el CSV si existe, ya no hay usuarios quemados en el código
        if not os.path.exists(self.archivo_usuarios):
            print(f"Advertencia: El archivo {self.archivo_usuarios} no existe. Por favor créalo o registra usuarios.")
            return
            
        with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                usuario_obj = Usuario(
                    nombre=row["nombre"],
                    rol=row["rol"],
                    password=row["password"]
                )
                self.usuarios[row["nombre"]] = usuario_obj

    def registrar_usuario(self, nombre, rol, password):
        """Guarda un nuevo usuario de forma orientada a objetos en memoria y lo añade al CSV."""
        nuevo_usuario = Usuario(nombre, rol, password)
        self.usuarios[nombre] = nuevo_usuario
        
        archivo_existe = os.path.exists(self.archivo_usuarios)
        
        with open(self.archivo_usuarios, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["nombre", "rol", "password"])
            if not archivo_existe:
                writer.writeheader() # Escribe los encabezados solo si es un archivo nuevo
            writer.writerow({
                "nombre": nuevo_usuario.nombre,
                "rol": nuevo_usuario.rol,
                "password": nuevo_usuario.password
            })
            
    def autenticar(self, nombre, password):
        """
        Verifica si el usuario y la contraseña son correctos.
        Retorna el rol si es exitoso, de lo contrario retorna None.
        """
        usuario = self.usuarios.get(nombre)
        if usuario is not None and usuario.password == password:
            return usuario.rol
        return None
    
    def actualizar_csv_completo(self):
        """Sobrescribe el CSV con el estado actual del diccionario de usuarios."""
        with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["nombre", "rol", "password"])
            writer.writeheader()
            for usuario in self.usuarios.values():
                writer.writerow({
                    "nombre": usuario.nombre,
                    "rol": usuario.rol,
                    "password": usuario.password
                })
