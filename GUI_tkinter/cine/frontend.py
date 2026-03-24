import customtkinter as ctk
from backend import *
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os
from datetime import datetime, timedelta

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
salas_sys = SistemaSalas()
productos_sys = SistemaProductos()
peliculas_sys = SistemaPeliculas()
funciones_sys = SistemaFunciones()
ventas_sys = SistemaVentas()
asientos_sys = SistemaAsientos()
ventas_dulceria_sys = SistemaVentasDulceria()
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
            item = tabla.item(seleccion[0])
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
            item = tabla.item(seleccion[0])
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
        
    elif titulo == "Gestión de salas":
        frame_form = ctk.CTkFrame(nueva_ventana)
        frame_form.pack(pady=10, padx=20, fill="x")

        entry_num = ctk.CTkEntry(frame_form, placeholder_text="Número Sala")
        entry_num.grid(row=0, column=0, padx=10, pady=10)

        entry_fila = ctk.CTkEntry(frame_form, placeholder_text="Nº de Filas")
        entry_fila.grid(row=0, column=1, padx=10, pady=10)
        
        entry_columna = ctk.CTkEntry(frame_form, placeholder_text="Nº de Columnas")
        entry_columna.grid(row=0, column=2, padx=10, pady=10)

        combo_tipo = ctk.CTkComboBox(frame_form, values=["Estándar", "3D", "VIP", "IMAX"])
        combo_tipo.grid(row=1, column=0, padx=10, pady=10)

        #con esto se agranda la letra de la tabla
        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Roboto", 16), rowheight=30)
        estilo.configure("Treeview.Heading", font=("Roboto", 13, "bold"))

        # Anotación: Visualizamos las salas mediante una tabla TreeView
        columnas_salas = ("idsala","numero","tipo", "asientos")
        tabla_salas = ttk.Treeview(nueva_ventana, columns=columnas_salas, show="headings", height=8)
        tabla_salas.heading("idsala", text="ID de Sala")
        tabla_salas.heading("numero", text="Número de Sala")
        tabla_salas.heading("tipo", text="Tipo Sala")
        tabla_salas.heading("asientos", text="Total Asientos (F x C)")
        tabla_salas.pack(pady=20, padx=20, fill="both", expand=True)
        
        frame_acciones_lista = ctk.CTkFrame(nueva_ventana, fg_color="transparent")
        frame_acciones_lista.pack(pady=10)

        def actualizar_tabla_salas():
            for item in tabla_salas.get_children():
                tabla_salas.delete(item)
            for num, obj in salas_sys.salas.items():
                dim = f"{len(obj.asientos) * len(obj.asientos[0]) if obj.asientos else 0}"
                tabla_salas.insert("", "end", values=(obj.idsala, obj.numero, obj.tipo, dim))

        def guardar_ensalas():
            # Anotación: Auto-generar id de la sala (Ej: S_1, S_2)
            max_id = 0
            for obj in salas_sys.salas.values():
                if obj.idsala.startswith("S_"):
                    try:
                        num_v = int(obj.idsala.split("_")[1])
                        if num_v > max_id: max_id = num_v
                    except: pass
            ids = f"S_{max_id + 1}"
            
            num = entry_num.get()
            f = entry_fila.get()
            c = entry_columna.get()
            t = combo_tipo.get()
            
            if num and f and c:
                try:
                    salas_sys.registrar_sala(ids, num, f, c, t)
                    actualizar_tabla_salas()
                    entry_num.delete(0, 'end')
                    entry_fila.delete(0, 'end')
                    entry_columna.delete(0, 'end')
                except ValueError:
                    messagebox.showerror("Error", "Filas y columnas deben ser números enteros.")
            else:
                messagebox.showwarning("Atención", "Llena todos los campos.")

        btn_guardar_s = ctk.CTkButton(frame_form, text="Guardar Sala", command=guardar_ensalas)
        btn_guardar_s.grid(row=1, column=2, padx=10, pady=10)

        def eliminar_sala():
            seleccion = tabla_salas.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una sala para eliminar")
                return
            item = tabla_salas.item(seleccion[0])
            num_sala = str(item['values'][1])
            
            if messagebox.askyesno("Confirmar", f"¿Eliminar sala N° {num_sala}?"):
                if num_sala in salas_sys.salas:
                    del salas_sys.salas[num_sala]
                    salas_sys.actualizar_csv_completo()
                    actualizar_tabla_salas()
                    messagebox.showinfo("Eliminado", "Sala eliminada con éxito")
        
        btn_eliminar_s = ctk.CTkButton(frame_acciones_lista, text="Eliminar Sala", 
                                     fg_color="#ef4444", hover_color="#b91c1c",
                                     command=eliminar_sala)
        btn_eliminar_s.grid(row=0, column=1, padx=10)
        
        def abrir_modificar_sala():
            seleccion = tabla_salas.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una sala a editar")
                return
            
            item = tabla_salas.item(seleccion[0])
            num_sala_antiguo = str(item['values'][1])
            sala_obj = salas_sys.salas.get(num_sala_antiguo)

            if sala_obj:
                vent_edit_s = ctk.CTkToplevel()
                vent_edit_s.title("Modificar Sala")
                vent_edit_s.geometry("350x450")
                vent_edit_s.grab_set()

                ctk.CTkLabel(vent_edit_s, text=f"Modificar Sala (ID: {sala_obj.idsala})", font=("Roboto", 16, "bold")).pack(pady=10)
                
                ctk.CTkLabel(vent_edit_s, text="Número Sala:").pack()
                entry_m_num = ctk.CTkEntry(vent_edit_s, width=200)
                entry_m_num.insert(0, str(sala_obj.numero))
                entry_m_num.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_s, text="Filas:").pack()
                entry_m_f = ctk.CTkEntry(vent_edit_s, width=200)
                entry_m_f.insert(0, str(len(sala_obj.asientos)))
                entry_m_f.pack(pady=5)

                ctk.CTkLabel(vent_edit_s, text="Columnas:").pack()
                entry_m_c = ctk.CTkEntry(vent_edit_s, width=200)
                entry_m_c.insert(0, str(len(sala_obj.asientos[0]) if sala_obj.asientos else 0))
                entry_m_c.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_s, text="Tipo:").pack()
                combo_m_t = ctk.CTkComboBox(vent_edit_s, values=["Estándar", "3D", "VIP", "IMAX"], width=200)
                combo_m_t.set(sala_obj.tipo)
                combo_m_t.pack(pady=5)

                def guardar_mod_sala():
                    n_num = entry_m_num.get()
                    n_f = entry_m_f.get()
                    n_c = entry_m_c.get()
                    n_tipo = combo_m_t.get()
                    
                    if not (n_num and n_f and n_c):
                        messagebox.showwarning("Atención", "Llena todos los campos")
                        return
                    
                    try:
                        f_int = int(n_f)
                        c_int = int(n_c)
                    except ValueError:
                        messagebox.showerror("Error", "Filas y columnas deben ser enteros")
                        return

                    
                    sala_obj.numero = n_num
                    sala_obj.tipo = n_tipo
                    
                    sala_obj.asientos = [[False for _ in range(c_int)] for _ in range(f_int)]
                    if n_num != num_sala_antiguo:
                        salas_sys.salas[n_num] = sala_obj
                        if num_sala_antiguo in salas_sys.salas:
                            del salas_sys.salas[num_sala_antiguo]

                    salas_sys.actualizar_csv_completo()
                    actualizar_tabla_salas()
                    vent_edit_s.destroy()
                    messagebox.showinfo("Modificada", "Se ha modificado la sala correctamente")

                ctk.CTkButton(vent_edit_s, text="Guardar Cambios", fg_color="#10b981", command=guardar_mod_sala).pack(pady=15)
                ctk.CTkButton(vent_edit_s, text="Cancelar", fg_color="#64748b", command=vent_edit_s.destroy).pack(pady=5)

        btn_modificar_s = ctk.CTkButton(frame_acciones_lista, text="Modificar Seleccionado", 
                                      fg_color="#f59e0b", hover_color="#d97706",
                                      command=abrir_modificar_sala)
        btn_modificar_s.grid(row=0, column=0, padx=10)

        actualizar_tabla_salas()

    elif titulo == "Gestión de productos":
        frame_form = ctk.CTkFrame(nueva_ventana)
        frame_form.pack(pady=10, padx=20, fill="x")

        entry_nombre = ctk.CTkEntry(frame_form, placeholder_text="Nombre Producto")
        entry_nombre.grid(row=0, column=0, padx=10, pady=10)

        combo_categoria = ctk.CTkComboBox(frame_form, values=["Bebidas", "Dulces", "Palomitas", "Snacks"])
        combo_categoria.grid(row=0, column=1, padx=10, pady=10)
        
        entry_precio = ctk.CTkEntry(frame_form, placeholder_text="Precio")
        entry_precio.grid(row=0, column=2, padx=10, pady=10)

        entry_stock = ctk.CTkEntry(frame_form, placeholder_text="Stock (Cantidad)")
        entry_stock.grid(row=1, column=0, padx=10, pady=10)

        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Roboto", 16), rowheight=30)
        estilo.configure("Treeview.Heading", font=("Roboto", 13, "bold"))

        columnas_prods = ("id_producto", "nombre", "categoria", "precio", "stock")
        tabla_prods = ttk.Treeview(nueva_ventana, columns=columnas_prods, show="headings", height=8)
        tabla_prods.heading("id_producto", text="ID")
        tabla_prods.heading("nombre", text="Nombre")
        tabla_prods.heading("categoria", text="Categoría")
        tabla_prods.heading("precio", text="Precio")
        tabla_prods.heading("stock", text="Stock")
        
        tabla_prods.column("id_producto", width=80)
        tabla_prods.column("precio", width=100)
        tabla_prods.column("stock", width=100)
        tabla_prods.pack(pady=20, padx=20, fill="both", expand=True)
        
        frame_acciones_lista = ctk.CTkFrame(nueva_ventana, fg_color="transparent")
        frame_acciones_lista.pack(pady=10)

        def actualizar_tabla_prods():
            for item in tabla_prods.get_children():
                tabla_prods.delete(item)
            for id_p, obj in productos_sys.productos.items():
                tabla_prods.insert("", "end", values=(obj.id_producto, obj.nombre, obj.categoria, f"${obj.precio:.2f}", obj.stock))

        def guardar_en_prods():
            max_id = 0
            for obj in productos_sys.productos.values():
                if obj.id_producto.startswith("P_"):
                    try:
                        num_v = int(obj.id_producto.split("_")[1])
                        if num_v > max_id: max_id = num_v
                    except: pass
            id_gen = f"P_{max_id + 1}"
            
            n = entry_nombre.get()
            cat = combo_categoria.get()
            p = entry_precio.get()
            s = entry_stock.get()
            
            if n and cat and p and s:
                try:
                    p_float = float(p)
                    s_int = int(s)
                    productos_sys.registrar_producto(id_gen, n, cat, p_float, s_int)
                    actualizar_tabla_prods()
                    entry_nombre.delete(0, 'end')
                    entry_precio.delete(0, 'end')
                    entry_stock.delete(0, 'end')
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número decimal y el stock entero.")
            else:
                messagebox.showwarning("Atención", "Llena todos los campos.")

        btn_guardar_p = ctk.CTkButton(frame_form, text="Guardar Producto", command=guardar_en_prods)
        btn_guardar_p.grid(row=1, column=1, padx=10, pady=10)

        def eliminar_producto():
            seleccion = tabla_prods.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona un producto para eliminar")
                return
            item = tabla_prods.item(seleccion[0])
            id_p = str(item['values'][0])
            nom_p = str(item['values'][1])
            
            if messagebox.askyesno("Confirmar", f"¿Eliminar producto {nom_p}?"):
                if id_p in productos_sys.productos:
                    del productos_sys.productos[id_p]
                    productos_sys.actualizar_csv_completo()
                    actualizar_tabla_prods()
                    messagebox.showinfo("Eliminado", "Producto eliminado con éxito")
        
        btn_eliminar_p = ctk.CTkButton(frame_acciones_lista, text="Eliminar Producto", 
                                     fg_color="#ef4444", hover_color="#b91c1c",
                                     command=eliminar_producto)
        btn_eliminar_p.grid(row=0, column=1, padx=10)
        
        def abrir_modificar_producto():
            seleccion = tabla_prods.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona un producto a editar")
                return
            
            item = tabla_prods.item(seleccion[0])
            id_p_antiguo = str(item['values'][0])
            prod_obj = productos_sys.productos.get(id_p_antiguo)

            if prod_obj:
                vent_edit_p = ctk.CTkToplevel()
                vent_edit_p.title("Modificar Producto")
                vent_edit_p.geometry("350x450")
                vent_edit_p.grab_set()

                ctk.CTkLabel(vent_edit_p, text=f"Modificar {prod_obj.nombre} (ID: {prod_obj.id_producto})", font=("Roboto", 16, "bold")).pack(pady=10)
                
                ctk.CTkLabel(vent_edit_p, text="Nombre:").pack()
                entry_m_nom = ctk.CTkEntry(vent_edit_p, width=200)
                entry_m_nom.insert(0, prod_obj.nombre)
                entry_m_nom.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_p, text="Categoría:").pack()
                combo_m_cat = ctk.CTkComboBox(vent_edit_p, values=["Bebidas", "Dulces", "Palomitas", "Snacks"], width=200)
                combo_m_cat.set(prod_obj.categoria)
                combo_m_cat.pack(pady=5)

                ctk.CTkLabel(vent_edit_p, text="Precio:").pack()
                entry_m_pre = ctk.CTkEntry(vent_edit_p, width=200)
                entry_m_pre.insert(0, str(prod_obj.precio))
                entry_m_pre.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_p, text="Stock:").pack()
                entry_m_stk = ctk.CTkEntry(vent_edit_p, width=200)
                entry_m_stk.insert(0, str(prod_obj.stock))
                entry_m_stk.pack(pady=5)

                def guardar_mod_producto():
                    n_nom = entry_m_nom.get()
                    n_cat = combo_m_cat.get()
                    n_pre = entry_m_pre.get()
                    n_stk = entry_m_stk.get()
                    
                    if not (n_nom and n_cat and n_pre and n_stk):
                        messagebox.showwarning("Atención", "Llena todos los campos")
                        return
                    
                    try:
                        p_float = float(n_pre)
                        s_int = int(n_stk)
                    except ValueError:
                        messagebox.showerror("Error", "Precio numérico decimal, stock numérico entero.")
                        return

                    prod_obj.nombre = n_nom
                    prod_obj.categoria = n_cat
                    prod_obj.precio = p_float
                    prod_obj.stock = s_int
                    
                    productos_sys.actualizar_csv_completo()
                    actualizar_tabla_prods()
                    vent_edit_p.destroy()
                    messagebox.showinfo("Modificado", "Se ha modificado el producto correctamente")

                ctk.CTkButton(vent_edit_p, text="Guardar Cambios", fg_color="#10b981", command=guardar_mod_producto).pack(pady=15)
                ctk.CTkButton(vent_edit_p, text="Cancelar", fg_color="#64748b", command=vent_edit_p.destroy).pack(pady=5)

        btn_modificar_p = ctk.CTkButton(frame_acciones_lista, text="Modificar Seleccionado", 
                                      fg_color="#f59e0b", hover_color="#d97706",
                                      command=abrir_modificar_producto)
        btn_modificar_p.grid(row=0, column=0, padx=10)

        actualizar_tabla_prods()

    elif titulo == "Gestión de peliculas":
        # Directorio base para las carátulas/pósters
        carpeta_caratulas = os.path.join(os.path.dirname(__file__), "caratulas")
        if not os.path.exists(carpeta_caratulas):
            os.makedirs(carpeta_caratulas)

        frame_form = ctk.CTkFrame(nueva_ventana)
        frame_form.pack(pady=10, padx=20, fill="x")

        entry_titulo = ctk.CTkEntry(frame_form, placeholder_text="Título de Película")
        entry_titulo.grid(row=0, column=0, padx=10, pady=10)

        combo_clasif = ctk.CTkComboBox(frame_form, values=["AA", "A", "B", "B15", "C"])
        combo_clasif.grid(row=0, column=1, padx=10, pady=10)
        
        entry_dura = ctk.CTkEntry(frame_form, placeholder_text="Duración (minutos)")
        entry_dura.grid(row=0, column=2, padx=10, pady=10)

        combo_genero = ctk.CTkComboBox(frame_form, values=["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción", "Infantil", "Romance", "Documental"])
        combo_genero.set("Acción")
        combo_genero.grid(row=1, column=0, padx=10, pady=10)

        textbox_sinopsis = ctk.CTkTextbox(frame_form, height=60, width=200)
        textbox_sinopsis.insert("0.0", "Escribe la sinopsis aquí...")
        textbox_sinopsis.grid(row=1, column=1, padx=10, pady=10)

        ruta_img_temp = {"path": ""}
        label_img_info = ctk.CTkLabel(frame_form, text="Sin póster", text_color="gray", font=("Roboto", 12, "italic"))
        label_img_info.grid(row=1, column=2, padx=10, pady=5)

        def seleccionar_imagen():
            ruta = filedialog.askopenfilename(
                title="Seleccionar Póster",
                filetypes=[("Imágenes", "*.png *.jpg *.jpeg")]
            )
            if ruta:
                ruta_img_temp["path"] = ruta
                label_img_info.configure(text="Póster seleccionado", text_color="#10b981")

        btn_img = ctk.CTkButton(frame_form, text="Seleccionar Póster", fg_color="#3b82f6", command=seleccionar_imagen)
        btn_img.grid(row=2, column=2, padx=10, pady=10)

        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Roboto", 16), rowheight=30)
        estilo.configure("Treeview.Heading", font=("Roboto", 13, "bold"))

        columnas_pelis = ("id_pelicula", "titulo", "clasificacion", "duracion", "genero")
        tabla_pelis = ttk.Treeview(nueva_ventana, columns=columnas_pelis, show="headings", height=8)
        tabla_pelis.heading("id_pelicula", text="ID")
        tabla_pelis.heading("titulo", text="Título")
        tabla_pelis.heading("clasificacion", text="Clasif.")
        tabla_pelis.heading("duracion", text="Duración (min)")
        tabla_pelis.heading("genero", text="Género")
        
        tabla_pelis.column("id_pelicula", width=80)
        tabla_pelis.column("clasificacion", width=80)
        tabla_pelis.column("duracion", width=100)
        tabla_pelis.pack(pady=20, padx=20, fill="both", expand=True)
        
        frame_acciones_lista = ctk.CTkFrame(nueva_ventana, fg_color="transparent")
        frame_acciones_lista.pack(pady=10)

        def actualizar_tabla_pelis():
            for item in tabla_pelis.get_children():
                tabla_pelis.delete(item)
            for id_p, obj in peliculas_sys.peliculas.items():
                tabla_pelis.insert("", "end", values=(obj.id_pelicula, obj.titulo, obj.clasificacion, obj.duracion, obj.genero))

        def guardar_en_pelis():
            max_id = 0
            for obj in peliculas_sys.peliculas.values():
                if obj.id_pelicula.startswith("M_"):
                    try:
                        num_v = int(obj.id_pelicula.split("_")[1])
                        if num_v > max_id: max_id = num_v
                    except: pass
            id_gen = f"M_{max_id + 1}"
            
            t = entry_titulo.get()
            c = combo_clasif.get()
            d = entry_dura.get()
            g = combo_genero.get()
            s = textbox_sinopsis.get("0.0", "end").strip()
            
            if s == "Escribe la sinopsis aquí...":
                s = ""
            
            if t and c and d and g:
                # Copiar archivo si se seleccionó
                nombre_archivo_img = ""
                if ruta_img_temp["path"]:
                    ext = os.path.splitext(ruta_img_temp["path"])[1]
                    nombre_archivo_img = f"{id_gen}{ext}"
                    ruta_destino = os.path.join(carpeta_caratulas, nombre_archivo_img)
                    try:
                        shutil.copy(ruta_img_temp["path"], ruta_destino)
                    except Exception as e:
                        print("Error al copiar imagen:", e)
                
                peliculas_sys.registrar_pelicula(id_gen, t, c, d, g, s, nombre_archivo_img)
                actualizar_tabla_pelis()
                
                # Limpiar formulario
                entry_titulo.delete(0, 'end')
                entry_dura.delete(0, 'end')
                combo_genero.set("Acción")
                textbox_sinopsis.delete("0.0", "end")
                textbox_sinopsis.insert("0.0", "Escribe la sinopsis aquí...")
                ruta_img_temp["path"] = ""
                label_img_info.configure(text="Sin póster", text_color="gray")
            else:
                messagebox.showwarning("Atención", "Llena todos los campos principales.")

        btn_guardar_peli = ctk.CTkButton(frame_form, text="Guardar Película", command=guardar_en_pelis)
        btn_guardar_peli.grid(row=2, column=1, padx=10, pady=10)

        def eliminar_pelicula():
            seleccion = tabla_pelis.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una película para eliminar")
                return
            item = tabla_pelis.item(seleccion[0])
            id_p = str(item['values'][0])
            tit_p = str(item['values'][1])
            
            if messagebox.askyesno("Confirmar", f"¿Eliminar película '{tit_p}'?"):
                if id_p in peliculas_sys.peliculas:
                    del peliculas_sys.peliculas[id_p]
                    peliculas_sys.actualizar_csv_completo()
                    actualizar_tabla_pelis()
                    messagebox.showinfo("Eliminado", "Película eliminada con éxito")
        
        btn_eliminar_peli = ctk.CTkButton(frame_acciones_lista, text="Eliminar Película", 
                                     fg_color="#ef4444", hover_color="#b91c1c",
                                     command=eliminar_pelicula)
        btn_eliminar_peli.grid(row=0, column=1, padx=10)
        
        def abrir_modificar_pelicula():
            seleccion = tabla_pelis.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una película a editar")
                return
            
            item = tabla_pelis.item(seleccion[0])
            id_p_antiguo = str(item['values'][0])
            peli_obj = peliculas_sys.peliculas.get(id_p_antiguo)

            if peli_obj:
                vent_edit_peli = ctk.CTkToplevel()
                vent_edit_peli.title("Modificar Película")
                vent_edit_peli.geometry("400x600")
                vent_edit_peli.grab_set()

                ctk.CTkLabel(vent_edit_peli, text=f"Modificar {peli_obj.titulo}", font=("Roboto", 16, "bold")).pack(pady=10)
                
                ctk.CTkLabel(vent_edit_peli, text="Título:").pack()
                entry_m_tit = ctk.CTkEntry(vent_edit_peli, width=250)
                entry_m_tit.insert(0, peli_obj.titulo)
                entry_m_tit.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_peli, text="Clasificación:").pack()
                combo_m_cla = ctk.CTkComboBox(vent_edit_peli, values=["AA", "A", "B", "B15", "C"], width=250)
                combo_m_cla.set(peli_obj.clasificacion)
                combo_m_cla.pack(pady=5)

                ctk.CTkLabel(vent_edit_peli, text="Duración (min):").pack()
                entry_m_dur = ctk.CTkEntry(vent_edit_peli, width=250)
                entry_m_dur.insert(0, str(peli_obj.duracion))
                entry_m_dur.pack(pady=5)
                
                ctk.CTkLabel(vent_edit_peli, text="Género:").pack()
                combo_m_gen = ctk.CTkComboBox(vent_edit_peli, values=["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción", "Infantil", "Romance", "Documental"], width=250)
                if peli_obj.genero:
                    combo_m_gen.set(peli_obj.genero)
                combo_m_gen.pack(pady=5)

                ctk.CTkLabel(vent_edit_peli, text="Sinopsis:").pack()
                textbox_m_sinop = ctk.CTkTextbox(vent_edit_peli, height=60, width=250)
                textbox_m_sinop.insert("0.0", peli_obj.sinopsis)
                textbox_m_sinop.pack(pady=5)

                # Lógica de imagen para edición
                ruta_img_mod = {"path": ""}
                txt_lbl = "Póster actual: " + (peli_obj.dir_img if peli_obj.dir_img else "Ninguno")
                lbl_img_mod = ctk.CTkLabel(vent_edit_peli, text=txt_lbl, text_color="gray")
                lbl_img_mod.pack(pady=5)

                def sel_img_mod():
                    ruta = filedialog.askopenfilename(
                        title="Cambiar Póster",
                        filetypes=[("Imágenes", "*.png *.jpg *.jpeg")]
                    )
                    if ruta:
                        ruta_img_mod["path"] = ruta
                        lbl_img_mod.configure(text="Póster nuevo seleccionado", text_color="#10b981")

                btn_img_mod = ctk.CTkButton(vent_edit_peli, text="Cambiar Póster", fg_color="#3b82f6", command=sel_img_mod)
                btn_img_mod.pack(pady=5)

                def guardar_mod_pelicula():
                    n_tit = entry_m_tit.get()
                    n_cla = combo_m_cla.get()
                    n_dur = entry_m_dur.get()
                    n_gen = combo_m_gen.get()
                    n_sin = textbox_m_sinop.get("0.0", "end").strip()
                    
                    if not (n_tit and n_cla and n_dur and n_gen):
                        messagebox.showwarning("Atención", "Llena todos los campos clave")
                        return

                    peli_obj.titulo = n_tit
                    peli_obj.clasificacion = n_cla
                    peli_obj.duracion = n_dur
                    peli_obj.genero = n_gen
                    peli_obj.sinopsis = n_sin

                    # Procesar cambio de imagen
                    if ruta_img_mod["path"]:
                        ext = os.path.splitext(ruta_img_mod["path"])[1]
                        nuevo_nombre_img = f"{peli_obj.id_pelicula}{ext}"
                        ruta_dest = os.path.join(carpeta_caratulas, nuevo_nombre_img)
                        try:
                            shutil.copy(ruta_img_mod["path"], ruta_dest)
                            peli_obj.dir_img = nuevo_nombre_img
                        except Exception as e:
                            print("Error al copiar imagen:", e)
                    
                    peliculas_sys.actualizar_csv_completo()
                    actualizar_tabla_pelis()
                    vent_edit_peli.destroy()
                    messagebox.showinfo("Modificado", "Se ha modificado la película correctamente")

                ctk.CTkButton(vent_edit_peli, text="Guardar Cambios", fg_color="#10b981", command=guardar_mod_pelicula).pack(pady=15)
                ctk.CTkButton(vent_edit_peli, text="Cancelar", fg_color="#64748b", command=vent_edit_peli.destroy).pack(pady=5)

        btn_modificar_peli = ctk.CTkButton(frame_acciones_lista, text="Modificar Seleccionada", 
                                      fg_color="#f59e0b", hover_color="#d97706",
                                      command=abrir_modificar_pelicula)
        btn_modificar_peli.grid(row=0, column=0, padx=10)

        def abrir_previsualizacion_pelicula():
            seleccion = tabla_pelis.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una película para previsualizar")
                return
            
            item = tabla_pelis.item(seleccion[0])
            id_p = str(item['values'][0])
            peli_obj = peliculas_sys.peliculas.get(id_p)

            if peli_obj:
                vent_prev = ctk.CTkToplevel()
                vent_prev.title(f"Detalles: {peli_obj.titulo}")
                vent_prev.geometry("650x450")
                vent_prev.grab_set()

                # Frame principal para dividir imagen y texto
                frame_main = ctk.CTkFrame(vent_prev, fg_color="transparent")
                frame_main.pack(fill="both", expand=True, padx=20, pady=20)

                # Frame para la imagen (Izquierda)
                frame_img = ctk.CTkFrame(frame_main, width=220, height=330, fg_color=COLOR_CUADRO_IMAGEN)
                frame_img.pack(side="left", fill="y", padx=(0, 20))
                frame_img.pack_propagate(False)

                lbl_img = ctk.CTkLabel(frame_img, text="Sin Póster", text_color="gray", font=("Roboto", 14, "italic"))
                lbl_img.pack(expand=True)

                if peli_obj.dir_img:
                    ruta_img = os.path.join(carpeta_caratulas, peli_obj.dir_img)
                    if os.path.exists(ruta_img):
                        try:
                            img_pil = Image.open(ruta_img)
                            img_ctk = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(200, 310))
                            lbl_img.configure(image=img_ctk, text="")
                        except Exception as e:
                            print("Error cargando imagen previsualización:", e)
                
                # Frame para los datos (Derecha)
                frame_datos = ctk.CTkFrame(frame_main, fg_color="transparent")
                frame_datos.pack(side="left", fill="both", expand=True)

                ctk.CTkLabel(frame_datos, text=peli_obj.titulo, font=("Roboto", 24, "bold"), text_color="#3b82f6", anchor="w").pack(fill="x", pady=(0, 10))
                
                info_frame = ctk.CTkFrame(frame_datos, fg_color="transparent")
                info_frame.pack(fill="x", pady=5)
                ctk.CTkLabel(info_frame, text=f"🎭 Género: {peli_obj.genero}", font=("Roboto", 14, "bold")).pack(side="left", padx=(0, 15))
                ctk.CTkLabel(info_frame, text=f"⏱ Duración: {peli_obj.duracion} min", font=("Roboto", 14, "bold")).pack(side="left", padx=(0, 15))
                ctk.CTkLabel(info_frame, text=f"🔞 Clasif: {peli_obj.clasificacion}", font=("Roboto", 14, "bold")).pack(side="left")

                ctk.CTkLabel(frame_datos, text="Sinopsis:", font=("Roboto", 16, "bold"), anchor="w").pack(fill="x", pady=(15, 5))
                
                txt_sinopsis = ctk.CTkTextbox(frame_datos, height=180, wrap="word", font=("Roboto", 14))
                txt_sinopsis.insert("0.0", peli_obj.sinopsis if peli_obj.sinopsis else "Sin sinopsis disponible.")
                txt_sinopsis.configure(state="disabled") # Solo lectura
                txt_sinopsis.pack(fill="both", expand=True)

                btn_cerrar = ctk.CTkButton(vent_prev, text="Cerrar Previsualización", fg_color="gray", command=vent_prev.destroy)
                btn_cerrar.pack(pady=10)

        btn_previsualizar = ctk.CTkButton(frame_acciones_lista, text="Previsualización", 
                                      fg_color="#8b5cf6", hover_color="#7c3aed",
                                      command=abrir_previsualizacion_pelicula)
        btn_previsualizar.grid(row=0, column=2, padx=10)

        actualizar_tabla_pelis()

    elif titulo == "Crear funciones":
        frame_form = ctk.CTkFrame(nueva_ventana)
        frame_form.pack(pady=10, padx=20, fill="x")

        # Cargar opciones para los combobox
        nombres_pelis = [f"{p.id_pelicula} - {p.titulo}" for p in peliculas_sys.peliculas.values()]
        if not nombres_pelis: nombres_pelis = ["No hay películas registradas"]
        
        nombres_salas = [f"{s.idsala} - Sala {s.numero}" for s in salas_sys.salas.values()]
        if not nombres_salas: nombres_salas = ["No hay salas registradas"]

        # Generar horas de 12:00 a 23:30 cada 30 min
        horas_disp = []
        hora_ini = datetime.strptime("12:00", "%H:%M")
        for _ in range(24): # Hasta 23:30 (12 * 2 = 24 bloques)
            horas_disp.append(hora_ini.strftime("%H:%M"))
            hora_ini += timedelta(minutes=30)
        
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        ctk.CTkLabel(frame_form, text="Día:").grid(row=0, column=0, padx=5, pady=5)
        combo_dia = ctk.CTkComboBox(frame_form, values=dias_semana, width=120)
        combo_dia.grid(row=1, column=0, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Película:").grid(row=0, column=1, padx=5, pady=5)
        combo_peli = ctk.CTkComboBox(frame_form, values=nombres_pelis, width=200)
        combo_peli.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Sala:").grid(row=0, column=2, padx=5, pady=5)
        combo_sala = ctk.CTkComboBox(frame_form, values=nombres_salas, width=200)
        combo_sala.grid(row=1, column=2, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Hora Inicio:").grid(row=0, column=3, padx=5, pady=5)
        combo_hora = ctk.CTkComboBox(frame_form, values=horas_disp, width=120)
        combo_hora.grid(row=1, column=3, padx=10, pady=5)

        # Tabla de cronograma
        ctk.CTkLabel(nueva_ventana, text="Cronograma de la sala seleccionada:", font=("Roboto", 16, "bold")).pack(pady=(15, 5))
        
        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Roboto", 14), rowheight=25)
        estilo.configure("Treeview.Heading", font=("Roboto", 13, "bold"))

        cols_agenda = ("id_fun", "dia", "hora_ini", "hora_fin", "pelicula")
        tabla_agenda = ttk.Treeview(nueva_ventana, columns=cols_agenda, show="headings", height=8)
        tabla_agenda.heading("id_fun", text="ID")
        tabla_agenda.heading("dia", text="Día")
        tabla_agenda.heading("hora_ini", text="Inicio")
        tabla_agenda.heading("hora_fin", text="Fin (incluye 20 min limpieza)")
        tabla_agenda.heading("pelicula", text="Película")
        tabla_agenda.column("id_fun", width=60)
        tabla_agenda.column("dia", width=80)
        tabla_agenda.column("hora_ini", width=80)
        tabla_agenda.column("hora_fin", width=120)
        tabla_agenda.pack(pady=10, padx=20, fill="both", expand=True)

        def actualizar_cronograma(*args):
            for item in tabla_agenda.get_children():
                tabla_agenda.delete(item)
            
            seleccion_sala = combo_sala.get()
            seleccion_dia = combo_dia.get()
            if "No hay" in seleccion_sala: return
            
            id_sala_seleccionada = seleccion_sala.split(" - ")[0]
            
            # Filtrar funciones de esa sala y día en específico
            funcs_sala = [f for f in funciones_sys.funciones if f.id_sala == id_sala_seleccionada and f.dia == seleccion_dia]
            # Ordenar por hora de inicio
            funcs_sala.sort(key=lambda x: datetime.strptime(x.hora_inicio, "%H:%M"))
            
            for f in funcs_sala:
                peli = peliculas_sys.peliculas.get(f.id_pelicula)
                if not peli: continue
                
                h_ini = datetime.strptime(f.hora_inicio, "%H:%M")
                try:
                    dur = int(peli.duracion)
                except:
                    dur = 90
                # Se agregan 20 min de limpieza para establecer cuándo termina todo el ciclo
                h_fin = h_ini + timedelta(minutes=dur + 20)
                
                tabla_agenda.insert("", "end", values=(
                    f.id_funcion,
                    f.dia,
                    h_ini.strftime("%H:%M"), 
                    h_fin.strftime("%H:%M"), 
                    peli.titulo
                ))
        
        # Enlazar actualización del cronograma cuando el usuario cambie de sala o día
        combo_sala.configure(command=actualizar_cronograma)
        combo_dia.configure(command=actualizar_cronograma)

        def generar_funciones():
            d_sel = combo_dia.get()
            p_sel = combo_peli.get()
            s_sel = combo_sala.get()
            h_sel = combo_hora.get()
            
            if "No hay" in p_sel or "No hay" in s_sel:
                messagebox.showwarning("Error", "Faltan registrar películas o salas.")
                return

            id_pelicula = p_sel.split(" - ")[0]
            id_sala = s_sel.split(" - ")[0]
            
            peli_obj = peliculas_sys.peliculas.get(id_pelicula)
            if not peli_obj: return

            # Validar Unicidad de Sala: Una película solo puede proyectarse en una única sala.
            for func in funciones_sys.funciones:
                if func.id_pelicula == id_pelicula and func.id_sala != id_sala:
                    messagebox.showerror("Regla de Negocio", f"La película '{peli_obj.titulo}' ya está asignada a otra sala (Solo se permite 1 sala por película).")
                    return

            try:
                dur_peli = int(peli_obj.duracion)
            except:
                dur_peli = 90

            hora_actual = datetime.strptime(h_sel, "%H:%M")
            limite = datetime.strptime("22:00", "%H:%M")
            
            # Checar si ya hay funciones ese día en esa sala
            funcs_dia_sala = [f for f in funciones_sys.funciones if f.dia == d_sel and f.id_sala == id_sala]
            if funcs_dia_sala:
                resp = messagebox.askyesno("Advertencia", f"Ya hay funciones programadas para la Sala {id_sala} el día {d_sel}. ¿Deseas borrar las funciones actuales de ese día y reprogramar todo desde cero de forma automática?")
                if resp:
                    # Filtro de nuevo excluyendo las funciones del choche
                    funciones_sys.funciones = [f for f in funciones_sys.funciones if not (f.dia == d_sel and f.id_sala == id_sala)]
                else:
                    return

            generadas = 0
            while hora_actual <= limite:
                max_id = 0
                for f in funciones_sys.funciones:
                    if f.id_funcion.startswith("F_"):
                        try:
                            n = int(f.id_funcion.split("_")[1])
                            if n > max_id: max_id = n
                        except: pass
                
                nuevo_id = f"F_{max_id + 1}"
                funciones_sys.registrar_funcion(nuevo_id, id_pelicula, id_sala, d_sel, hora_actual.strftime("%H:%M"))
                generadas += 1
                
                hora_actual += timedelta(minutes=dur_peli + 20)

            # Persistencia forzosa si hubo borrados o creaciones
            funciones_sys.actualizar_csv_completo()
            actualizar_cronograma()
            messagebox.showinfo("Éxito", f"Se generaron {generadas} funciones automáticamente para el {d_sel}.")

        ctk.CTkButton(frame_form, text="Generar Funciones", font=("Roboto", 14, "bold"), fg_color="#10b981", command=generar_funciones).grid(row=1, column=4, padx=20, pady=5)
        
        actualizar_cronograma()

        def eliminar_funcion():
            seleccion = tabla_agenda.selection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona una función de la tabla para eliminar.")
                return
            item = tabla_agenda.item(seleccion[0])
            id_f = str(item['values'][0]) # La col 0 es id_fun
            
            if messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar la función {id_f}?"):
                funciones_sys.funciones = [f for f in funciones_sys.funciones if f.id_funcion != id_f]
                funciones_sys.actualizar_csv_completo()
                actualizar_cronograma()
                messagebox.showinfo("Éxito", "Función eliminada correctamente.")

        ctk.CTkButton(nueva_ventana, text="Eliminar Función", fg_color="#ef4444", hover_color="#b91c1c", command=eliminar_funcion).pack(pady=5)

    elif titulo == "Cartelera Digital":
        nueva_ventana.geometry("1000x800")
        nueva_ventana.configure(fg_color="black") # Ambientación de cine
        
        frame_top = ctk.CTkFrame(nueva_ventana, fg_color="transparent")
        frame_top.pack(fill="x", pady=20, padx=20)
        
        ctk.CTkLabel(frame_top, text="Día a proyectar:", font=("Roboto", 16, "bold"), text_color="white").pack(side="left", padx=10)
        combo_dia_cart = ctk.CTkComboBox(frame_top, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], width=150)
        combo_dia_cart.set("Lunes")
        combo_dia_cart.pack(side="left", padx=10)
        
        # Frame central de contenido
        frame_cartelera = ctk.CTkFrame(nueva_ventana, fg_color="#111827", corner_radius=15, border_width=2, border_color="#3b82f6")
        frame_cartelera.pack(fill="both", expand=True, padx=40, pady=20)

        # Dividimos en Izquierda (Póster) y Derecha (Datos y Horarios)
        frame_izq = ctk.CTkFrame(frame_cartelera, fg_color="transparent")
        frame_izq.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        frame_der = ctk.CTkFrame(frame_cartelera, fg_color="transparent")
        frame_der.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        lbl_poster = ctk.CTkLabel(frame_izq, text="Cargando Póster...", font=("Roboto", 24, "italic"), text_color="gray")
        lbl_poster.pack(expand=True)
        
        lbl_tit_cine = ctk.CTkLabel(frame_der, text="SELECCIONA UN DÍA", font=("Roboto", 48, "bold"), text_color="#facc15", anchor="w")
        lbl_tit_cine.pack(fill="x", pady=(30, 5))

        lbl_sala_cine = ctk.CTkLabel(frame_der, text="SALA --", font=("Roboto", 32, "bold"), text_color="white", anchor="w")
        lbl_sala_cine.pack(fill="x", pady=(5, 10))

        lbl_gen_cine = ctk.CTkLabel(frame_der, text="GÉNERO / DURACIÓN / CLASIF", font=("Roboto", 20), text_color="#9ca3af", anchor="w")
        lbl_gen_cine.pack(fill="x", pady=10)

        lbl_horarios = ctk.CTkLabel(frame_der, text="HORARIOS DISPONIBLES:", font=("Roboto", 24, "bold"), text_color="gray", anchor="w")
        lbl_horarios.pack(fill="x", pady=(30, 5))
        
        lbl_lista_horarios = ctk.CTkLabel(frame_der, text="--:--", font=("Roboto", 36, "bold"), text_color="#10b981", anchor="w")
        lbl_lista_horarios.pack(fill="x", pady=10)

        estado = {"indice": 0, "pelis": [], "timer_id": None}

        def rotar_cartelera():
            if not estado["pelis"]:
                lbl_tit_cine.configure(text="No hay funciones hoy")
                lbl_poster.configure(image="", text="SIN FUNCIONES")
                lbl_sala_cine.configure(text="SALA --")
                lbl_gen_cine.configure(text="---")
                lbl_lista_horarios.configure(text="--:--")
                return

            peli_id = estado["pelis"][estado["indice"]]["id"]
            horarios = estado["pelis"][estado["indice"]]["horas"]
            sala_id = estado["pelis"][estado["indice"]]["sala"]
            
            peli_obj = peliculas_sys.peliculas.get(peli_id)
            sala_obj = salas_sys.salas.get(sala_id)
            
            if not sala_obj:
                # Búsqueda manual de respaldo (por si hay problemas de lectura del CSV)
                for s in salas_sys.salas.values():
                    if str(s.idsala).strip() == str(sala_id).strip() or str(s.numero).strip() == str(sala_id).strip():
                        sala_obj = s
                        break

            if peli_obj:
                lbl_tit_cine.configure(text=peli_obj.titulo.upper())
                lbl_gen_cine.configure(text=f"{peli_obj.genero.upper()}  |  {peli_obj.duracion} MIN  |  CLASIF. {peli_obj.clasificacion}")
                
                if sala_obj:
                    lbl_sala_cine.configure(text=f"SALA {sala_obj.numero}")
                else:
                    num_s = str(sala_id).upper().replace("S_", "").strip()
                    lbl_sala_cine.configure(text=f"SALA {num_s}")

                # Format Horarios
                lbl_lista_horarios.configure(text="  -  ".join(horarios))
                
                # Cargar imagen
                if peli_obj.dir_img:
                    ruta = os.path.join(os.path.dirname(__file__), "caratulas", peli_obj.dir_img)
                    if os.path.exists(ruta):
                        try:
                            img = Image.open(ruta)
                            img_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 600))
                            lbl_poster.configure(image=img_ctk, text="")
                        except:
                            lbl_poster.configure(image="", text="ERROR DE IMAGEN")
                    else:
                        lbl_poster.configure(image="", text="PÓSTER NO ENCONTRADO")
                else:
                    lbl_poster.configure(image="", text="PRÓXIMAMENTE\nMUY PRONTO")

            # Rotar después de 6 segundos
            estado["indice"] = (estado["indice"] + 1) % len(estado["pelis"])
            estado["timer_id"] = nueva_ventana.after(6000, rotar_cartelera)

        def actualizar_dia(*args):
            dia = combo_dia_cart.get()
            if estado["timer_id"]:
                nueva_ventana.after_cancel(estado["timer_id"])
            
            # Agrupar por id_pelicula
            dict_pelis = {}
            for f in funciones_sys.funciones:
                if f.dia == dia:
                    if f.id_pelicula not in dict_pelis:
                        dict_pelis[f.id_pelicula] = {"horas": [], "sala": f.id_sala}
                    dict_pelis[f.id_pelicula]["horas"].append(f.hora_inicio)
            
            # Limpiar formatos y ordenar
            lista_final = []
            for pid, dat in dict_pelis.items():
                hrs = sorted(list(set(dat["horas"])), key=lambda x: datetime.strptime(x, "%H:%M"))
                lista_final.append({"id": pid, "horas": hrs, "sala": dat["sala"]})
            
            estado["pelis"] = lista_final
            estado["indice"] = 0
            rotar_cartelera()

        combo_dia_cart.configure(command=actualizar_dia)
        
        # Override de destrucción para cancelar el loop silencioso
        def al_cerrar_cartelera():
            if estado["timer_id"]:
                try:
                    nueva_ventana.after_cancel(estado["timer_id"])
                except:
                    pass
            nueva_ventana.destroy()
            
        nueva_ventana.protocol("WM_DELETE_WINDOW", al_cerrar_cartelera)
        actualizar_dia()
        btn_salir = ctk.CTkButton(nueva_ventana, text="Cerrar Cartelera", fg_color="gray", command=al_cerrar_cartelera)
        btn_salir.pack(pady=10)
        return

    btn_salir = ctk.CTkButton(nueva_ventana, text="Cerrar", fg_color="gray", command=nueva_ventana.destroy)
    btn_salir.pack(pady=10)




