import customtkinter as ctk
from backend import *
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

def abrir_ventana_accion(titulo):
    nueva_ventana=ctk.CTkToplevel()
    nueva_ventana.title(titulo)
    nueva_ventana.after(0,lambda: nueva_ventana.state('zoomed'))
    nueva_ventana.grab_set()

    etiqueta1=ctk.CTkLabel(nueva_ventana,text=f"Módulo {titulo}")
    etiqueta1.pack(pady=10)

    boton_regresar=ctk.CTkButton(nueva_ventana,text="Volver al menu",command=nueva_ventana.destroy)
    boton_regresar.pack()



def mostrar_pantalla_admin(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Ventana Gestión Administrativa")
    
    label = ctk.CTkLabel(ventana, text="¡Bienvenido al Panel de Administrador!", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=60)

    frame_menu=ctk.CTkFrame(ventana,fg_color="transparent")
    frame_menu.pack(pady=10)

    boton_registro=ctk.CTkButton(frame_menu,text="Registrar usuarios",width=220,height=50,command=lambda: abrir_ventana_accion("Registrar usuarios"))
    boton_registro.grid(row=0,column=0,padx=10,pady=10)

    boton_modusu=ctk.CTkButton(frame_menu,text="Modificar usuarios",width=220,height=50,command=lambda: abrir_ventana_accion("Modificar usuarios"))
    boton_modusu.grid(row=0,column=1,padx=10,pady=10)

    boton_lisusu=ctk.CTkButton(frame_menu,text="Lista de usuarios",width=220,height=50,command=lambda: abrir_ventana_accion("Lista de usuarios"))
    boton_lisusu.grid(row=1,column=0,padx=10,pady=10)

    boton_crearsalas=ctk.CTkButton(frame_menu,text="Crear salas",width=220,height=50,command=lambda: abrir_ventana_accion("Crear salas"))
    boton_crearsalas.grid(row=1,column=1,padx=10,pady=10)

    boton_lissalas=ctk.CTkButton(frame_menu,text="Lista de salas",width=220,height=50,command=lambda: abrir_ventana_accion("Lista de salas"))
    boton_lissalas.grid(row=2,column=0,padx=10,pady=10)

    boton_crearprod=ctk.CTkButton(frame_menu,text="Crear producto",width=220,height=50,command=lambda: abrir_ventana_accion("Crear producto"))
    boton_crearprod.grid(row=2,column=1,padx=10,pady=10)

    boton_lisprod=ctk.CTkButton(frame_menu,text="Lista de productos",width=220,height=50,command=lambda: abrir_ventana_accion("Lista de productos"))
    boton_lisprod.grid(row=3,column=0,padx=10,pady=10)

    boton_cartelera=ctk.CTkButton(frame_menu,text="Cartelera",width=220,height=50,command=lambda: abrir_ventana_accion("Cartelera"))
    boton_cartelera.grid(row=3,column=1,padx=10,pady=10)
    
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
    ventana.geometry("600x600")
    ventana.configure(fg_color=COLOR_FONDO_PRINCIPAL)
    ventana.title("Cargando Sistema...")
    mostrar_pantalla_login(ventana)
    
    ventana.mainloop()

iniciar_aplicacion()