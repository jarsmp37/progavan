import customtkinter as ctk
from backend import SistemaAutenticacion
from PIL import Image

# ========================================================================
# CONFIGURACIÓN DE DISEÑO (Colores y Apariencia)
# ========================================================================
COLOR_FONDO_PRINCIPAL = "#0f172a"
COLOR_BOTON_AZUL_REY = "#002366"
COLOR_BOTON_HOVER = "#003bba"
COLOR_CUADRO_IMAGEN = "#1e293b"

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

# Instancia global del backend
auth_sys = SistemaAutenticacion()

# ========================================================================
# FUNCIONES AUXILIARES
# ========================================================================

def limpiar_pantalla(ventana):
    """Elimina todos los widgets de la ventana actual."""
    for widget in ventana.winfo_children():
        widget.destroy()

def _crear_boton_cerrar_sesion(ventana):
    """Crea el botón para regresar al login."""
    btn_cerrar = ctk.CTkButton(
        ventana, 
        text="Cerrar Sesión", 
        fg_color="#dc2626", 
        hover_color="#3c0ed3",
        font=("Roboto", 14, "bold"),
        command=lambda: mostrar_pantalla_login(ventana)
    )
    btn_cerrar.pack(pady=20)

# ========================================================================
# VISTAS (PANTALLAS)
# ========================================================================

def mostrar_pantalla_admin(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Ventana con administrador")
    
    label = ctk.CTkLabel(ventana, text="¡Bienvenido al Panel de Administrador!", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=60)
    
    _crear_boton_cerrar_sesion(ventana)

def mostrar_pantalla_taquillero(ventana):
    limpiar_pantalla(ventana)
    ventana.title("taquillero")
    
    label = ctk.CTkLabel(ventana, text="Módulo de Ventas de Taquilla", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=60)
    
    _crear_boton_cerrar_sesion(ventana)

def mostrar_pantalla_dulcero(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Dulcería")
    
    label = ctk.CTkLabel(ventana, text="Hola, Dulcero.", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=60)
    
    _crear_boton_cerrar_sesion(ventana)

def mostrar_pantalla_login(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Sistema de Cine - Iniciar Sesión")

    frame_login = ctk.CTkFrame(ventana, corner_radius=20, fg_color="#1e293b")
    frame_login.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    label_titulo = ctk.CTkLabel(frame_login, text="Bienvenido a LoboCine", font=("Roboto", 24, "bold"), text_color="white")
    label_titulo.pack(pady=(30, 10), padx=40)

    frame_imagen = ctk.CTkFrame(frame_login, width=300, height=150, fg_color=COLOR_CUADRO_IMAGEN, corner_radius=10)
    frame_imagen.pack(pady=10)
    
    imagen = Image.open("C:/Users/Jaime/Documents/GitHub/progavan/GUI_tkinter/cine/logocine.png")
    mi_imagen=ctk.CTkImage(light_image=imagen,dark_image=imagen, size=(150,150))
    label_imagen = ctk.CTkLabel(frame_imagen,image=mi_imagen, text="", font=("Roboto", 12, "italic"), text_color="gray")
    label_imagen.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    entry_usuario = ctk.CTkEntry(frame_login, placeholder_text="Nombre de usuario", width=250, height=40, corner_radius=10)
    entry_usuario.pack(pady=10)

    entry_password = ctk.CTkEntry(frame_login, placeholder_text="Contraseña", show="*", width=250, height=40, corner_radius=10)
    entry_password.pack(pady=10)

    label_error = ctk.CTkLabel(frame_login, text="", text_color="#ef4444", font=("Roboto", 12))
    label_error.pack(pady=5)

    def evento_login():
        usuario_texto = entry_usuario.get()
        password_texto = entry_password.get()

        rol_usuario = auth_sys.autenticar(usuario_texto, password_texto)

        if rol_usuario == "administrador":
            mostrar_pantalla_admin(ventana)
        elif rol_usuario == "taquillero":
            mostrar_pantalla_taquillero(ventana)
        elif rol_usuario == "dulcero":
            mostrar_pantalla_dulcero(ventana)
        else:
            label_error.configure(text="Datos incorrectos o usuario no existe.")

    btn_ingresar = ctk.CTkButton(
        frame_login, text="Entrar", width=250, height=40, corner_radius=10,
        fg_color=COLOR_BOTON_AZUL_REY, hover_color=COLOR_BOTON_HOVER,
        font=("Roboto", 16, "bold"), command=evento_login
    )
    btn_ingresar.pack(pady=(10, 30))

def iniciar_aplicacion():
    ventana = ctk.CTk()
    ventana.geometry("600x500")
    ventana.configure(fg_color=COLOR_FONDO_PRINCIPAL)
    ventana.title("Cargando Sistema...")
    mostrar_pantalla_login(ventana)
    
    ventana.mainloop()

iniciar_aplicacion()