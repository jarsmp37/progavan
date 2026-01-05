#  Importa la clase Modelo
from usuario import Usuario

#  Importa la clase Manejador
from firestore_manager import FirestoreManager


# --- Configuración (ajusta tu ruta real) ---
RUTA_CREDENTIALS = 'C:/Users/Jaime/Documents/Ciencia de datos/proyectos alumnos/base1-78ad0-firebase-adminsdk-fbsvc-9bf9711125.json'
NOMBRE_COLECCION = 'estudiantes'


def ejecutar_programa():
    # 1. Crear el gestor de la base de datos
    # Se inicializa la conexión a Firebase aquí
    gestor_db = FirestoreManager(RUTA_CREDENTIALS, NOMBRE_COLECCION)

    print("\n--- Iniciando registro de usuarios ---")
    
    # 2. Crear un objeto Usuario (registro 1)
    usuario_1 = Usuario(
        nombre="Sofía M.",
        color="Morado",
        edad=20
    )

    # 3. Llamar al método del Manejador para guardar el Modelo
    gestor_db.registrar_usuario(usuario_1)
    
    # 4. Crear otro objeto Usuario (registro 2)
    usuario_2 = Usuario(
        nombre="Ricardo Z.",
        color="Naranja",
        edad=22
    )
    
    # 5. Llamar al método del Manejador para guardar el Modelo
    gestor_db.registrar_usuario(usuario_2)


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_programa()