import customtkinter as ctk
from backend import *
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

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
def crear_ventana_modificar(usuario, callback_actualizar):
    ventana_edit = ctk.CTkToplevel()
    ventana_edit.title(f"Modificar: {usuario.nombre}")
    ventana_edit.geometry("400x400")
    ventana_edit.grab_set() # Bloquea la ventana de atrás hasta cerrar esta

    ctk.CTkLabel(ventana_edit, text="Editar Usuario", font=("Roboto", 18, "bold")).pack(pady=20)

    # Campos con la información actual
    entry_nom = ctk.CTkEntry(ventana_edit, width=250)
    entry_nom.insert(0, usuario.nombre)
    entry_nom.configure(state="disabled")
    entry_nom.pack(pady=10)

    combo_rol = ctk.CTkComboBox(ventana_edit, values=["administrador", "taquillero", "dulcero"], width=250)
    combo_rol.set(usuario.rol)
    combo_rol.pack(pady=10)

    entry_pass = ctk.CTkEntry(ventana_edit, placeholder_text="Nueva contraseña", width=250)
    entry_pass.insert(0, usuario.password)
    entry_pass.pack(pady=10)

    def guardar_cambios():
        
        usuario.rol = combo_rol.get()
        usuario.password = entry_pass.get()
        messagebox.showinfo("Éxito", f"Usuario {usuario.nombre} actualizado correctamente.")
        
        callback_actualizar() # Refresca la tabla de la ventana anterior
        ventana_edit.destroy() # Cierra la ventana actual

    btn_guardar = ctk.CTkButton(ventana_edit, text="Guardar Cambios", fg_color="#10b981", command=guardar_cambios)
    btn_guardar.pack(pady=20)

    btn_cancelar = ctk.CTkButton(ventana_edit, text="Cancelar", fg_color="#64748b", command=ventana_edit.destroy)
    btn_cancelar.pack()

