# ==================================================
# Contenido de: firestore_manager.py
# ==================================================

# 1. 🔴 CORRECCIÓN: Importación de la clase Modelo (Usuario)
from usuario import Usuario 

# Importaciones de Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import _apps # Usado para verificar si la app ya fue inicializada

class FirestoreManager:
    """
    Gestiona la conexión y las operaciones de persistencia de datos en Firestore.
    """
    def __init__(self, ruta_credenciales_json, coleccion='usuarios'):
        # 2. 🟢 CORRECCIÓN: Inicialización y asignación de atributos
        try:
            cred = credentials.Certificate(ruta_credenciales_json)
            
            # Inicializa la app solo si no lo ha sido ya
            if not _apps:
                firebase_admin.initialize_app(cred)
            
            print("Firebase Admin SDK inicializado.")
            
            # Obtiene el cliente de Firestore
            self.db = firestore.client()
            
            # Asigna la referencia a la colección (self.coleccion_ref)
            self.coleccion_ref = self.db.collection(coleccion)
            
        except FileNotFoundError:
            print(f"❌ ERROR: No se encontró el archivo de credenciales en la ruta: {ruta_credenciales_json}")
            # Si hay error, no asignamos self.coleccion_ref
            self.coleccion_ref = None 
            
        except Exception as e:
            print(f"❌ ERROR FATAL en la inicialización de Firebase: {e}")
            # Si hay error, no asignamos self.coleccion_ref
            self.coleccion_ref = None

    # 3. 🟢 CORRECCIÓN: Definición correcta del método con indentación
    def registrar_usuario(self, usuario: Usuario):
        """
        Guarda un objeto Usuario como un documento en Firestore.
        """
        # Verifica si la inicialización fue exitosa antes de proceder
        if not self.coleccion_ref:
            print("❌ Registro fallido: La conexión a Firebase no se pudo establecer correctamente.")
            return False
            
        datos_usuario = usuario.a_diccionario()
        # Creamos un ID único usando el nombre
        nombre_id = usuario.nombre.replace(" ", "_").lower() 

        print(f"Intentando registrar a: {usuario.nombre}...")
        
        try:
            # El método 'set' crea o actualiza el documento
            self.coleccion_ref.document(nombre_id).set(datos_usuario)
            print(f"✅ Registro exitoso para {usuario.nombre} en Firestore.")
            return True
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
            return False