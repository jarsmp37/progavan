# Definimos la clase 'Perro'
class Perro:
    # El método __init__ es el constructor de la clase aquí definimos atributos
    def __init__(self, nombre, edad):
        # 'self' hace referencia a la instancia actual del objeto
        # Definimos las propiedades del objeto
        self.nombre = nombre  # Atributo: nombre del perro
        self.edad = edad      # Atributo: edad del perro

    # Método para que el perro "hable"
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")
    
    # Método para calcular la edad en años humanos
    def edad_humana(self):
        return self.edad * 7

# Crear un objeto de la clase 'Perro'
mi_perro = Perro("Rex", 3)

# Llamar a los métodos del objeto
mi_perro.hablar()  
print(f"La edad de {mi_perro.nombre} en años humanos es: {mi_perro.edad_humana()}")
