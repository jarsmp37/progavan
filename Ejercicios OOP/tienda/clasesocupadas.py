class Producto():
    def __init__(self,nom,prec,stok):
        self.nombre=nom
        self.precio=prec
        self.stock=stok
    def aplicar_descuento(self,porcentaje):
        self.precio*=(1-porcentaje)
        print(f"el nuevo precio es {self.precio}")
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("no puedes tener stock negativo")
        else:
            self.stock+=cantidad
            print(f"la nueva cantidad es {self.stock}")

class Categoria():
    def __init__(self,nomcat):
        self.nombre_cat=nomcat
        self.lista=[]
    def agregar_producto(self,producto):
        self.lista.append(producto)
        print(f"el producto {producto.nombre} se agrego a la lista")
    def valor_total_categoria(self):
        suma=0
        for b in self.lista:
            suma+=b.precio
        print(f"el valor total de la categoria es {suma}")

class Pedido():
    def __init__(self,cliente):
        self.cliente=cliente
        self.lista_comprados=[]
        self.estado="Pendiente"
    
    def agregar_produto(self,product):
        self.lista_comprados.append(product)
        print(f"Agregaste el producto {product.nombre} al carrito")
    
    def calcula_total(self):
        total=0
        for x in self.lista_comprados:
            total+=x.precio
        
        print(f"El total de productos comprados es ${total}, el iva es ${0.16*total} y dando sumado ${1.16*total:0.2f}")
