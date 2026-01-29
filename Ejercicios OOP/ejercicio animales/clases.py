class Animal():
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido(self):
        print("El animal hace un sonido genérico")

class Conejo(Animal):
    def sonido(self):
        print("El conejo hace snif snif")
    
    def carac(self):
        print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animal):
    def __init__(self,nombre,color,patas,pico):
        super().__init__(nombre,color,patas)
        self.pico=pico
    def sonido(self):
        print("El Ornitorrinco hace brrr brrrr")
    
    def carac(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es color {self.color}, tiene {self.patas} patas y su pico mide {self.pico} cm")

class Dinosaurio(Animal):
    tipo="Dinosaurio"
    def sonido(self):
        print("El Dinosaurio hace RAAAAAAAWWRRRRR")
    
    def carac(self):
        print(f"Mi dino se llama {self.nombre}, es color {self.color}, tiene {self.patas} patas y soy un {self.tipo}")



