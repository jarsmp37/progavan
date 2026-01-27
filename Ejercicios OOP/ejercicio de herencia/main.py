from humanidad import *

humano1=Humano("Diana",17,"Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero)
humano1.caract()
humano1.saludo()

programador1=Programador("Gilberto",20,"Masculino")
print(programador1.nombre)
programador1.caract()
programador1.saludo()
programador1.saludo2()

lic1=Licenciado("Brian",23,"No Binario",2134453123)
lic1.saludo()
lic1.caract()