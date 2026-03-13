from backend import *

usuario1=Usuario("Gael",23,"Croquetas de atún")
usuario2=Usuario("Dana",19,"Lassagna")
usuario3=Usuario("Camy",18,"Tacos")

print(usuario1.mostrar_datos())
print(usuario2.mostrar_datos())
print(usuario3.mostrar_datos())

Usuario.mostrar_lista()