def abrir_ventana_accion(titulo):
    nueva_ventana=ctk.CTkToplevel()
    nueva_ventana.title(titulo)
    nueva_ventana.after(0,lambda: nueva_ventana.state('zoomed'))
    nueva_ventana.grab_set()
    

    ctk.CTkLabel(nueva_ventana, text=f"Módulo: {titulo}", font=("Roboto", 20, "bold")).pack(pady=10)
    #Acá se verifica que va a contener la ventana según la opción elegida
    if titulo == "Gestión de usuarios":
        
        frame_form = ctk.CTkFrame(nueva_ventana)
        frame_form.pack(pady=10, padx=20, fill="x")

        entry_nom = ctk.CTkEntry(frame_form, placeholder_text="Nombre completo")
        entry_nom.grid(row=0, column=0, padx=10, pady=10)

        combo_rol = ctk.CTkComboBox(frame_form, values=["administrador", "taquillero", "dulcero"])
        combo_rol.grid(row=0, column=1, padx=10, pady=10)

        entry_pass = ctk.CTkEntry(frame_form, placeholder_text="Contraseña")
        entry_pass.grid(row=1, column=0, padx=10, pady=10)

        # --- TABLA DE USUARIOS (Usando Treeview de Tkinter estándar) ---
        columnas = ("nombre", "rol")
        tabla = ttk.Treeview(nueva_ventana, columns=columnas, show="headings", height=8)
        tabla.heading("nombre", text="Nombre del Usuario")
        tabla.heading("rol", text="Rol / Puesto")
        tabla.pack(pady=20, padx=20, fill="both", expand=True)

        frame_acciones_lista = ctk.CTkFrame(nueva_ventana, fg_color="transparent")
        frame_acciones_lista.pack(pady=10)

        def abrir_ventana_edicion():
            # Obtener el elemento seleccionado de la tabla
            seleccion = tabla.selection()
            if not seleccion:
                print("Por favor, selecciona un usuario de la lista")
                return
            
            # Extraer datos de la fila
            item = tabla.item(seleccion)
            nombre_usuario = item['values'][0]
            usuario_obj = auth_sys.usuarios.get(nombre_usuario)

            if usuario_obj:
                crear_ventana_modificar(usuario_obj, actualizar_tabla)
            

        btn_modificar = ctk.CTkButton(frame_acciones_lista, text="Modificar Seleccionado", 
                                      fg_color="#f59e0b", hover_color="#d97706",
                                      command=abrir_ventana_edicion)
        btn_modificar.grid(row=0, column=0, padx=10)

        def actualizar_tabla():
            # Limpiar tabla actual
            for item in tabla.get_children():
                tabla.delete(item)
            # Cargar desde auth_sys
            for nombre, obj in auth_sys.usuarios.items():
                tabla.insert("", "end", values=(obj.nombre, obj.rol))

        def guardar_datos():
            nom = entry_nom.get()
            rol = combo_rol.get()
            pas = entry_pass.get()
            
            if nom and pas:
                auth_sys.registrar_usuario(nom, rol, pas)
                actualizar_tabla()
                entry_nom.delete(0, 'end')
                entry_pass.delete(0, 'end')
            else:
                print("Error: Llena todos los campos")

        btn_guardar = ctk.CTkButton(frame_form, text="Guardar Usuario", command=guardar_datos)
        btn_guardar.grid(row=1, column=1, padx=10, pady=10)

        def eliminar_usuario():
            seleccion = tabla.selection()
            if not seleccion:
                from tkinter import messagebox
                messagebox.showwarning("Atención", "Selecciona un usuario para eliminar")
                return
            
            # Obtener el nombre del usuario seleccionado
            item = tabla.item(seleccion)
            nombre_usuario = item['values'][0]
            
            from tkinter import messagebox
            confirmar = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar a {nombre_usuario}?")
            
            if confirmar:
                # 1. Eliminar del diccionario en memoria
                if nombre_usuario in auth_sys.usuarios:
                    del auth_sys.usuarios[nombre_usuario]
                    
                    # 2. Actualizar el archivo CSV (Usando el método nuevo del backend)
                    auth_sys.actualizar_csv_completo()
                    
                    # 3. Refrescar la tabla visual
                    actualizar_tabla()
                    messagebox.showinfo("Eliminado", "Usuario borrado con éxito")

        
        btn_eliminar = ctk.CTkButton(frame_acciones_lista, text="Eliminar Seleccionado", 
                                     fg_color="#ef4444", hover_color="#b91c1c",
                                     command=eliminar_usuario)
        btn_eliminar.grid(row=0, column=1, padx=10)

        
        actualizar_tabla()

    btn_salir = ctk.CTkButton(nueva_ventana, text="Cerrar", fg_color="gray", command=nueva_ventana.destroy)
    btn_salir.pack(pady=10)




def mostrar_pantalla_admin(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Ventana Gestión Administrativa")
    
    label = ctk.CTkLabel(ventana, text="¡Bienvenido al Panel de Administrador!", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=60)

    frame_menu=ctk.CTkFrame(ventana,fg_color="transparent")
    frame_menu.pack(pady=10)

    boton_registro=ctk.CTkButton(frame_menu,text="Gestión de usuarios",width=220,height=50,command=lambda: abrir_ventana_accion("Gestión de usuarios"))
    boton_registro.grid(row=0,column=0,padx=10,pady=10)

    boton_crearsalas=ctk.CTkButton(frame_menu,text="Gestión de salas",width=220,height=50,command=lambda: abrir_ventana_accion("Gestión de salas"))
    boton_crearsalas.grid(row=1,column=0,padx=10,pady=10)

    boton_crearprod=ctk.CTkButton(frame_menu,text="Gestión de productos",width=220,height=50,command=lambda: abrir_ventana_accion("Gestión de productos"))
    boton_crearprod.grid(row=2,column=0,padx=10,pady=10)
    
    boton_crearpelis=ctk.CTkButton(frame_menu,text="Gestión de peliculas",width=220,height=50,command=lambda: abrir_ventana_accion("Gestión de peliculas"))
    boton_crearpelis.grid(row=3,column=0,padx=10,pady=10)

    boton_cartelera=ctk.CTkButton(frame_menu,text="Crear funciones",width=220,height=50,command=lambda: abrir_ventana_accion("Crear funciones"))
    boton_cartelera.grid(row=4,column=0,padx=10,pady=10)
    
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
    #Código para abrir imágenes guardadas en la misma carpeta
    carpeta_actual = os.path.dirname(__file__)
    ruta_relativa_imagen = os.path.join(carpeta_actual, "logocine.png")
    imagen = Image.open(ruta_relativa_imagen)
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