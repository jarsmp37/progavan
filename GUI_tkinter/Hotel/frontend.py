import tkinter as tk
from PIL import Image, ImageTk
from backconguardado import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime


def ventanainicio():
    global venta1
    Usuario.cargar_usuarios()
    Habitacion.cargar_habitaciones()
    Huesped.cargar_huespedes()
    Reserva.cargar_reservas()
    venta1 = tk.Tk()
    venta1.title("Inicio de Sesión")
    venta1.geometry("400x400")
    venta1.config(bg="lightblue")

    venta1.iconbitmap("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Hotel//hotel.ico")

    global entrada1,entrada2

    canvas = tk.Canvas(venta1, width=400, height=400)
    canvas.pack()
    imagen = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Hotel//imaghotel.jpg")
    fondo = ImageTk.PhotoImage(imagen)
    canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
    canvas.image = fondo 


    fuente_titulo = ("Arial", 16, "bold")  
    titulo = tk.Label(venta1, text="Hotel de Proga Avanzada", bg="lightblue", font=fuente_titulo)
    canvas.create_window(200, 30, window=titulo)

    fuente_personalizada = ("Arial", 12, "bold")
    etiqueta1 = tk.Label(venta1, text="Usuario:", bg="lightblue", font=fuente_personalizada)
    entrada1 = tk.Entry(venta1)
    etiqueta2 = tk.Label(venta1, text="Contraseña:", bg="lightblue", font=fuente_personalizada)
    entrada2 = tk.Entry(venta1, show="*")  

    
    canvas.create_window(100, 100, window=etiqueta1)
    canvas.create_window(250, 100, window=entrada1)
    canvas.create_window(100, 150, window=etiqueta2)
    canvas.create_window(250, 150, window=entrada2)

    
    boton_login = tk.Button(venta1, text="Iniciar Sesión", command=inicio)
    canvas.create_window(200, 200, window=boton_login)
    venta1.protocol("WM_DELETE_WINDOW", alcerrar)

    venta1.mainloop()

def alcerrar():
    Usuario.guardar_usuarios()
    Habitacion.guardar_habitaciones()
    Huesped.guardar_huespedes()
    Reserva.guardar_reservas()
    venta1.destroy()


def inicio():
    usuario=entrada1.get()
    password=entrada2.get()
    usuario_iniciar=Usuario.iniciar_sesion(usuario,password)
    venta1.destroy() 

    if usuario_iniciar.rol=="Administrador":
        ventanadmin()
    elif usuario_iniciar.rol=="Recepcionista":
        ventanarecep()
    
    

