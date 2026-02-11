from clasesocupadas import *

prod1 = Producto("Maruchan", 16, 100)
prod2 = Producto("Coca Cola 600ml", 18, 50)
prod3 = Producto("Papas Sabritas Original", 22, 40)
prod4 = Producto("Leche Entera 1L", 26, 30)
prod5 = Producto("Pan Blanco Grande", 45, 20)
prod6 = Producto("Huevo 12 piezas", 38, 15)
prod7 = Producto("Arroz 1kg", 24, 60)
prod8 = Producto("Frijol Negro 1kg", 32, 45)
prod9 = Producto("Aceite Vegetal 1L", 42, 25)
prod10 = Producto("Azúcar Blanca 1kg", 28, 35)
prod11 = Producto("Café Soluble 100g", 65, 18)
prod12 = Producto("Galletas Oreo", 19, 55)
prod13 = Producto("Atún en Agua", 21, 80)
prod14 = Producto("Pasta para Sopa", 12, 100)
prod15 = Producto("Jabón de Tocador", 15, 40)
prod16 = Producto("Detergente en Polvo 1kg", 36, 22)
prod17 = Producto("Shampoo 400ml", 55, 12)
prod18 = Producto("Papel Higiénico 4 rollos", 29, 30)
prod19 = Producto("Refresco de Naranja 2L", 32, 20)
prod20 = Producto("Chocolate en Barra", 14, 75)

listaproductos=[]
listaproductos.append(prod1)
listaproductos.append(prod2)
listaproductos.append(prod3)
listaproductos.append(prod4)
listaproductos.append(prod5)
listaproductos.append(prod6)
listaproductos.append(prod7)
listaproductos.append(prod8)
listaproductos.append(prod9)
listaproductos.append(prod10)

print(listaproductos)

#cat1=Categoria("Alimentos")
#lst1=[prod4, prod5,prod6,prod7,prod8]
#for a in lst1:
    #cat1.agregar_producto(a)

#print(cat1.lista[0].precio)
#cat1.valor_total_categoria()

pedido1=Pedido("Alfredo")
pedido1.agregar_produto(prod10)
pedido1.agregar_produto(prod8)
pedido1.agregar_produto(prod6)
print(pedido1.lista_comprados)
pedido1.calcula_total()
pedido1.finalizar_pedido()
