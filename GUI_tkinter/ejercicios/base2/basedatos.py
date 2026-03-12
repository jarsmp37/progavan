from supabase import create_client, Client
from backend import *
# pip install supabase

# Reemplaza estos valores con la URL y Key (anon public) de tu proyecto en Supabase
SUPABASE_URL = "pon tu direc"
SUPABASE_KEY = "pon tu key"

# Creamos el cliente global de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class GestorUsuarios:
    def __init__(self):
        self.lista_usuarios = []
        self.usuarios_nuevos = []  # Llevaremos rastro de los que insertemos en esta sesión
        
    def agregar_localmente(self, usuario):
        self.lista_usuarios.append(usuario)
        self.usuarios_nuevos.append(usuario)

    def cargar_desde_supabase(self):
        try:
            respuesta = supabase.table("usuarios").select("*").execute()
            datos = respuesta.data
            Usuario.lista = [] # Limpiamos la lista global del backend
            for val in datos:
                # Al instanciarlo, el __init__ del backend ya lo mete a Usuario.lista
                Usuario(val.get('nombre', ''), val.get('edad', 0), val.get('contraseña', ''))
            
            # Vaciamos usuarios_nuevos porque lo que acabamos de bajar ya está en la nube
            self.usuarios_nuevos = [] 
            print(f"Sincronizado: {len(Usuario.lista)} usuarios cargados.")
        except Exception as e:
            print("Error al cargar:", e)

    def guardar_en_supabase(self):
        """Ésta función se llamará al cerrar nuestra ventana visual"""
        if not self.usuarios_nuevos:
            print("No hay usuarios nuevos para enviar a Supabase.")
            return
            
        print(f"Subiendo {len(self.usuarios_nuevos)} nuevos usuarios a Supabase...")
        
        # Transformamos nuestra sub-lista de objetos nuevos a diccionarios
        lista_a_insertar = [u.to_dict() for u in self.usuarios_nuevos]
            
        try:
            # Un query '.insert()' manda a agregar varios registros en una sola operación (bulk insert)
            respuesta = supabase.table("usuarios").insert(lista_a_insertar).execute()
            print("¡Nuevos datos respaldados exitosamente a la base de datos remota!")
        except Exception as e:
            print("No se pudo guardar la información a Supabase:", e)