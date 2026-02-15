from clasesocupadas import *

# 1. Crear la Tienda
mi_tienda = Tienda("Supermercado 'El Programador'")

# 2. Definir Productos 
p1 = Producto("Arroz 1kg", 24, 60)
p2 = Producto("Frijol Negro 1kg", 32, 45)
p3 = Producto("Huevo 12 piezas", 38, 15)
p4 = Producto("Coca Cola 600ml", 18, 50)
p5 = Producto("Café Soluble 100g", 65, 18)
p6 = Producto("Leche Entera 1L", 26, 30)
p7 = Producto("Jabón de Tocador", 15, 40)
p8 = Producto("Detergente en Polvo 1kg", 36, 22)
p9 = Producto("Shampoo 400ml", 55, 12)

# Lista maestra para sincronizar stock al final
inventario_total = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

# 3. Crear 3 Categorías 
cat_alimentos = Categoria("Alimentos")
cat_bebidas = Categoria("Bebidas")
cat_limpieza = Categoria("Limpieza")

# Agregar productos a categorías
for p in [p1, p2, p3]: cat_alimentos.agregar_producto(p)
for p in [p4, p5, p6]: cat_bebidas.agregar_producto(p)
for p in [p7, p8, p9]: cat_limpieza.agregar_producto(p)

# Registrar categorías en la tienda
mi_tienda.registrar_categoria(cat_alimentos)
mi_tienda.registrar_categoria(cat_bebidas)
mi_tienda.registrar_categoria(cat_limpieza)

#Probando los métododos de cada objeto

print("\n" + "="*40)
print(" PRUEBA 1: Métodos de Producto")
print("="*40)
p5.aplicar_descuento(0.10)  
p1.actualizar_stock(10)     
p1.actualizar_stock(-100)   

print("\n" + "="*40)
print(" PRUEBA 2: Valor por Categoría")
print("="*40)
valor = mi_tienda.valor_total_categoria("Alimentos")
print(f"Confirmación: El valor retornado a la tienda es ${valor}")

print("\n" + "="*40)
print(" PRUEBA 3: Gestión de Pedidos")
print("="*40)
pedido_sugey = Pedido("Sugey")
pedido_sugey.agregar_produto(p5) 
pedido_sugey.agregar_produto(p3) 


total_con_iva = pedido_sugey.calcular_total()
print(f"Total calculado para {pedido_sugey.cliente}: ${total_con_iva:.2f}")

# Finalizar pedido 
print(f"Stock antes de finalizar: {p5.nombre} = {p5.stock}")
pedido_sugey.finalizar_pedido(inventario_total)
print(f"Stock después de finalizar: {p5.nombre} = {p5.stock}")

# Agregar el pedido a la tienda para que aparezca en el reporte
mi_tienda.pedidos_realizados.append(pedido_sugey)

print("\n" + "="*40)
print(" PRUEBA 4: Reportes de Tienda")
print("="*40)
mi_tienda.generar_reporte_ventas()
mi_tienda.producto_mas_caro()