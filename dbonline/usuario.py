class Usuario:
    """
    Define el objeto de negocio con sus atributos básicos.
    """
    def __init__(self, nombre, color, edad):
        self.nombre = str(nombre)
        self.color = str(color)
        self.edad = int(edad)
    
    def a_diccionario(self):
        """
        Convierte el objeto a un formato que Firestore pueda guardar.
        """
        return {
            'nombre': self.nombre,
            'color': self.color,
            'edad': self.edad
        }

    def __str__(self):
        return f"Usuario(Nombre: {self.nombre}, Color: {self.color}, Edad: {self.edad})"

