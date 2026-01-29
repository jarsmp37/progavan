from clases import *

animal=Animal("Sparky","azul",4)
print(animal.nombre)
print(animal.color)
print(animal.patas)
animal.sonido()

conejo=Conejo("Juan","Blanco",8)
conejo.sonido()
conejo.carac()

ornit=Ornitorrinco("Perry","Azul turquesa",2,20)
ornit.sonido()
ornit.carac()

dino=Dinosaurio("Fer","Verde",2)
dino.sonido()
dino.carac()