def ventanadmin():
    venta2 = tk.Tk()
    venta2.title("Ventana Admin")
    venta2.geometry("600x500")
    venta2.resizable(False, False)  

    
    imagen_fondo = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Hotel//admin_bg.jpg")
    imagen_fondo = imagen_fondo.resize((600, 500))
    fondo = ImageTk.PhotoImage(imagen_fondo)
    
    canvas = tk.Canvas(venta2, width=600, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
    canvas.image = fondo
    
   
    titulo = tk.Label(venta2, text="Panel de Administrador", font=("Arial", 16, "bold"), bg="lightgray")
    canvas.create_window(300, 50, window=titulo)
    
    
    botones = [
        ("Crear Usuario", crear_usuario),
        ("Modificar Usuarios", modificar_usuarios),
        ("Crear Habitación", crear_habitacion),
        ("Mostrar Habitaciones", mostrar_habitaciones),
        ("Cerrar Sesión", lambda: cerrar_sesion(venta2))
    ]
    
    for i, (texto, comando) in enumerate(botones):
        boton = tk.Button(venta2, text=texto, command=comando, width=20, height=2, font=("Arial", 10, "bold"))
        canvas.create_window(300, 120 + i * 60, window=boton)
    
    venta2.mainloop()

def crear_usuario():
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Crear Usuario")
    ventana_crear_usuario.geometry("300x250")

    tk.Label(ventana_crear_usuario, text="Nombre de Usuario:").pack()
    entrada_usuario = tk.Entry(ventana_crear_usuario)
    entrada_usuario.pack()

    tk.Label(ventana_crear_usuario, text="Contraseña:").pack()
    entrada_password = tk.Entry(ventana_crear_usuario, show="*")
    entrada_password.pack()

    tk.Label(ventana_crear_usuario, text="Rol:").pack()
    rol_var = tk.StringVar(value="Administrador")
    tk.Radiobutton(ventana_crear_usuario, text="Administrador", variable=rol_var, value="Administrador").pack()
    tk.Radiobutton(ventana_crear_usuario, text="Recepcionista", variable=rol_var, value="Recepcionista").pack()

    def guardar_usuario():
        nombre = entrada_usuario.get()
        password = entrada_password.get()
        rol = rol_var.get()
        nuevo_usuario = Usuario(nombre,rol, password)
        messagebox.showinfo("Éxito", "Usuario creado correctamente")
        Usuario.guardar_usuarios()
        ventana_crear_usuario.destroy()

    boton_guardar = tk.Button(ventana_crear_usuario, text="Guardar", command=guardar_usuario)
    boton_guardar.pack(pady=10)

def modificar_usuarios():
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Modificar Usuarios")
    ventana_modificar.geometry("600x300")

    frame = tk.Frame(ventana_modificar)
    frame.pack(fill=tk.BOTH, expand=True)

    
    tree = ttk.Treeview(frame, columns=("Usuario", "Rol", "Contraseña"), show="headings")
    tree.heading("Usuario", text="Usuario")
    tree.heading("Rol", text="Rol")
    tree.heading("Contraseña", text="Contraseña")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    
    for usuario in Usuario.lista_usuario:
        tree.insert("", tk.END, values=(usuario.nombre, usuario.rol, usuario._Usuario__pass))

    def modificar_usuario():
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            abrir_edicion_usuario(item["values"][0]) 
        Usuario.guardar_usuarios()

    def borrar_usuario():
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            usuario_nombre = item["values"][0]

            for usuario in Usuario.lista_usuario:
                if usuario.nombre == usuario_nombre:
                    Usuario.lista_usuario.remove(usuario)
                    break

            for row in tree.get_children():
                tree.delete(row)

            for usuario in Usuario.lista_usuario:
                tree.insert("", tk.END, values=(usuario.nombre, usuario.rol, usuario._Usuario__pass))
        Usuario.guardar_usuarios()

    boton_modificar = tk.Button(ventana_modificar, text="Modificar", command=modificar_usuario)
    boton_modificar.pack(side=tk.LEFT, padx=10)

    boton_borrar = tk.Button(ventana_modificar, text="Borrar", command=borrar_usuario)
    boton_borrar.pack(side=tk.LEFT, padx=10)

def abrir_edicion_usuario(nombre_usuario):
    ventana_edicion = tk.Toplevel()
    ventana_edicion.title("Editar Usuario")
    ventana_edicion.geometry("300x250")

    usuario = next((u for u in Usuario.lista_usuario if u.nombre == nombre_usuario), None)
    if not usuario:
        messagebox.showerror("Error", "Usuario no encontrado")
        return

    
    tk.Label(ventana_edicion, text="Usuario:").pack()
    entrada_usuario = tk.Entry(ventana_edicion)
    entrada_usuario.insert(0, usuario.nombre)
    entrada_usuario.pack()

    
    tk.Label(ventana_edicion, text="Contraseña:").pack()
    entrada_password = tk.Entry(ventana_edicion, show="*")
    entrada_password.insert(0, usuario._Usuario__pass)  
    entrada_password.pack()

    
    tk.Label(ventana_edicion, text="Rol:").pack()
    rol_var = tk.StringVar(value=usuario.rol)
    tk.Radiobutton(ventana_edicion, text="Administrador", variable=rol_var, value="Administrador").pack()
    tk.Radiobutton(ventana_edicion, text="Recepcionista", variable=rol_var, value="Recepcionista").pack()

    def guardar_cambios():
        usuario.nombre = entrada_usuario.get()
        usuario._Usuario__pass = entrada_password.get()  
        usuario.rol = rol_var.get()
        messagebox.showinfo("Éxito", "Usuario modificado correctamente")
        Usuario.guardar_usuarios()  
        ventana_edicion.destroy()

    tk.Button(ventana_edicion, text="Guardar", command=guardar_cambios).pack()

def mostrar_habitaciones():
    ventana_habitaciones = tk.Toplevel()
    ventana_habitaciones.title("Lista de Habitaciones")
    ventana_habitaciones.geometry("800x400")

    frame = tk.Frame(ventana_habitaciones)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("Número", "Tipo", "Camas", "Costo por noche", "Disponibilidad"), show="headings")
    tree.heading("Número", text="Número")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Camas", text="Camas")
    tree.heading("Costo por noche", text="Costo por noche")
    tree.heading("Disponibilidad", text="Disponibilidad")

    tree.column("Número", width=100)
    tree.column("Tipo", width=150)
    tree.column("Camas", width=100)
    tree.column("Costo por noche", width=150)
    tree.column("Disponibilidad", width=150)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for habitacion in Habitacion.lista_Habitaciones:
        disponibilidad = "Disponible" if habitacion.disponibilidad else "Ocupada"
        tree.insert("", tk.END, values=(habitacion.numero, habitacion.tipo, habitacion.camas, habitacion.costo, disponibilidad))

    def modificar_habitacion():
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            numero_habitacion = item["values"][0]
            abrir_edicion_habitacion(numero_habitacion)
        Habitacion.guardar_habitaciones()

    def borrar_habitacion():
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            numero_habitacion = str(item["values"][0])  

            
            for habitacion in Habitacion.lista_Habitaciones:
                if str(habitacion.numero) == numero_habitacion:
                    Habitacion.lista_Habitaciones.remove(habitacion)
                    break

            
            for row in tree.get_children():
                tree.delete(row)

            for habitacion in Habitacion.lista_Habitaciones:
                disponibilidad = "Disponible" if habitacion.disponibilidad else "Ocupada"
                tree.insert("", tk.END, values=(habitacion.numero, habitacion.tipo, habitacion.camas, habitacion.costo, disponibilidad))

            
            Habitacion.guardar_habitaciones()
            messagebox.showinfo("Éxito", "Habitación eliminada correctamente")

    boton_modificar = tk.Button(ventana_habitaciones, text="Modificar", command=modificar_habitacion)
    boton_modificar.pack(side=tk.LEFT, padx=10)

    boton_borrar = tk.Button(ventana_habitaciones, text="Borrar", command=borrar_habitacion)
    boton_borrar.pack(side=tk.LEFT, padx=10)


