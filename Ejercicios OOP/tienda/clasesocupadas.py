class Producto():
    def __init__(self, nom, prec, stok):
        self.nombre = nom
        self.precio = prec
        self.stock = stok

    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje)
        print(f"El nuevo precio de {self.nombre} es {self.precio}")

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad) < 0:
            print("No puedes tener stock negativo")
        else:
            self.stock += cantidad
            print(f"La nueva cantidad de {self.nombre} es {self.stock}")

class Categoria():
    def __init__(self, nomcat):
        self.nombre_categoria = nomcat
        self.lista = []

    def agregar_producto(self, producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} se agregó a la categoría {self.nombre_categoria}")

    def valor_total_categoria(self):
        suma = sum(b.precio for b in self.lista)
        print(f"El valor total de la categoría {self.nombre_categoria} es {suma}")
        return suma

class Pedido():
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.lista_comprados = []
        self.estado = "Pendiente"
    
    def agregar_produto(self, product):
        self.lista_comprados.append(product)
        print(f"Agregaste {product.nombre} al carrito")
    
    def calcular_total(self):
        total_base = sum(x.precio for x in self.lista_comprados)
        total_con_iva = total_base * 1.16
        return total_con_iva
    
    def finalizar_pedido(self, listab):
        self.estado = "Completado"
        for x in self.lista_comprados:
            for y in listab:
                if x.nombre == y.nombre:
                    y.stock -= 1
                    print(f"Del producto {y.nombre} se quitó una unidad. Stock restante: {y.stock}")

class Tienda():
    def __init__(self, nombre_tienda: str):
        self.nombre_tienda = nombre_tienda
        self.categorias: list[Categoria] = []
        self.pedidos_realizados: list[Pedido] = []

    def registrar_categoria(self, categoria: Categoria):
        self.categorias.append(categoria)

    def generar_reporte_ventas(self):
        
        total_ingresos = sum(p.calcular_total() for p in self.pedidos_realizados if p.estado == "Completado")
        
        print(f"\n--- Reporte {self.nombre_tienda} ---")
        for pedido in self.pedidos_realizados:
            print(f"Pedido de {pedido.cliente}: Total con IVA = ${pedido.calcular_total():.2f}, Estado: {pedido.estado}.")
        print(f"Ingresos totales (completados): ${total_ingresos:.2f}")

    def producto_mas_caro(self):
        producto_max = None
        precio_max = -1
        for cat in self.categorias:
            for prod in cat.lista: 
                if prod.precio > precio_max: 
                    precio_max = prod.precio
                    producto_max = prod
        
        if producto_max:
            print(f"El producto más caro es: {producto_max.nombre} (${producto_max.precio:.2f}).")
        else:
            print("No hay productos en inventario.")
    
    def valor_total_categoria(self, nombre_categoria):
        for cat in self.categorias:
            # Verifica que el nombre coincida con el de la categoría
            if cat.nombre_categoria == nombre_categoria:
                return cat.valor_total_categoria()
        print(f"La categoría '{nombre_categoria}' no existe.")
        return 0.0