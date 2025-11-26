class Persona: 
    def __init__  (self, nombre, edad, genero, ocupacion, origen):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion
        self.origen = origen

    def hablar(self):
        print(f"Hola, me llamo {self.nombre}.")
        print(f"Tengo {self.edad}.")
        print(f"Soy {self.genero}.")
        print(f"Soy {self.ocupacion}.")
        print(f"Soy de {self.origen}")

Kein = Persona("Juan Beltrán", "23 edad", "hombre", "estudiante", "Barrancabermeja, Santander")
Kein.hablar()