from backend import *

usuario1=Usuario("Bryan",23,"Bongles")
usuario2=Usuario("Wen",18,"Pasta")
usuario3=Usuario("Fanny",18,"Hamburguesas")

print(usuario1.mostrar_info())
print(usuario2.mostrar_info())
print(usuario3.mostrar_info())

print(Usuario.mostrar_usuarios())
Usuario.guardar_usuarios()