def mostrar_pantalla_admin(ventana):
    limpiar_pantalla(ventana)
    ventana.title("Ventana Gestión Administrativa")
    
    label = ctk.CTkLabel(ventana, text="¡Bienvenido al Panel de Administrador!", font=("Roboto", 28, "bold"), text_color="white")
    label.pack(pady=20)

    frame_menu=ctk.CTkFrame(ventana,fg_color="transparent")
    frame_menu.pack(pady=10)

    boton_usuarios = ctk.CTkButton(frame_menu, text="Gestión de usuarios", width=240, height=50, command=lambda: abrir_ventana_accion("Gestión de usuarios"))
    boton_usuarios.grid(row=0, column=0, padx=15, pady=15)

    boton_salas = ctk.CTkButton(frame_menu, text="Gestión de salas", width=240, height=50, command=lambda: abrir_ventana_accion("Gestión de salas"))
    boton_salas.grid(row=0, column=1, padx=15, pady=15)

    boton_crearpelis = ctk.CTkButton(frame_menu, text="Gestión de peliculas", width=240, height=50, command=lambda: abrir_ventana_accion("Gestión de peliculas"))
    boton_crearpelis.grid(row=1, column=0, padx=15, pady=15)

    boton_productos = ctk.CTkButton(frame_menu, text="Gestión de productos", width=240, height=50, command=lambda: abrir_ventana_accion("Gestión de productos"))
    boton_productos.grid(row=1, column=1, padx=15, pady=15)

    btn_funciones = ctk.CTkButton(frame_menu, text="Gestión de carteleras", width=240, height=50, command=lambda: abrir_ventana_accion("Crear funciones"))
    btn_funciones.grid(row=2, column=0, padx=15, pady=15)

    btn_cartelera = ctk.CTkButton(frame_menu, text="Ver Cartelera Digital", width=240, height=50, fg_color="#8b5cf6", hover_color="#7c3aed", command=lambda: abrir_ventana_accion("Cartelera Digital"))
    btn_cartelera.grid(row=2, column=1, padx=15, pady=15)
    
    _crear_boton_cerrar_sesion(ventana)