def abrir_edicion_habitacion(numero_habitacion):
    numero_habitacion = str(numero_habitacion)
    
    
    habitacion = next((h for h in Habitacion.lista_Habitaciones if str(h.numero) == numero_habitacion), None)
    
    if not habitacion:
        messagebox.showerror("Error", "Habitación no encontrada")
        return

    
    ventana_edicion = tk.Toplevel()
    ventana_edicion.title("Editar Habitación")
    ventana_edicion.geometry("300x200")

    
    tk.Label(ventana_edicion, text="Número:").pack()
    entrada_numero = tk.Entry(ventana_edicion)
    entrada_numero.insert(0, habitacion.numero)
    entrada_numero.pack()

    tk.Label(ventana_edicion, text="Tipo:").pack()
    entrada_tipo = tk.Entry(ventana_edicion)
    entrada_tipo.insert(0, habitacion.tipo)
    entrada_tipo.pack()

    tk.Label(ventana_edicion, text="Camas:").pack()
    entrada_camas = tk.Entry(ventana_edicion)
    entrada_camas.insert(0, habitacion.camas)
    entrada_camas.pack()

    tk.Label(ventana_edicion, text="Costo por noche:").pack()
    entrada_costo = tk.Entry(ventana_edicion)
    entrada_costo.insert(0, habitacion.costo)
    entrada_costo.pack()

    def guardar_cambios():
        
        habitacion.numero = entrada_numero.get()
        habitacion.tipo = entrada_tipo.get()
        habitacion.camas = entrada_camas.get()
        habitacion.costo = entrada_costo.get()
        
        Habitacion.guardar_habitaciones()
        messagebox.showinfo("Éxito", "Habitación modificada correctamente")
        ventana_edicion.destroy()

    
    tk.Button(ventana_edicion, text="Guardar", command=guardar_cambios).pack()

