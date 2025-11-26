class miembro_ejercito:
    def __init__(self, ID, Rango, Nombre, Peloton):
        self.ID = ID 
        self.Rango = Rango
        self.Nombre = Nombre
        self.Peloton = Peloton
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Pelotón: {self.Peloton}")

class SoldadoRuso(miembro_ejercito):
    def __init__(self, ID, Rango, Nombre, Peloton, alias, tiempo_servicio_prestar):
        super().__init__(ID, Rango, Nombre, Peloton)
        self.alias = alias
        self.tiempo_servicio_prestar = tiempo_servicio_prestar
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Pelotón: {self.Peloton}, Alias: {self.alias}, Tiempo de servicio a prestar: {self.tiempo_servicio_prestar}")

class Cabo(miembro_ejercito):
    def __init__(self, ID, Rango, Nombre, Peloton, tiempo_servicio_prestado):
        super().__init__(ID, Rango, Nombre, Peloton)
        self.tiempo_servicio_prestado = tiempo_servicio_prestado
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Pelotón: {self.Peloton}, Tiempo de servicio prestado: {self.tiempo_servicio_prestado}")

class Sargento(miembro_ejercito):
    def __init__(self, ID,Rango, Nombre, Peloton, a_cargo_peloton):
        super().__init__(ID, Rango, Nombre, Peloton)
        self.a_cargo_peloton = a_cargo_peloton
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Pelotón: {self.Peloton}, A cargo de pelotón: {self.a_cargo_peloton}")

class Teniente(miembro_ejercito):
    def __init__(self, ID, Rango, Nombre, Peloton, num_oficiales_a_cargo):
        super().__init__(ID, Rango, Nombre, Peloton)
        self.num_oficiales_a_cargo = num_oficiales_a_cargo
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Pelotón: {self.Peloton}, Número de oficiales a cargo: {self.num_oficiales_a_cargo}")

class General(miembro_ejercito):
    def __init__(self, ID, Rango, Nombre,Peloton, batallon_a_cargo):
        super().__init__(ID, Rango, Nombre,Peloton)
        self.batallon_a_cargo = batallon_a_cargo
    def info(self):
        print(f"Rango: {self.Rango}, ID: {self.ID}, Nombre: {self.Nombre}, Batallón a cargo: {self.batallon_a_cargo}")

soldado1 = SoldadoRuso("Soldado", "001", "Chamorrito", "Pelotón A", "Morrito El Ruso", "12 meses")
cabo1 = Cabo("CB-010", "Granaditos", "Pelotón B", "16 meses", "16 meses")
sargento1 = Sargento("Sargento", "100", "Gabrielita", "Pelotón C", "Sí")
teniente1 = Teniente("Teniente", "200", "Johansiño", "Pelotón D", "5")
general1 = General("General", "900", "Keinsiño","Sin pelotón", "2 batallones")

if __name__ == "__main__":
    print("\nMiembros del ejército")
    print("\nSoldado (ruso):")
    soldado1.info()

    print("\nCabo:")
    cabo1.info()

    print("\nSargento:")
    sargento1.info()

    print("\nTeniente:")
    teniente1.info()

    print("\nGeneral:")
    general1.info()

input("Presiona Enter para salir...")