def mostrar_pantalla_taquillero(ventana, nombre_taquillero="Taquillero"):
    limpiar_pantalla(ventana)
    ventana.title(f"Taquilla — {nombre_taquillero}")
    ventana.after(0, lambda: ventana.state('zoomed'))

   
    frame_header = ctk.CTkFrame(ventana, fg_color="#1e293b", corner_radius=0, height=70)
    frame_header.pack(fill="x", side="top")
    frame_header.pack_propagate(False)

    ctk.CTkLabel(
        frame_header,
        text=f"🎬  LoboCine — Taquilla",
        font=("Roboto", 22, "bold"),
        text_color="#facc15"
    ).pack(side="left", padx=25, pady=15)

    ctk.CTkLabel(
        frame_header,
        text=f"👤  {nombre_taquillero}",
        font=("Roboto", 18, "bold"),
        text_color="#10b981"
    ).pack(side="right", padx=25, pady=15)

    
    frame_body = ctk.CTkFrame(ventana, fg_color="#0f172a")
    frame_body.pack(fill="both", expand=True, padx=0, pady=0)

    
    estado_venta = {
        "funcion_obj": None,
        "peli_obj": None,
        "sala_obj": None,
        "asientos_sel": [],
    }

    # ---------- PASO 1: Selección de Función ----------
    def mostrar_paso1():
        limpiar_pantalla(frame_body)
        estado_venta["funcion_obj"] = None
        estado_venta["peli_obj"] = None
        estado_venta["sala_obj"] = None
        estado_venta["asientos_sel"] = []

        ctk.CTkLabel(
            frame_body,
            text="Paso 1 — Selecciona función",
            font=("Roboto", 22, "bold"),
            text_color="#3b82f6"
        ).pack(pady=(30, 10))

        frame_filtros = ctk.CTkFrame(frame_body, fg_color="#1e293b", corner_radius=12)
        frame_filtros.pack(padx=40, pady=10, fill="x")

        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        ctk.CTkLabel(frame_filtros, text="Día:", font=("Roboto", 16, "bold")).grid(row=0, column=0, padx=20, pady=15, sticky="w")
        combo_dia = ctk.CTkComboBox(frame_filtros, values=dias_semana, width=160)
        combo_dia.set("Lunes")
        combo_dia.grid(row=0, column=1, padx=10, pady=15)

        # Tabla de funciones del día
        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Roboto", 14), rowheight=30, background="#1e293b", foreground="white", fieldbackground="#1e293b")
        estilo.configure("Treeview.Heading", font=("Roboto", 13, "bold"))
        estilo.map("Treeview", background=[("selected", "#2563eb")])

        cols = ("id_fun", "pelicula", "sala", "hora", "duracion", "clasif")
        tabla_fun = ttk.Treeview(frame_body, columns=cols, show="headings", height=10)
        tabla_fun.heading("id_fun", text="ID")
        tabla_fun.heading("pelicula", text="Película")
        tabla_fun.heading("sala", text="Sala")
        tabla_fun.heading("hora", text="Hora")
        tabla_fun.heading("duracion", text="Duración")
        tabla_fun.heading("clasif", text="Clasif.")
        tabla_fun.column("id_fun", width=70)
        tabla_fun.column("pelicula", width=280)
        tabla_fun.column("sala", width=80)
        tabla_fun.column("hora", width=80)
        tabla_fun.column("duracion", width=100)
        tabla_fun.column("clasif", width=80)
        tabla_fun.pack(padx=40, pady=10, fill="both", expand=True)

        def cargar_funciones(*args):
            for item in tabla_fun.get_children():
                tabla_fun.delete(item)
            dia = combo_dia.get()
            for f in funciones_sys.funciones:
                if f.dia == dia:
                    peli = peliculas_sys.peliculas.get(f.id_pelicula)
                    sala = None
                    for s in salas_sys.salas.values():
                        if s.idsala == f.id_sala:
                            sala = s
                            break
                    if peli and sala:
                        tabla_fun.insert("", "end", iid=f.id_funcion, values=(
                            f.id_funcion,
                            peli.titulo,
                            f"Sala {sala.numero}",
                            f.hora_inicio,
                            f"{peli.duracion} min",
                            peli.clasificacion
                        ))

        combo_dia.configure(command=cargar_funciones)
        cargar_funciones()

        frame_btn = ctk.CTkFrame(frame_body, fg_color="transparent")
        frame_btn.pack(pady=15)

        def ir_paso2():
            sel = tabla_fun.selection()
            if not sel:
                messagebox.showwarning("Atención", "Selecciona una función de la lista.")
                return
            id_fun = sel[0]
            funcion = next((f for f in funciones_sys.funciones if f.id_funcion == id_fun), None)
            if not funcion: return
            peli = peliculas_sys.peliculas.get(funcion.id_pelicula)
            sala = None
            for s in salas_sys.salas.values():
                if s.idsala == funcion.id_sala:
                    sala = s
                    break
            if not peli or not sala:
                messagebox.showerror("Error", "No se encontraron los datos de la función.")
                return
            estado_venta["funcion_obj"] = funcion
            estado_venta["peli_obj"] = peli
            estado_venta["sala_obj"] = sala
            mostrar_paso2()

        ctk.CTkButton(
            frame_btn, text="Continuar →  Seleccionar Asientos",
            width=280, height=45, font=("Roboto", 15, "bold"),
            fg_color="#2563eb", hover_color="#1d4ed8",
            command=ir_paso2
        ).pack()

    # ---------- PASO 2: Mapa de Asientos ----------
    def mostrar_paso2():
        limpiar_pantalla(frame_body)
        estado_venta["asientos_sel"] = []

        funcion = estado_venta["funcion_obj"]
        peli    = estado_venta["peli_obj"]
        sala    = estado_venta["sala_obj"]

        filas = len(sala.asientos)
        columnas = len(sala.asientos[0]) if filas > 0 else 0

        ctk.CTkLabel(
            frame_body,
            text=f"Paso 2 — Selecciona asientos  |  {peli.titulo}  |  {funcion.hora_inicio}  |  Sala {sala.numero}",
            font=("Roboto", 18, "bold"),
            text_color="#3b82f6"
        ).pack(pady=(20, 5))

        # Leyenda de colores
        frame_ley = ctk.CTkFrame(frame_body, fg_color="transparent")
        frame_ley.pack(pady=5)
        for color, texto in [("#10b981", "● Disponible"), ("#ef4444", "● Ocupado"), ("#f59e0b", "● Seleccionado")]:
            ctk.CTkLabel(frame_ley, text=texto, font=("Roboto", 13, "bold"), text_color=color).pack(side="left", padx=15)

        # Pantalla de cine (decorativa)
        lbl_pantalla = ctk.CTkLabel(frame_body, text="▬▬▬  P A N T A L L A  ▬▬▬",
                                    font=("Roboto", 13), text_color="#9ca3af")
        lbl_pantalla.pack(pady=(10, 2))

        # Scroll canvas para el mapa de asientos
        frame_canvas_outer = ctk.CTkFrame(frame_body, fg_color="#111827", corner_radius=12)
        frame_canvas_outer.pack(padx=30, pady=5, fill="both", expand=True)

        canvas = tk.Canvas(frame_canvas_outer, bg="#111827", highlightthickness=0)
        scrollbar_y = ttk.Scrollbar(frame_canvas_outer, orient="vertical", command=canvas.yview)
        scrollbar_x = ttk.Scrollbar(frame_canvas_outer, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)

        frame_asientos = tk.Frame(canvas, bg="#111827")
        canvas.create_window((0, 0), window=frame_asientos, anchor="nw")

        TAMANO_BTN = 38
        LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ocupados = asientos_sys.obtener_ocupados(funcion.id_funcion)
        botones_mapa = {}

        def toggle_asiento(codigo):
            if codigo in ocupados:
                return  
            if codigo in estado_venta["asientos_sel"]:
                estado_venta["asientos_sel"].remove(codigo)
                botones_mapa[codigo].configure(bg="#10b981")
            else:
                estado_venta["asientos_sel"].append(codigo)
                botones_mapa[codigo].configure(bg="#f59e0b")
            actualizar_contador()

        # Encabezados de columna
        tk.Label(frame_asientos, text="", bg="#111827", width=3).grid(row=0, column=0, padx=2, pady=2)
        for c in range(columnas):
            tk.Label(
                frame_asientos, text=str(c + 1),
                bg="#111827", fg="#9ca3af",
                font=("Roboto", 10, "bold"), width=4
            ).grid(row=0, column=c + 1, padx=2, pady=2)

        for r in range(filas):
            letra = LETRAS[r] if r < len(LETRAS) else str(r + 1)
            tk.Label(
                frame_asientos, text=letra,
                bg="#111827", fg="#9ca3af",
                font=("Roboto", 10, "bold"), width=3
            ).grid(row=r + 1, column=0, padx=4, pady=2)

            for c in range(columnas):
                codigo = f"{letra}{c + 1}"
                if codigo in ocupados:
                    color = "#ef4444"
                    active_color = "#ef4444"
                    cursor = "arrow"
                else:
                    color = "#10b981"
                    active_color = "#f59e0b"
                    cursor = "hand2"

                btn = tk.Button(
                    frame_asientos,
                    text=" ",
                    bg=color,
                    activebackground=active_color,
                    cursor=cursor,
                    relief="flat",
                    width=3, height=1,
                    command=lambda cod=codigo: toggle_asiento(cod)
                )
                btn.grid(row=r + 1, column=c + 1, padx=2, pady=2)
                botones_mapa[codigo] = btn

        frame_asientos.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Contador y precio
        frame_info = ctk.CTkFrame(frame_body, fg_color="#1e293b", corner_radius=10)
        frame_info.pack(padx=30, pady=8, fill="x")

        lbl_counter = ctk.CTkLabel(
            frame_info,
            text="Asientos seleccionados: 0  |  Total: $0.00",
            font=("Roboto", 16, "bold"),
            text_color="#facc15"
        )
        lbl_counter.pack(side="left", padx=20, pady=10)

        def actualizar_contador():
            n = len(estado_venta["asientos_sel"])
            total = n * SistemaVentas.PRECIO_BOLETO
            lbl_counter.configure(text=f"Asientos seleccionados: {n}  |  Total: ${total:.2f} MXN")

        frame_btns = ctk.CTkFrame(frame_body, fg_color="transparent")
        frame_btns.pack(pady=10)

        ctk.CTkButton(
            frame_btns, text="← Regresar",
            width=160, height=42,
            fg_color="#64748b", hover_color="#475569",
            font=("Roboto", 14, "bold"),
            command=mostrar_paso1
        ).pack(side="left", padx=15)

        def ir_paso3():
            if not estado_venta["asientos_sel"]:
                messagebox.showwarning("Atención", "Selecciona al menos un asiento.")
                return
            mostrar_ticket()

        ctk.CTkButton(
            frame_btns, text="Continuar →  Ver Ticket",
            width=240, height=42,
            fg_color="#2563eb", hover_color="#1d4ed8",
            font=("Roboto", 14, "bold"),
            command=ir_paso3
        ).pack(side="left", padx=15)

    # ---------- PASO 3: Ticket y Confirmación ----------
    def mostrar_ticket():
        funcion = estado_venta["funcion_obj"]
        peli    = estado_venta["peli_obj"]
        sala    = estado_venta["sala_obj"]
        asientos = estado_venta["asientos_sel"]
        total = len(asientos) * SistemaVentas.PRECIO_BOLETO
        fecha_hora_ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

        vent_ticket = ctk.CTkToplevel(ventana)
        vent_ticket.title("Ticket de Venta")
        vent_ticket.geometry("540x700")
        vent_ticket.configure(fg_color="#0f172a")
        vent_ticket.resizable(False, False)
        vent_ticket.attributes("-topmost", True)          # Siempre encima
        vent_ticket.after(50, vent_ticket.lift)           # Lift diferido para que CTk termine de cargar
        

        
        frame_btns_t = ctk.CTkFrame(vent_ticket, fg_color="#1e293b", corner_radius=0, height=80)
        frame_btns_t.pack(side="bottom", fill="x", padx=0, pady=0)
        frame_btns_t.pack_propagate(False)

        def confirmar_venta():
            n_asientos = len(asientos)
            titulo_peli = peli.titulo
            total_cobrado = total
            id_fun = funcion.id_funcion

            ventas_sys.registrar_venta(nombre_taquillero, id_fun, list(asientos))
            asientos_sys.reservar(id_fun, list(asientos))
            vent_ticket.destroy()
            mostrar_paso1()
            messagebox.showinfo(
                "Venta Exitosa",
                f"Se vendieron {n_asientos} boleto(s) para '{titulo_peli}'.\n"
                f"Total cobrado: ${total_cobrado:.2f} MXN"
            )

        ctk.CTkButton(
            frame_btns_t,
            text="Confirmar Venta",
            width=220, height=50,
            fg_color="#16a34a", hover_color="#15803d",
            font=("Roboto", 15, "bold"),
            command=confirmar_venta
        ).pack(side="left", padx=30, pady=15)

        ctk.CTkButton(
            frame_btns_t,
            text="Cancelar",
            width=150, height=50,
            fg_color="#dc2626", hover_color="#b91c1c",
            font=("Roboto", 14, "bold"),
            command=vent_ticket.destroy
        ).pack(side="right", padx=30, pady=15)

        # ── CONTENIDO SCROLLEABLE EN EL CENTRO ──
        frame_scroll_outer = ctk.CTkScrollableFrame(vent_ticket, fg_color="#0f172a")
        frame_scroll_outer.pack(fill="both", expand=True)

        # Encabezado
        frame_enc = ctk.CTkFrame(frame_scroll_outer, fg_color="#1e3a8a", corner_radius=10)
        frame_enc.pack(fill="x", padx=20, pady=(15, 6))
        ctk.CTkLabel(frame_enc, text="LOBOCINE",
                     font=("Roboto", 28, "bold"), text_color="#facc15").pack(pady=(14, 2))
        ctk.CTkLabel(frame_enc, text="BOLETO DE ENTRADA",
                     font=("Roboto", 12), text_color="#93c5fd").pack(pady=(0, 12))

        def fila_dato(parent, etiqueta, valor, color_val="white"):
            f = ctk.CTkFrame(parent, fg_color="transparent")
            f.pack(fill="x", padx=16, pady=3)
            ctk.CTkLabel(f, text=etiqueta, font=("Roboto", 12), text_color="#9ca3af",
                         anchor="w", width=150).pack(side="left")
            ctk.CTkLabel(f, text=valor, font=("Roboto", 13, "bold"), text_color=color_val,
                         anchor="w", wraplength=260).pack(side="left", fill="x", expand=True)

        # Datos de la función
        frame_datos = ctk.CTkFrame(frame_scroll_outer, fg_color="#1e293b", corner_radius=10)
        frame_datos.pack(padx=20, pady=6, fill="x")
        ctk.CTkLabel(frame_datos, text="  FUNCION", font=("Roboto", 11, "bold"),
                     text_color="#3b82f6", anchor="w").pack(fill="x", padx=16, pady=(8, 4))
        fila_dato(frame_datos, "Pelicula:", peli.titulo, "#facc15")
        fila_dato(frame_datos, "Clasificacion:", peli.clasificacion)
        fila_dato(frame_datos, "Sala:", f"Sala {sala.numero}  ({sala.tipo})")
        fila_dato(frame_datos, "Dia:", funcion.dia)
        fila_dato(frame_datos, "Hora:", funcion.hora_inicio)
        fila_dato(frame_datos, "ID Funcion:", funcion.id_funcion, "#6b7280")
        ctk.CTkLabel(frame_datos, text="").pack(pady=4)

        # Asientos
        frame_asientos_t = ctk.CTkFrame(frame_scroll_outer, fg_color="#1e293b", corner_radius=10)
        frame_asientos_t.pack(padx=20, pady=6, fill="x")
        ctk.CTkLabel(frame_asientos_t, text="  BOLETOS", font=("Roboto", 11, "bold"),
                     text_color="#3b82f6", anchor="w").pack(fill="x", padx=16, pady=(8, 4))
        fila_dato(frame_asientos_t, "Asientos:", ", ".join(sorted(asientos)), "#10b981")
        fila_dato(frame_asientos_t, "Cantidad:", str(len(asientos)))
        fila_dato(frame_asientos_t, "Precio c/u:", f"${SistemaVentas.PRECIO_BOLETO:.2f} MXN")
        ctk.CTkLabel(frame_asientos_t, text="").pack(pady=4)

        # Total
        frame_total = ctk.CTkFrame(frame_scroll_outer, fg_color="#064e3b", corner_radius=10)
        frame_total.pack(padx=20, pady=6, fill="x")
        ctk.CTkLabel(frame_total, text=f"TOTAL: ${total:.2f} MXN",
                     font=("Roboto", 26, "bold"), text_color="#34d399").pack(pady=18)

        # Pie
        frame_pie = ctk.CTkFrame(frame_scroll_outer, fg_color="transparent")
        frame_pie.pack(padx=20, pady=(6, 15), fill="x")
        ctk.CTkLabel(frame_pie, text=f"Atendido por: {nombre_taquillero}",
                     font=("Roboto", 11), text_color="#6b7280").pack()
        ctk.CTkLabel(frame_pie, text=f"Fecha/Hora: {fecha_hora_ahora}",
                     font=("Roboto", 11), text_color="#6b7280").pack()

    # Botón cerrar sesión (debajo del body)
    frame_footer = ctk.CTkFrame(ventana, fg_color="#0f172a", height=50)
    frame_footer.pack(fill="x", side="bottom")
    ctk.CTkButton(
        frame_footer, text="Cerrar Sesión",
        fg_color="#dc2626", hover_color="#991b1b",
        font=("Roboto", 13, "bold"), width=150, height=36,
        command=lambda: mostrar_pantalla_login(ventana)
    ).pack(side="right", padx=20, pady=7)

    # Iniciar en paso 1
    mostrar_paso1()