def registrar_huesped():
    ventana_registrar = tk.Toplevel()
    ventana_registrar.title("Registrar Huésped")
    ventana_registrar.geometry("300x200")

    tk.Label(ventana_registrar, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana_registrar)
    entrada_nombre.pack()

    tk.Label(ventana_registrar, text="Teléfono:").pack()
    entrada_telefono = tk.Entry(ventana_registrar)
    entrada_telefono.pack()

    def guardar_huesped():
        nombre = entrada_nombre.get()
        telefono = entrada_telefono.get()
        nuevo_huesped = Huesped(nombre, telefono)
        admin.registrar(nuevo_huesped)
        ventana_registrar.destroy()

    boton_guardar = tk.Button(ventana_registrar, text="Guardar", command=guardar_huesped)
    boton_guardar.pack()

def modificar_huesped():
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Modificar Huésped")
    ventana_modificar.geometry("600x400")

    
    frame_huespedes = tk.Frame(ventana_modificar)
    frame_huespedes.pack(fill=tk.BOTH, expand=True)

    
    canvas = tk.Canvas(frame_huespedes)
    scrollbar = tk.Scrollbar(frame_huespedes, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    
    for huesped in Huesped.lista_huespedes:
        frame_huesped = tk.Frame(scrollable_frame)
        frame_huesped.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(frame_huesped, text=f"Nombre: {huesped.nombre}, Teléfono: {huesped.telefono}").pack(side=tk.LEFT)

        boton_modificar = tk.Button(frame_huesped, text="Modificar", command=lambda h=huesped: modificar_huesped_seleccionado(h))
        boton_modificar.pack(side=tk.LEFT, padx=5)

        boton_eliminar = tk.Button(frame_huesped, text="Eliminar", command=lambda h=huesped: eliminar_huesped_seleccionado(h))
        boton_eliminar.pack(side=tk.LEFT, padx=5)

def modificar_huesped_seleccionado(huesped):
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Huésped")
    ventana_editar.geometry("300x200")

    tk.Label(ventana_editar, text="Nuevo nombre:").pack()
    entrada_nuevo_nombre = tk.Entry(ventana_editar)
    entrada_nuevo_nombre.insert(0, huesped.nombre)
    entrada_nuevo_nombre.pack()

    tk.Label(ventana_editar, text="Nuevo teléfono:").pack()
    entrada_nuevo_telefono = tk.Entry(ventana_editar)
    entrada_nuevo_telefono.insert(0, huesped.telefono)
    entrada_nuevo_telefono.pack()

    def guardar_cambios():
        nuevo_nombre = entrada_nuevo_nombre.get()
        nuevo_telefono = entrada_nuevo_telefono.get()
        admin.modificarcliente(huesped, nuevo_nombre, nuevo_telefono)
        ventana_editar.destroy()
        tk.messagebox.showinfo("Éxito", "Huésped modificado correctamente")

    boton_guardar = tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios)
    boton_guardar.pack()

def eliminar_huesped_seleccionado(huesped):
  
    confirmacion = tk.messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar a {huesped.nombre}?")
    if confirmacion:
        admin.eliminarcliente(huesped)
        tk.messagebox.showinfo("Éxito", f"Huésped {huesped.nombre} eliminado correctamente")
        modificar_huesped()


