class Empleado:
    def __init__(self, nombre, id, rol):
        self.nombre = nombre
        self.id = id
        self.rol = rol

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi id es {self.id} y mi rol en la empresa es {self.rol}.")

empleado1 = Empleado("Juan Kein", "001", "Empleado")
empleado1.presentarse()

SMLV = 1750000

class Gerente(Empleado):
    def __init__(self, nombre, id):
        super().__init__(nombre, id, "Gerente")
        self.salario = 3 * SMLV

    def presentarse(self):
        super().presentarse()
        print(f"Mi salario es: ${self.salario:,}")

class EmpleadoOrdinario(Empleado):
    def __init__(self, nombre, id, horas_trabajo):
        super().__init__(nombre, id, "Empleado Ordinario")
        self.horas_trabajo = horas_trabajo
        self.salario = 2 * SMLV

    def presentarse(self):
        super().presentarse()
        print(f"Mis horas de trabajo son: {self.horas_trabajo}")
        print(f"Mi salario es: ${self.salario:,}")

gerente1 = Gerente("Chamorriño Granadiño", "1234")
empleado1 = EmpleadoOrdinario("Gabigol", "3123", 160)

gerente1.presentarse()
empleado1.presentarse()

input("Presiona Enter para salir...")