def mostrar_pantalla_dulcero(ventana, nombre_dulcero="Dulcero"):
    limpiar_pantalla(ventana)
    ventana.title(f"Dulceria - {nombre_dulcero}")
    ventana.after(0, lambda: ventana.state('zoomed'))

    # ─── HEADER ───────────────────────────────────────────────────
    frame_header = ctk.CTkFrame(ventana, fg_color="#7c2d12", corner_radius=0, height=70)
    frame_header.pack(fill="x", side="top")
    frame_header.pack_propagate(False)
    ctk.CTkLabel(
        frame_header, text="Dulceria LoboCine",
        font=("Roboto", 22, "bold"), text_color="#fde68a"
    ).pack(side="left", padx=25, pady=15)
    ctk.CTkLabel(
        frame_header, text=f"Dulcero: {nombre_dulcero}",
        font=("Roboto", 18, "bold"), text_color="#10b981"
    ).pack(side="right", padx=25, pady=15)

    # ─── FOOTER ───────────────────────────────────────────────────
    frame_footer = ctk.CTkFrame(ventana, fg_color="#0f172a", height=50)
    frame_footer.pack(fill="x", side="bottom")
    frame_footer.pack_propagate(False)
    ctk.CTkButton(
        frame_footer, text="Cerrar Sesion",
        fg_color="#dc2626", hover_color="#991b1b",
        font=("Roboto", 13, "bold"), width=150, height=36,
        command=lambda: mostrar_pantalla_login(ventana)
    ).pack(side="right", padx=20, pady=7)

    # ─── CUERPO: izquierda=Catalogo, derecha=Carrito ───────────────
    frame_body = ctk.CTkFrame(ventana, fg_color="#0f172a")
    frame_body.pack(fill="both", expand=True)

    # ── PANEL DERECHO: CARRITO ──────────────────────────────────────
    frame_carrito = ctk.CTkFrame(frame_body, fg_color="#1e293b", corner_radius=0, width=320)
    frame_carrito.pack(side="right", fill="y", padx=0, pady=0)
    frame_carrito.pack_propagate(False)

    ctk.CTkLabel(frame_carrito, text="Carrito",
                 font=("Roboto", 18, "bold"), text_color="#fde68a").pack(pady=(15, 5))

    frame_lista_carrito = ctk.CTkScrollableFrame(frame_carrito, fg_color="#0f172a", corner_radius=8)
    frame_lista_carrito.pack(fill="both", expand=True, padx=10, pady=5)

    lbl_total = ctk.CTkLabel(frame_carrito, text="Total: $0.00 MXN",
                             font=("Roboto", 17, "bold"), text_color="#34d399")
    lbl_total.pack(pady=8)

    btn_cobrar = ctk.CTkButton(
        frame_carrito, text="Cobrar",
        fg_color="#16a34a", hover_color="#15803d",
        font=("Roboto", 16, "bold"), width=260, height=50
    )
    btn_cobrar.pack(pady=(5, 5))

    btn_limpiar = ctk.CTkButton(
        frame_carrito, text="Limpiar carrito",
        fg_color="#64748b", hover_color="#475569",
        font=("Roboto", 13), width=260, height=36
    )
    btn_limpiar.pack(pady=(0, 12))

    # Estado del carrito: {id_producto: {"nombre", "precio", "cantidad"}}
    carrito = {}
    widgets_carrito = {}  # id_producto -> frame del item en el panel

    def recalcular_total():
        total = sum(v["precio"] * v["cantidad"] for v in carrito.values())
        lbl_total.configure(text=f"Total: ${total:.2f} MXN")

    def actualizar_panel_carrito():
        for w in frame_lista_carrito.winfo_children():
            w.destroy()
        widgets_carrito.clear()
        for id_p, it in carrito.items():
            fr = ctk.CTkFrame(frame_lista_carrito, fg_color="#1e293b", corner_radius=8)
            fr.pack(fill="x", pady=3, padx=2)
            ctk.CTkLabel(fr, text=it["nombre"], font=("Roboto", 12, "bold"),
                         text_color="white", anchor="w", wraplength=160).grid(row=0, column=0, columnspan=3, padx=8, pady=(6,2), sticky="w")
            ctk.CTkLabel(fr, text=f"${it['precio']:.2f} c/u",
                         font=("Roboto", 10), text_color="#9ca3af").grid(row=1, column=0, padx=8, sticky="w")

            def quitar(pid=id_p):
                if carrito[pid]["cantidad"] > 1:
                    carrito[pid]["cantidad"] -= 1
                else:
                    del carrito[pid]
                actualizar_panel_carrito()
                recalcular_total()

            def agregar_uno(pid=id_p):
                prod = productos_sys.productos.get(pid)
                if prod and carrito[pid]["cantidad"] < prod.stock:
                    carrito[pid]["cantidad"] += 1
                    actualizar_panel_carrito()
                    recalcular_total()

            ctk.CTkButton(fr, text="-", width=28, height=28, fg_color="#ef4444",
                          font=("Roboto", 13, "bold"), command=quitar).grid(row=1, column=1, padx=3, pady=4)
            ctk.CTkLabel(fr, text=str(it["cantidad"]), font=("Roboto", 13, "bold"),
                         text_color="#facc15", width=24).grid(row=1, column=2)
            ctk.CTkButton(fr, text="+", width=28, height=28, fg_color="#10b981",
                          font=("Roboto", 13, "bold"), command=agregar_uno).grid(row=1, column=3, padx=3)
            subtotal = it["precio"] * it["cantidad"]
            ctk.CTkLabel(fr, text=f"=${subtotal:.2f}",
                         font=("Roboto", 11, "bold"), text_color="#34d399").grid(row=1, column=4, padx=6)
            widgets_carrito[id_p] = fr

    def limpiar_carrito():
        carrito.clear()
        actualizar_panel_carrito()
        recalcular_total()

    btn_limpiar.configure(command=limpiar_carrito)

    def agregar_al_carrito(id_p, nombre, precio):
        prod = productos_sys.productos.get(id_p)
        if not prod or prod.stock <= 0:
            messagebox.showwarning("Sin stock", f"'{nombre}' no tiene stock disponible.")
            return
        if id_p in carrito:
            if carrito[id_p]["cantidad"] >= prod.stock:
                messagebox.showwarning("Sin stock", f"No hay mas stock de '{nombre}'.")
                return
            carrito[id_p]["cantidad"] += 1
        else:
            carrito[id_p] = {"nombre": nombre, "precio": precio, "cantidad": 1}
        actualizar_panel_carrito()
        recalcular_total()

    # ── PANEL IZQUIERDO: CATALOGO POR CATEGORIAS ────────────────────
    frame_catalogo = ctk.CTkFrame(frame_body, fg_color="#0f172a")
    frame_catalogo.pack(side="left", fill="both", expand=True)

    CATEGORIAS = ["Todos", "Combos", "Palomitas", "Bebidas", "Dulces", "Snacks"]
    CAT_COLORES = {
        "Todos": "#3b82f6", "Combos": "#f59e0b", "Palomitas": "#ef4444",
        "Bebidas": "#06b6d4", "Dulces": "#a855f7", "Snacks": "#10b981"
    }
    cat_sel = {"valor": "Todos"}
    btns_cat = {}

    frame_tabs = ctk.CTkFrame(frame_catalogo, fg_color="#1e293b", corner_radius=0, height=52)
    frame_tabs.pack(fill="x")
    frame_tabs.pack_propagate(False)

    frame_grid_outer = ctk.CTkScrollableFrame(frame_catalogo, fg_color="#0f172a")
    frame_grid_outer.pack(fill="both", expand=True, padx=10, pady=10)

    COLS = 4  # tarjetas por fila

    def mostrar_catalogo(categoria="Todos"):
        cat_sel["valor"] = categoria
        for c, btn in btns_cat.items():
            if c == categoria:
                btn.configure(fg_color=CAT_COLORES.get(c, "#3b82f6"))
            else:
                btn.configure(fg_color="#334155")
        for w in frame_grid_outer.winfo_children():
            w.destroy()

        productos_sys._cargar_productos()  # Refrescar stock
        productos_filtrados = [
            p for p in productos_sys.productos.values()
            if categoria == "Todos" or p.categoria == categoria
        ]

        for idx, prod in enumerate(productos_filtrados):
            fila = idx // COLS
            col  = idx % COLS
            agotado = prod.stock <= 0

            card = ctk.CTkFrame(
                frame_grid_outer,
                fg_color="#1e293b" if not agotado else "#1c1c1c",
                corner_radius=12,
                border_width=1,
                border_color=CAT_COLORES.get(prod.categoria, "#334155") if not agotado else "#374151"
            )
            card.grid(row=fila, column=col, padx=8, pady=8, sticky="nsew")
            frame_grid_outer.grid_columnconfigure(col, weight=1)

            # Icono por categoria
            iconos = {"Combos": "🎬", "Palomitas": "🍿", "Bebidas": "🥤", "Dulces": "🍬", "Snacks": "🌮"}
            icono = iconos.get(prod.categoria, "🛒")

            ctk.CTkLabel(card, text=icono, font=("Roboto", 28)).pack(pady=(14, 2))
            ctk.CTkLabel(card, text=prod.nombre,
                         font=("Roboto", 12, "bold"), text_color="white" if not agotado else "#6b7280",
                         wraplength=160).pack(padx=8)
            ctk.CTkLabel(card, text=f"${prod.precio:.2f} MXN",
                         font=("Roboto", 14, "bold"),
                         text_color=CAT_COLORES.get(prod.categoria, "#facc15") if not agotado else "#4b5563"
                         ).pack(pady=4)
            ctk.CTkLabel(card, text=f"Stock: {prod.stock}",
                         font=("Roboto", 10),
                         text_color="#10b981" if prod.stock > 10 else ("#f59e0b" if prod.stock > 0 else "#ef4444")
                         ).pack(pady=(0, 6))

            if not agotado:
                ctk.CTkButton(
                    card, text="+ Agregar",
                    fg_color=CAT_COLORES.get(prod.categoria, "#3b82f6"),
                    hover_color="#1d4ed8",
                    font=("Roboto", 12, "bold"), height=34,
                    command=lambda pid=prod.id_producto, pnom=prod.nombre, ppre=prod.precio:
                        agregar_al_carrito(pid, pnom, ppre)
                ).pack(fill="x", padx=10, pady=(0, 12))
            else:
                ctk.CTkLabel(card, text="AGOTADO",
                             font=("Roboto", 12, "bold"), text_color="#ef4444").pack(pady=(0, 12))

    # Crear tabs de categoria
    for i, cat in enumerate(CATEGORIAS):
        b = ctk.CTkButton(
            frame_tabs, text=cat,
            width=100, height=40,
            fg_color="#334155" if i > 0 else CAT_COLORES["Todos"],
            hover_color=CAT_COLORES.get(cat, "#3b82f6"),
            font=("Roboto", 13, "bold"), corner_radius=0,
            command=lambda c=cat: mostrar_catalogo(c)
        )
        b.pack(side="left", padx=1)
        btns_cat[cat] = b

    # ── LOGICA DE COBRO ─────────────────────────────────────────────
    def cobrar():
        if not carrito:
            messagebox.showwarning("Carrito vacio", "Agrega productos al carrito antes de cobrar.")
            return

        items_lista = [
            {
                "id_producto": pid,
                "nombre": it["nombre"],
                "cantidad": it["cantidad"],
                "subtotal": it["precio"] * it["cantidad"]
            }
            for pid, it in carrito.items()
        ]
        total_venta = sum(it["subtotal"] for it in items_lista)
        fecha_hora_ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

        # ── Ventana de Ticket ──────────────────────────
        vent_t = ctk.CTkToplevel(ventana)
        vent_t.title("Ticket Dulceria")
        vent_t.geometry("480x660")
        vent_t.configure(fg_color="#0f172a")
        vent_t.resizable(False, False)
        vent_t.attributes("-topmost", True)
        vent_t.after(50, vent_t.lift)

        # Botones fijos abajo (PRIMERO)
        frame_bf = ctk.CTkFrame(vent_t, fg_color="#7c2d12", corner_radius=0, height=78)
        frame_bf.pack(side="bottom", fill="x")
        frame_bf.pack_propagate(False)

        def confirmar_cobro():
            ventas_dulceria_sys.registrar_venta(nombre_dulcero, items_lista, productos_sys)
            vent_t.destroy()
            limpiar_carrito()
            mostrar_catalogo(cat_sel["valor"])
            messagebox.showinfo("Venta registrada",
                f"Venta guardada correctamente.\nTotal cobrado: ${total_venta:.2f} MXN")

        ctk.CTkButton(frame_bf, text="Confirmar Cobro",
                      fg_color="#16a34a", hover_color="#15803d",
                      font=("Roboto", 15, "bold"), width=200, height=50,
                      command=confirmar_cobro).pack(side="left", padx=25, pady=14)
        ctk.CTkButton(frame_bf, text="Cancelar",
                      fg_color="#64748b", hover_color="#475569",
                      font=("Roboto", 13), width=130, height=50,
                      command=vent_t.destroy).pack(side="right", padx=25, pady=14)

        # Contenido scrolleable
        sc = ctk.CTkScrollableFrame(vent_t, fg_color="#0f172a")
        sc.pack(fill="both", expand=True)

        # Encabezado ticket
        enc = ctk.CTkFrame(sc, fg_color="#7c2d12", corner_radius=10)
        enc.pack(fill="x", padx=20, pady=(15, 6))
        ctk.CTkLabel(enc, text="LOBOCINE", font=("Roboto", 24, "bold"),
                     text_color="#fde68a").pack(pady=(12, 2))
        ctk.CTkLabel(enc, text="DULCERIA - TICKET DE VENTA",
                     font=("Roboto", 11), text_color="#fca5a5").pack(pady=(0, 10))

        # Items
        fr_items = ctk.CTkFrame(sc, fg_color="#1e293b", corner_radius=10)
        fr_items.pack(fill="x", padx=20, pady=6)
        ctk.CTkLabel(fr_items, text="  PRODUCTOS", font=("Roboto", 11, "bold"),
                     text_color="#f59e0b", anchor="w").pack(fill="x", padx=16, pady=(8, 4))

        for it in items_lista:
            fr_row = ctk.CTkFrame(fr_items, fg_color="transparent")
            fr_row.pack(fill="x", padx=16, pady=2)
            ctk.CTkLabel(fr_row, text=f"{it['nombre']} x{it['cantidad']}",
                         font=("Roboto", 12), text_color="white", anchor="w").pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(fr_row, text=f"${it['subtotal']:.2f}",
                         font=("Roboto", 12, "bold"), text_color="#34d399").pack(side="right")
        ctk.CTkLabel(fr_items, text="").pack(pady=4)

        # Total
        fr_total = ctk.CTkFrame(sc, fg_color="#064e3b", corner_radius=10)
        fr_total.pack(fill="x", padx=20, pady=6)
        ctk.CTkLabel(fr_total, text=f"TOTAL: ${total_venta:.2f} MXN",
                     font=("Roboto", 24, "bold"), text_color="#34d399").pack(pady=16)

        # Pie
        fr_pie = ctk.CTkFrame(sc, fg_color="transparent")
        fr_pie.pack(fill="x", padx=20, pady=(4, 14))
        ctk.CTkLabel(fr_pie, text=f"Atendido por: {nombre_dulcero}",
                     font=("Roboto", 11), text_color="#6b7280").pack()
        ctk.CTkLabel(fr_pie, text=f"Fecha/Hora: {fecha_hora_ahora}",
                     font=("Roboto", 11), text_color="#6b7280").pack()

    btn_cobrar.configure(command=cobrar)

    # Inicializar catalogo
    mostrar_catalogo("Todos")

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
            mostrar_pantalla_taquillero(ventana, usuario_texto)
        elif rol_usuario == "dulcero":
            mostrar_pantalla_dulcero(ventana, usuario_texto)
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