def crear_habitacion():
    ventana_crear = tk.Toplevel()
    ventana_crear.title("Crear Habitación")
    ventana_crear.geometry("300x200")

    tk.Label(ventana_crear, text="Número:").pack()
    entrada_numero = tk.Entry(ventana_crear)
    entrada_numero.pack()

    tk.Label(ventana_crear, text="Tipo:").pack()
    entrada_tipo = tk.Entry(ventana_crear)
    entrada_tipo.pack()

    tk.Label(ventana_crear, text="Camas:").pack()
    entrada_camas = tk.Entry(ventana_crear)
    entrada_camas.pack()

    tk.Label(ventana_crear, text="Costo por noche:").pack()
    entrada_costo = tk.Entry(ventana_crear)
    entrada_costo.pack()

    def guardar_habitacion():
        numero = entrada_numero.get()
        tipo = entrada_tipo.get()
        camas = entrada_camas.get()
        costo = entrada_costo.get()
        nueva_habitacion = Habitacion(numero, tipo, camas, costo)
        print("Nueva habitación creada:", nueva_habitacion.numero) 
        Habitacion.guardar_habitaciones()
        ventana_crear.destroy()

    boton_guardar = tk.Button(ventana_crear, text="Guardar", command=guardar_habitacion)
    boton_guardar.pack()



