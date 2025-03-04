import tkinter as tk
from PIL import Image, ImageTk
from backconguardado import *
from tkinter import messagebox
from tkinter import ttk

def ventanainicio():
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

    
    etiqueta1 = tk.Label(venta1, text="Usuario:", bg="lightblue")
    entrada1 = tk.Entry(venta1)
    etiqueta2 = tk.Label(venta1, text="Contraseña:", bg="lightblue")
    entrada2 = tk.Entry(venta1, show="*")  

    
    canvas.create_window(100, 50, window=etiqueta1)
    canvas.create_window(250, 50, window=entrada1)
    canvas.create_window(100, 100, window=etiqueta2)
    canvas.create_window(250, 100, window=entrada2)

    
    boton_login = tk.Button(venta1, text="Iniciar Sesión", command=inicio)
    canvas.create_window(200, 150, window=boton_login)

    venta1.mainloop()

def inicio():
    usuario=entrada1.get()
    password=entrada2.get()
    usuario_iniciar=Usuario.iniciar_sesion(usuario,password)

    if usuario_iniciar.rol=="Administrador":
        ventanadmin()
    elif usuario_iniciar.rol=="Recepcionista":
        ventanarecep()
    
    

def ventanadmin():
    venta2 = tk.Toplevel()
    venta2.title("Ventana admin")
    venta2.geometry("600x500")
    tk.Label(venta2, text="Bienvenido, Administrador").pack()


    boton_registrar_huesped = tk.Button(venta2, text="Registrar Huésped", command=registrar_huesped)
    boton_registrar_huesped.pack()

    
    boton_modificar_huesped = tk.Button(venta2, text="Modificar Huésped", command=modificar_huesped)
    boton_modificar_huesped.pack()

    boton_crear_habitacion = tk.Button(venta2, text="Crear Habitación", command=crear_habitacion)
    boton_crear_habitacion.pack()

    boton_mostrar_habitaciones = tk.Button(venta2, text="Mostrar Habitaciones", command=mostrar_habitaciones)
    boton_mostrar_habitaciones.pack()

def mostrar_habitaciones():
    ventana_habitaciones = tk.Toplevel()
    ventana_habitaciones.title("Lista de Habitaciones")
    ventana_habitaciones.geometry("600x400")

    # Crear un Frame para contener el Treeview y el Scrollbar
    frame = tk.Frame(ventana_habitaciones)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear un Treeview para mostrar las habitaciones
    tree = ttk.Treeview(frame, columns=("Número", "Tipo", "Camas", "Costo por noche", "Disponibilidad"), show="headings")
    tree.heading("Número", text="Número")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Camas", text="Camas")
    tree.heading("Costo por noche", text="Costo por noche")
    tree.heading("Disponibilidad", text="Disponibilidad")

    # Configurar el Treeview para que ocupe todo el espacio disponible
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Añadir un scrollbar para el Treeview
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Insertar datos de las habitaciones en el Treeview
    for habitacion in Habitacion.lista_Habitaciones:
        disponibilidad = "Disponible" if habitacion.disponibilidad else "Ocupada"
        tree.insert("", tk.END, values=(habitacion.numero, habitacion.tipo, habitacion.camas, habitacion.costo, disponibilidad))

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
        admin.crearhabitaciones(numero, tipo, camas, costo)
        ventana_crear.destroy()

    boton_guardar = tk.Button(ventana_crear, text="Guardar", command=guardar_habitacion)
    boton_guardar.pack()




def ventanarecep():
    venta3 = tk.Toplevel()
    venta3.title("Ventana recepción")
    venta3.geometry("600x500")
    tk.Label(venta3, text="Bienvenido, Recepcionista").pack()

    # Botón para ver disponibilidad
    boton_ver_disponibilidad = tk.Button(venta3, text="Ver Disponibilidad", command=ver_disponibilidad)
    boton_ver_disponibilidad.pack()

    # Botón para reservar habitación
    boton_reservar = tk.Button(venta3, text="Reservar Habitación", command=reservar_habitacion)
    boton_reservar.pack()

    # Botón para cancelar reserva
    boton_cancelar = tk.Button(venta3, text="Cancelar Reserva", command=cancelar_reserva)
    boton_cancelar.pack()

def ver_disponibilidad():
    ventana_disponibilidad = tk.Toplevel()
    ventana_disponibilidad.title("Disponibilidad de Habitaciones")
    ventana_disponibilidad.geometry("400x300")

    for habitacion in Habitacion.lista_Habitaciones:
        estado = "Disponible" if habitacion.disponibilidad else "Ocupada"
        tk.Label(ventana_disponibilidad, text=f"Habitación {habitacion.numero}: {estado}").pack()

def reservar_habitacion():
    ventana_reservar = tk.Toplevel()
    ventana_reservar.title("Reservar Habitación")
    ventana_reservar.geometry("400x300")

    tk.Label(ventana_reservar, text="Número de habitación:").pack()
    entrada_numero = tk.Entry(ventana_reservar)
    entrada_numero.pack()

    tk.Label(ventana_reservar, text="Fecha de entrada (YYYY-MM-DD):").pack()
    entrada_fecha_entrada = tk.Entry(ventana_reservar)
    entrada_fecha_entrada.pack()

    tk.Label(ventana_reservar, text="Fecha de salida (YYYY-MM-DD):").pack()
    entrada_fecha_salida = tk.Entry(ventana_reservar)
    entrada_fecha_salida.pack()

    tk.Label(ventana_reservar, text="Nombre del huésped:").pack()
    entrada_huesped = tk.Entry(ventana_reservar)
    entrada_huesped.pack()

    def confirmar_reserva():
        numero = entrada_numero.get()
        fecha_entrada = entrada_fecha_entrada.get()
        fecha_salida = entrada_fecha_salida.get()
        nombre_huesped = entrada_huesped.get()

        habitacion = next((h for h in Habitacion.lista_Habitaciones if h.numero == numero), None)
        huesped = next((h for h in Huesped.lista_huespedes if h.nombre == nombre_huesped), None)

        if habitacion and huesped:
            recepcionista.reservar(habitacion, fecha_entrada, fecha_salida, huesped)
            ventana_reservar.destroy()
        else:
            tk.messagebox.showerror("Error", "Habitación o huésped no encontrado")

    boton_confirmar = tk.Button(ventana_reservar, text="Confirmar Reserva", command=confirmar_reserva)
    boton_confirmar.pack()

def cancelar_reserva():
    ventana_cancelar = tk.Toplevel()
    ventana_cancelar.title("Cancelar Reserva")
    ventana_cancelar.geometry("300x100")

    tk.Label(ventana_cancelar, text="ID de la reserva:").pack()
    entrada_id = tk.Entry(ventana_cancelar)
    entrada_id.pack()

    def confirmar_cancelar():
        id_reserva = int(entrada_id.get())
        reserva = next((r for r in Reserva.lista_reservas if r.id == id_reserva), None)
        if reserva:
            recepcionista.cancelar(reserva)
            ventana_cancelar.destroy()
        else:
            tk.messagebox.showerror("Error", "Reserva no encontrada")

    boton_confirmar = tk.Button(ventana_cancelar, text="Cancelar Reserva", command=confirmar_cancelar)
    boton_confirmar.pack()


ventanainicio()