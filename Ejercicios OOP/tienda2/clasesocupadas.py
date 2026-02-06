class Producto():
    def __init__(self,nom, prec,stok):
        self.nombre=nom
        self.precio=prec
        self.stock=stok
    
    def aplicar_descuento(self,porcentaje):
        self.precio*=(1-porcentaje)
        print(f"El nuevo precio del producto {self.nombre} es {self.precio}")

    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("No hay suficiente stock")
        else:
            self.stock+=cantidad
            print(f"El nuevo stock de {self.nombre} es {self.stock}")

class Categoria():
    def __init__(self,nomb):
        self.nombre_cat=nomb
        self.lista=[]

    def agregar_producto(self,producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.lista:
            suma+=m.precio*m.stock
        print(f"El precio total de la categoria {self.nombre_cat} es {suma} pesos")