def ventanarecep():
    venta3 = tk.Tk()
    venta3.title("Ventana Recepción")
    venta3.geometry("600x500")
    venta3.resizable(False, False)

    
    imagen_fondo = Image.open("C://Users//Jaime//Documents//GitHub//progavan//GUI_tkinter//Hotel//recepcion_bg.jpg")
    imagen_fondo = imagen_fondo.resize((600, 500))
    fondo = ImageTk.PhotoImage(imagen_fondo)

    
    canvas = tk.Canvas(venta3, width=600, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
    canvas.image = fondo

    titulo = tk.Label(venta3, text="Panel de Recepción", font=("Arial", 16, "bold"), bg="lightgray")
    canvas.create_window(300, 50, window=titulo)

    botones = [
        ("Ver Disponibilidad", ver_disponibilidad),
        ("Reservar Habitación", reservar_habitacion),
        ("Cancelar Reserva", cancelar_reserva),
        ("Cerrar Sesión", lambda: cerrar_sesion(venta3))
    ]

    for i, (texto, comando) in enumerate(botones):
        boton = tk.Button(venta3, text=texto, command=comando, width=20, height=2, font=("Arial", 10, "bold"))
        canvas.create_window(300, 120 + i * 60, window=boton)

    venta3.mainloop()


def cerrar_sesion(ventana_actual):
    ventana_actual.destroy()  
    ventanainicio() 


def ver_disponibilidad():
    ventana_disponibilidad = tk.Toplevel()
    ventana_disponibilidad.title("Disponibilidad de Habitaciones")
    ventana_disponibilidad.geometry("600x400")

    frame = tk.Frame(ventana_disponibilidad)
    frame.pack(fill=tk.BOTH, expand=True)

    columnas = ("Disponibilidad", "Número", "Tipo", "Camas", "Costo por noche")
    tree = ttk.Treeview(frame, columns=columnas, show="headings")
    
    tree.heading("Disponibilidad", text="Disponibilidad")
    tree.heading("Número", text="Número")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Camas", text="Camas")
    tree.heading("Costo por noche", text="Costo por noche")

    tree.column("Disponibilidad", width=100)
    tree.column("Número", width=100)
    tree.column("Tipo", width=150)
    tree.column("Camas", width=100)
    tree.column("Costo por noche", width=150)

    for habitacion in Habitacion.lista_Habitaciones:
        disponibilidad = "Disponible" if habitacion.disponibilidad else "Ocupada"
        tree.insert("", tk.END, values=(disponibilidad, habitacion.numero, habitacion.tipo, habitacion.camas, habitacion.costo))

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



def reservar_habitacion():
    ventana_reservar = tk.Toplevel()
    ventana_reservar.title("Reservar Habitación")
    ventana_reservar.geometry("650x550")

    frame_personas = tk.Frame(ventana_reservar)
    frame_personas.pack(pady=10)

    tk.Label(frame_personas, text="¿Para cuántas personas?").pack(side=tk.LEFT, padx=5)
    spin_personas = tk.Spinbox(frame_personas, from_=1, to=10, width=5)
    spin_personas.pack(side=tk.LEFT, padx=5)

    frame_calendarios = tk.Frame(ventana_reservar)
    frame_calendarios.pack(pady=10)

    tk.Label(frame_calendarios, text="Fecha de entrada:").pack(side=tk.LEFT, padx=5)
    calendario_entrada = DateEntry(frame_calendarios, width=12, background="darkblue", foreground="white", borderwidth=2)
    calendario_entrada.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_calendarios, text="Fecha de salida:").pack(side=tk.LEFT, padx=5)
    calendario_salida = DateEntry(frame_calendarios, width=12, background="darkblue", foreground="white", borderwidth=2)
    calendario_salida.pack(side=tk.LEFT, padx=5)

    frame_habitaciones = tk.Frame(ventana_reservar)
    frame_habitaciones.pack(pady=10)

    columnas = ("Número", "Tipo", "Camas", "Costo por noche", "Disponibilidad")
    tree = ttk.Treeview(frame_habitaciones, columns=columnas, show="headings")
    
    tree.heading("Número", text="Número")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Camas", text="Camas")
    tree.heading("Costo por noche", text="Costo por noche")
    tree.heading("Disponibilidad", text="Disponibilidad")

    tree.column("Número", width=100)
    tree.column("Tipo", width=150)
    tree.column("Camas", width=100)
    tree.column("Costo por noche", width=150)
    tree.column("Disponibilidad", width=100)

    scrollbar = ttk.Scrollbar(frame_habitaciones, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def actualizar_habitaciones():
        for row in tree.get_children():
            tree.delete(row)

        num_personas = int(spin_personas.get())
        fecha_entrada = calendario_entrada.get_date()
        fecha_salida = calendario_salida.get_date()

        if num_personas <= 2:
            camas_necesarias = 1
        elif num_personas <= 4:
            camas_necesarias = 2
        elif num_personas <= 6:
            camas_necesarias = 3
        else:
            camas_necesarias = (num_personas // 2) + (1 if num_personas % 2 != 0 else 0)

        for habitacion in Habitacion.lista_Habitaciones:
            if habitacion.disponibilidad and int(habitacion.camas) >= camas_necesarias:
                disponibilidad = "Disponible"
                costo_total = (fecha_salida - fecha_entrada).days * habitacion.costo
                tree.insert("", tk.END, values=(habitacion.numero, habitacion.tipo, habitacion.camas, f"${costo_total}", disponibilidad))

    boton_actualizar = tk.Button(ventana_reservar, text="Actualizar Habitaciones", command=actualizar_habitaciones)
    boton_actualizar.pack(pady=10)

    frame_huesped = tk.Frame(ventana_reservar)
    frame_huesped.pack(pady=10)

    tk.Label(frame_huesped, text="Nombre del huésped:").pack(side=tk.LEFT, padx=5)
    entrada_nombre = tk.Entry(frame_huesped)
    entrada_nombre.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_huesped, text="Teléfono:").pack(side=tk.LEFT, padx=5)
    entrada_telefono = tk.Entry(frame_huesped)
    entrada_telefono.pack(side=tk.LEFT, padx=5)

    from datetime import datetime

    def confirmar_reserva():
        selected_item = tree.selection()
        if not selected_item:
            tk.messagebox.showerror("Error", "Seleccione una habitación")
            return

        item = tree.item(selected_item)
        numero_habitacion = item["values"][0]
        nombre_huesped = entrada_nombre.get()
        telefono_huesped = entrada_telefono.get()

        fecha_entrada = calendario_entrada.get_date()
        fecha_salida = calendario_salida.get_date()

        if not nombre_huesped or not telefono_huesped:
            tk.messagebox.showerror("Error", "Ingrese el nombre y teléfono del huésped")
            return

        # Buscar o crear el huésped
        huesped = next((h for h in Huesped.lista_huespedes if h.nombre == nombre_huesped), None)
        if not huesped:
            huesped = Huesped(nombre_huesped, telefono_huesped)
            Huesped.guardar_huespedes()

        # Buscar la habitación
        habitacion = next((h for h in Habitacion.lista_Habitaciones if h.numero == numero_habitacion), None)

        if habitacion and huesped:
            # Crear una nueva reserva con un ID único
            nueva_reserva = Reserva(
                id=len(Reserva.lista_reservas) + 1,  # ID único
                habitacion=habitacion,
                fecha_entrada=fecha_entrada,
                fecha_salida=fecha_salida,
                huesped=huesped
            )
            # Marcar la habitación como no disponible
            habitacion.disponibilidad = False
            # Guardar los cambios
            Reserva.guardar_reservas()
            Habitacion.guardar_habitaciones()
            ventana_reservar.destroy()
        else:
            tk.messagebox.showerror("Error", "Habitación no disponible")

    boton_confirmar = tk.Button(ventana_reservar, text="Confirmar Reserva", command=confirmar_reserva)
    boton_confirmar.pack(pady=10)

def cancelar_reserva():
    ventana_cancelar = tk.Toplevel()
    ventana_cancelar.title("Cancelar Reserva")
    ventana_cancelar.geometry("800x400")

    # Frame para la lista de reservas activas
    frame_reservas = tk.Frame(ventana_cancelar)
    frame_reservas.pack(fill=tk.BOTH, expand=True)

    # Crear la tabla (Treeview)
    columnas = ("ID", "Habitación", "Huésped", "Fecha Entrada", "Fecha Salida", "Costo Total")
    tree = ttk.Treeview(frame_reservas, columns=columnas, show="headings")
    
    # Configurar las columnas
    tree.heading("ID", text="ID")
    tree.heading("Habitación", text="Habitación")
    tree.heading("Huésped", text="Huésped")
    tree.heading("Fecha Entrada", text="Fecha Entrada")
    tree.heading("Fecha Salida", text="Fecha Salida")
    tree.heading("Costo Total", text="Costo Total")

    # Ajustar el ancho de las columnas
    tree.column("ID", width=50)
    tree.column("Habitación", width=100)
    tree.column("Huésped", width=150)
    tree.column("Fecha Entrada", width=100)
    tree.column("Fecha Salida", width=100)
    tree.column("Costo Total", width=100)

    # Añadir las reservas activas a la tabla
    for reserva in Reserva.lista_reservas:
        costo_total = (reserva.fecha_salida - reserva.fecha_entrada).days * reserva.habitacion.costo
        tree.insert("", tk.END, values=(
            reserva.id,
            reserva.habitacion.numero,
            reserva.huesped.nombre,
            reserva.fecha_entrada.strftime("%Y-%m-%d"),
            reserva.fecha_salida.strftime("%Y-%m-%d"),
            f"${costo_total}"
        ))

    # Añadir una barra de desplazamiento
    scrollbar = ttk.Scrollbar(frame_reservas, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    
    def cancelar_seleccionada():
        selected_item = tree.selection()
        if not selected_item:
            tk.messagebox.showerror("Error", "Seleccione una reserva para cancelar")
            return

        item = tree.item(selected_item)
        id_reserva = item["values"][0]

        reserva = next((r for r in Reserva.lista_reservas if r.id == id_reserva), None)
        if reserva:
            
            reserva.habitacion.disponibilidad = True

            Reserva.lista_reservas.remove(reserva)

            Reserva.guardar_reservas()
            Habitacion.guardar_habitaciones()

            for row in tree.get_children():
                tree.delete(row)

            for reserva in Reserva.lista_reservas:
                costo_total = (reserva.fecha_salida - reserva.fecha_entrada).days * reserva.habitacion.costo
                tree.insert("", tk.END, values=(
                    reserva.id,
                    reserva.habitacion.numero,
                    reserva.huesped.nombre,
                    reserva.fecha_entrada.strftime("%Y-%m-%d"),
                    reserva.fecha_salida.strftime("%Y-%m-%d"),
                    f"${costo_total}"
                ))

            tk.messagebox.showinfo("Éxito", "Reserva cancelada correctamente")
        else:
            tk.messagebox.showerror("Error", "Reserva no encontrada")

    
    boton_cancelar = tk.Button(ventana_cancelar, text="Cancelar Reserva Seleccionada", command=cancelar_seleccionada)
    boton_cancelar.pack(pady=10)

ventanainicio()

#Instalar la libreria pip install pyinstaller
#crear autoejecutable
#poner en su directorio actual
#correr pyinstaller --onefile --windowed frontend.py