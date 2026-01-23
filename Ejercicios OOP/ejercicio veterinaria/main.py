from animales import *

perro1=Perro("Fido","negro")
perro2=Perro("Rex","blanco")
perro3=Perro("Firulais","cafe")

gato1=Gato("Michi","moteado")
gato2=Gato("Victor","azul")
gato3=Gato("Thor","negro")

kang1=Canguro("Fery","cafe1")
kang2=Canguro("JAck","cafe2")
kang3=Canguro("Rocky","cafe3")

vet1=Veterinaria("Los ángeles")
vet1.agregar(perro1)
vet1.agregar(perro2)
vet1.agregar(perro3)
vet1.agregar(gato1)
vet1.agregar(gato2)
vet1.agregar(gato3)
vet1.agregar(kang1)
vet1.agregar(kang2)
vet1.agregar(kang3)
#print(vet1.lista)
print(vet1.lista[0].tipo, vet1.lista[0].nombre, vet1.lista[0].color,vet1.lista[0].sonido())
print(f"El animal es un {vet1.lista[0].tipo} su nombre es {vet1.lista[0].nombre} y es de color {vet1.lista[0].color} y hace el sonido {vet1.lista[0].sonido()}")
print(vet1.inventario())