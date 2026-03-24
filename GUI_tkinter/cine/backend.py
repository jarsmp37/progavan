import csv
import os
from datetime import datetime

class Usuario:
    """Clase para representar a un usuario del sistema mediante Programación Orientada a Objetos."""
    def __init__(self, nombre, rol, password):
        self.nombre = nombre
        self.rol = rol
        self.password = password

class Pelicula:
    def __init__(self,id,titulo,clasif,dura,genero,sinopsis,direc_img):
        self.id_pelicula=id
        self.titulo=titulo
        self.clasificacion=clasif
        self.duracion=dura
        self.genero=genero
        self.sinopsis=sinopsis
        self.dir_img=direc_img

class Funcion:
    def __init__(self,id_fun,id_pelicula,id_sala,dia,hora_ini):
        self.id_funcion=id_fun
        self.id_pelicula=id_pelicula
        self.id_sala=id_sala
        self.dia=dia
        self.hora_inicio=hora_ini

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
        filas = int(filas)
        columnas = int(columnas)
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

class SistemaSalas:
    """Clase encargada de gestionar las salas del cine con almacenamiento en CSV."""
    def __init__(self, archivo_salas="salas.csv"):
        self.archivo_salas = os.path.join(os.path.dirname(__file__), archivo_salas)
        self.salas = {} # Diccionario para almacenar las salas en memoria
        self._cargar_salas()

    def _cargar_salas(self):
        """Carga las salas desde el archivo CVS si existe."""
        if not os.path.exists(self.archivo_salas):
            return
            
        with open(self.archivo_salas, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                s = Sala(
                    idsala=row["idsala"],
                    numero=row["numero"],
                    filas=row["filas"],
                    columnas=row["columnas"],
                    tipo=row["tipo"]
                )
                self.salas[str(row["numero"])] = s

    def registrar_sala(self, idsala, numero, filas, columnas, tipo):
        """Registra una nueva sala y la adjunta al final del CSV."""
        nueva_sala = Sala(idsala, numero, filas, columnas, tipo)
        self.salas[str(numero)] = nueva_sala
        
        archivo_existe = os.path.exists(self.archivo_salas)
        with open(self.archivo_salas, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["idsala", "numero", "filas", "columnas", "tipo"])
            if not archivo_existe:
                writer.writeheader()
            writer.writerow({
                "idsala": nueva_sala.idsala,
                "numero": nueva_sala.numero,
                "filas": len(nueva_sala.asientos),
                "columnas": len(nueva_sala.asientos[0]) if len(nueva_sala.asientos) > 0 else 0,
                "tipo": nueva_sala.tipo
            })
            
    def actualizar_csv_completo(self):
        """Sobrescribe el CSV completo si se edita o borra una sala."""
        with open(self.archivo_salas, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["idsala", "numero", "filas", "columnas", "tipo"])
            writer.writeheader()
            for sala in self.salas.values():
                writer.writerow({
                    "idsala": sala.idsala,
                    "numero": sala.numero,
                    "filas": len(sala.asientos),
                    "columnas": len(sala.asientos[0]) if len(sala.asientos) > 0 else 0,
                    "tipo": sala.tipo
                })

class SistemaProductos:
    """Clase encargada de gestionar el inventario de la dulcería con almacenamiento en CSV."""
    def __init__(self, archivo_productos="productos.csv"):
        self.archivo_productos = os.path.join(os.path.dirname(__file__), archivo_productos)
        self.productos = {} # Diccionario para almacenar los productos en memoria
        self._cargar_productos()

    def _cargar_productos(self):
        """Carga los productos desde el archivo CVS si existe."""
        if not os.path.exists(self.archivo_productos):
            return
            
        with open(self.archivo_productos, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                p = Producto(
                    id_prod=row["id_producto"],
                    nombre=row["nombre"],
                    categoria=row["categoria"],
                    precio=float(row["precio"]),
                    stock=int(row["stock"])
                )
                self.productos[p.id_producto] = p

    def registrar_producto(self, id_producto, nombre, categoria, precio, stock):
        """Registra un nuevo producto y lo adjunta al final del CSV."""
        nuevo_producto = Producto(id_producto, nombre, categoria, float(precio), int(stock))
        self.productos[id_producto] = nuevo_producto
        
        archivo_existe = os.path.exists(self.archivo_productos)
        with open(self.archivo_productos, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_producto", "nombre", "categoria", "precio", "stock"])
            if not archivo_existe:
                writer.writeheader()
            writer.writerow({
                "id_producto": nuevo_producto.id_producto,
                "nombre": nuevo_producto.nombre,
                "categoria": nuevo_producto.categoria,
                "precio": nuevo_producto.precio,
                "stock": nuevo_producto.stock
            })
            
    def actualizar_csv_completo(self):
        """Sobrescribe el CSV completo si se edita o borra un producto."""
        with open(self.archivo_productos, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_producto", "nombre", "categoria", "precio", "stock"])
            writer.writeheader()
            for prod in self.productos.values():
                writer.writerow({
                    "id_producto": prod.id_producto,
                    "nombre": prod.nombre,
                    "categoria": prod.categoria,
                    "precio": prod.precio,
                    "stock": prod.stock
                })

class SistemaPeliculas:
    """Clase encargada de gestionar las películas con almacenamiento en CSV."""
    def __init__(self, archivo_peliculas="peliculas.csv"):
        self.archivo_peliculas = os.path.join(os.path.dirname(__file__), archivo_peliculas)
        self.peliculas = {} # Diccionario para almacenar las películas en memoria
        self._cargar_peliculas()

    def _cargar_peliculas(self):
        """Carga las películas desde el archivo CVS si existe."""
        if not os.path.exists(self.archivo_peliculas):
            return
            
        with open(self.archivo_peliculas, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                p = Pelicula(
                    id=row["id_pelicula"],
                    titulo=row["titulo"],
                    clasif=row["clasificacion"],
                    dura=row["duracion"],
                    genero=row["genero"],
                    sinopsis=row.get("sinopsis", ""),
                    direc_img=row.get("dir_img", "") # Puede venir vacío
                )
                self.peliculas[p.id_pelicula] = p

    def registrar_pelicula(self, id_pelicula, titulo, clasificacion, duracion, genero, sinopsis, dir_img=""):
        """Registra una nueva película y la adjunta al final del CSV."""
        nueva_pelicula = Pelicula(id_pelicula, titulo, clasificacion, duracion, genero, sinopsis, dir_img)
        self.peliculas[id_pelicula] = nueva_pelicula
        
        archivo_existe = os.path.exists(self.archivo_peliculas)
        with open(self.archivo_peliculas, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_pelicula", "titulo", "clasificacion", "duracion", "genero", "sinopsis", "dir_img"])
            if not archivo_existe:
                writer.writeheader()
            writer.writerow({
                "id_pelicula": nueva_pelicula.id_pelicula,
                "titulo": nueva_pelicula.titulo,
                "clasificacion": nueva_pelicula.clasificacion,
                "duracion": nueva_pelicula.duracion,
                "genero": nueva_pelicula.genero,
                "sinopsis": nueva_pelicula.sinopsis,
                "dir_img": nueva_pelicula.dir_img
            })
            
    def actualizar_csv_completo(self):
        """Sobrescribe el CSV completo si se edita o borra una película."""
        with open(self.archivo_peliculas, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_pelicula", "titulo", "clasificacion", "duracion", "genero", "sinopsis", "dir_img"])
            writer.writeheader()
            for pelicula in self.peliculas.values():
                writer.writerow({
                    "id_pelicula": pelicula.id_pelicula,
                    "titulo": pelicula.titulo,
                    "clasificacion": pelicula.clasificacion,
                    "duracion": pelicula.duracion,
                    "genero": pelicula.genero,
                    "sinopsis": pelicula.sinopsis,
                    "dir_img": pelicula.dir_img
                })

class SistemaFunciones:
    """Clase encargada de gestionar las funciones con almacenamiento en CSV."""
    def __init__(self, archivo_funciones="funciones.csv"):
        self.archivo_funciones = os.path.join(os.path.dirname(__file__), archivo_funciones)
        self.funciones = [] # Lista para almacenar las funciones
        self._cargar_funciones()

    def _cargar_funciones(self):
        if not os.path.exists(self.archivo_funciones):
            return
            
        with open(self.archivo_funciones, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                f = Funcion(
                    id_fun=row["id_funcion"],
                    id_pelicula=row["id_pelicula"],
                    id_sala=row["id_sala"],
                    dia=row.get("dia", "Lunes"), # Por retrocompatibilidad si el archivo es viejo
                    hora_ini=row["hora_inicio"]
                )
                self.funciones.append(f)

    def registrar_funcion(self, id_funcion, id_pelicula, id_sala, dia, hora_inicio):
        nueva_funcion = Funcion(id_funcion, id_pelicula, id_sala, dia, hora_inicio)
        self.funciones.append(nueva_funcion)
        
        archivo_existe = os.path.exists(self.archivo_funciones)
        with open(self.archivo_funciones, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_funcion", "id_pelicula", "id_sala", "dia", "hora_inicio"])
            if not archivo_existe:
                writer.writeheader()
            writer.writerow({
                "id_funcion": nueva_funcion.id_funcion,
                "id_pelicula": nueva_funcion.id_pelicula,
                "id_sala": nueva_funcion.id_sala,
                "dia": nueva_funcion.dia,
                "hora_inicio": nueva_funcion.hora_inicio
            })
            
    def actualizar_csv_completo(self):
        with open(self.archivo_funciones, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["id_funcion", "id_pelicula", "id_sala", "dia", "hora_inicio"])
            writer.writeheader()
            for func in self.funciones:
                writer.writerow({
                    "id_funcion": func.id_funcion,
                    "id_pelicula": func.id_pelicula,
                    "id_sala": func.id_sala,
                    "dia": func.dia,
                    "hora_inicio": func.hora_inicio
                })

# ============================================================
# NUEVAS CLASES PARA EL MÓDULO DE TAQUILLA
# ============================================================

class Venta:
    """Representa una venta de boletos realizada por un taquillero."""
    def __init__(self, id_venta, taquillero, id_funcion, asientos, total, fecha_hora):
        self.id_venta = id_venta
        self.taquillero = taquillero
        self.id_funcion = id_funcion
        self.asientos = asientos          
        self.total = float(total)
        self.fecha_hora = fecha_hora      

class SistemaVentas:
    """Gestiona el registro de ventas en ventas.csv."""
    PRECIO_BOLETO = 85.0 

    def __init__(self, archivo_ventas="ventas.csv"):
        self.archivo_ventas = os.path.join(os.path.dirname(__file__), archivo_ventas)
        self.ventas = []
        self._cargar_ventas()

    def _cargar_ventas(self):
        if not os.path.exists(self.archivo_ventas):
            return
        with open(self.archivo_ventas, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                v = Venta(
                    id_venta=row["id_venta"],
                    taquillero=row["taquillero"],
                    id_funcion=row["id_funcion"],
                    asientos=row["asientos"].split("|") if row["asientos"] else [],
                    total=float(row["total"]),
                    fecha_hora=row["fecha_hora"]
                )
                self.ventas.append(v)

    def registrar_venta(self, taquillero, id_funcion, asientos_lista):
        """Crea y persiste una nueva venta. Retorna el objeto Venta creado."""
        max_id = 0
        for v in self.ventas:
            if v.id_venta.startswith("V_"):
                try:
                    n = int(v.id_venta.split("_")[1])
                    if n > max_id: max_id = n
                except: pass
        nuevo_id = f"V_{max_id + 1}"
        total = len(asientos_lista) * self.PRECIO_BOLETO
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = Venta(nuevo_id, taquillero, id_funcion, asientos_lista, total, fecha_hora)
        self.ventas.append(nueva_venta)

        archivo_existe = os.path.exists(self.archivo_ventas)
        with open(self.archivo_ventas, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id_venta", "taquillero", "id_funcion", "asientos", "total", "fecha_hora"])
            if not archivo_existe:
                writer.writeheader()
            writer.writerow({
                "id_venta": nueva_venta.id_venta,
                "taquillero": nueva_venta.taquillero,
                "id_funcion": nueva_venta.id_funcion,
                "asientos": "|".join(nueva_venta.asientos),
                "total": nueva_venta.total,
                "fecha_hora": nueva_venta.fecha_hora
            })
        return nueva_venta

    def obtener_ventas_por_taquillero(self, nombre):
        return [v for v in self.ventas if v.taquillero == nombre]


class SistemaAsientos:
    """Persiste los asientos ocupados por función en asientos_reservados.csv."""
    def __init__(self, archivo="asientos_reservados.csv"):
        self.archivo = os.path.join(os.path.dirname(__file__), archivo)
        self.ocupados = {}
        self._cargar()

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_fun = row["id_funcion"]
                asiento = row["asiento"]
                if id_fun not in self.ocupados:
                    self.ocupados[id_fun] = set()
                self.ocupados[id_fun].add(asiento)

    def reservar(self, id_funcion, asientos_lista):
        """Marca los asientos como ocupados y los persiste."""
        if id_funcion not in self.ocupados:
            self.ocupados[id_funcion] = set()
        
        nuevos = [a for a in asientos_lista if a not in self.ocupados[id_funcion]]
        self.ocupados[id_funcion].update(nuevos)

        archivo_existe = os.path.exists(self.archivo)
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id_funcion", "asiento"])
            if not archivo_existe:
                writer.writeheader()
            for a in nuevos:
                writer.writerow({"id_funcion": id_funcion, "asiento": a})

    def obtener_ocupados(self, id_funcion):
        """Retorna el set de asientos ocupados para una función."""
        return self.ocupados.get(id_funcion, set())


# ============================================================
# CLASES PARA EL MÓDULO DE DULCERÍA
# ============================================================

class VentaDulceria:
    """Representa una venta en la dulcería."""
    def __init__(self, id_venta, dulcero, items, total, fecha_hora):
        self.id_venta = id_venta
        self.dulcero = dulcero
        # items: lista de dicts {"id_producto": ..., "nombre": ..., "cantidad": ..., "subtotal": ...}
        self.items = items
        self.total = float(total)
        self.fecha_hora = fecha_hora

class SistemaVentasDulceria:
    """Gestiona ventas de dulcería en ventas_dulceria.csv y descuenta stock."""
    def __init__(self, archivo="ventas_dulceria.csv"):
        self.archivo = os.path.join(os.path.dirname(__file__), archivo)
        self.ventas = []
        self._cargar()

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                v = VentaDulceria(
                    id_venta=row["id_venta"],
                    dulcero=row["dulcero"],
                    items=[],          # Se guarda resumen; no se deserializa detalle
                    total=float(row["total"]),
                    fecha_hora=row["fecha_hora"]
                )
                self.ventas.append(v)

    def registrar_venta(self, dulcero, items_carrito, sistema_productos):
        """
        items_carrito: lista de dicts {"id_producto", "nombre", "cantidad", "subtotal"}
        sistema_productos: instancia de SistemaProductos para descontar stock.
        Retorna el objeto VentaDulceria creado.
        """
        max_id = 0
        for v in self.ventas:
            if v.id_venta.startswith("VD_"):
                try:
                    n = int(v.id_venta.split("_")[1])
                    if n > max_id: max_id = n
                except: pass
        nuevo_id = f"VD_{max_id + 1}"
        total = sum(it["subtotal"] for it in items_carrito)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = VentaDulceria(nuevo_id, dulcero, items_carrito, total, fecha_hora)
        self.ventas.append(nueva_venta)

        # Descontar stock
        for it in items_carrito:
            prod = sistema_productos.productos.get(it["id_producto"])
            if prod:
                prod.stock = max(0, prod.stock - it["cantidad"])
        sistema_productos.actualizar_csv_completo()

        # Persistir venta (una fila por producto vendido)
        archivo_existe = os.path.exists(self.archivo)
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "id_venta", "dulcero", "id_producto", "nombre_producto",
                "cantidad", "subtotal", "total", "fecha_hora"
            ])
            if not archivo_existe:
                writer.writeheader()
            for it in items_carrito:
                writer.writerow({
                    "id_venta": nuevo_id,
                    "dulcero": dulcero,
                    "id_producto": it["id_producto"],
                    "nombre_producto": it["nombre"],
                    "cantidad": it["cantidad"],
                    "subtotal": it["subtotal"],
                    "total": total,
                    "fecha_hora": fecha_hora
                })
        return nueva_venta

