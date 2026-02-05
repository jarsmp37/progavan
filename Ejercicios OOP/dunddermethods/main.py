from atributos import *

per1=Nombre("Bernardo",18,"Ciencias de la compu")
per2=Nombre("Mich",18,"Ciencias de la compu")
per3=Nombre("Lupita",18,"Ciencia de datos")

print(str(per1))
print(repr(per2))

print(per1+per2)
print(per2*per3)
print(per1==per2)
print(per1==per3)