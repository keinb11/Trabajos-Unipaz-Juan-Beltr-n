class Vehiculo:
    def __init__(self, marca, modelo, color, año, tipo):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")

    def arrancar(self):
        print(f"El {self.tipo} {self.marca} {self.modelo} {self.color} arrancó")

    def parar(self):
        print(f"El {self.tipo} {self.marca} {self.modelo} {self.color} se paró")

autito = Vehiculo("Chevrolet", "Spark", "Vinotinto", 2016, "Carro")


autito.mostrar_info()
autito.arrancar()
autito.parar()
