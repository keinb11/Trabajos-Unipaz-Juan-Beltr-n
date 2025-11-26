class Personajes: 
    def __init__(self, nombre, edad, debilidades, color_de_piel, estatura, hechizo_fuerte, lugar_de_origen, tipo_personaje, equipo_especial, vidas, resistencia, habilidades, oficio, poder_equipo, tipo_arma, nivel_arma, daño_arma):
        self.nombre = nombre
        self.edad = edad
        self.debilidades = debilidades
        self.color_de_piel = color_de_piel
        self.estatura = estatura
        self.hechizo_fuerte = hechizo_fuerte
        self.lugar_de_origen = lugar_de_origen
        self.tipo_personaje = tipo_personaje
        self.equipo_especial = equipo_especial
        self.vidas = vidas
        self.resistencia = resistencia
        self.habilidades = habilidades
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.tipo_arma = tipo_arma
        self.nivel_arma = nivel_arma
        self.daño_arma = daño_arma

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
        print(f"Soy un {self.edad}.")
        print(f"Mis debilidades son {self.debilidades}.")
        print(f"Mi color de piel es {self.color_de_piel}.")
        print(f"Mido {self.estatura}.")
        print(f"Mi hechizo fuerte es {self.hechizo_fuerte}.")
        print(f"Vengo de {self.lugar_de_origen}.")
        print(f"Tipo de personaje: {self.tipo_personaje}")
        print(f"Equipo especial: {self.equipo_especial}")
        print(f"Vidas: {self.vidas}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Habilidades: {self.habilidades}")
        print(f"Oficio: {self.oficio}")
        print(f"Poder del equipo: {self.poder_equipo}")
        print(f"Tipo de arma: {self.tipo_arma}")
        print(f"Nivel del arma: {self.nivel_arma}")
        print(f"Daño del arma: {self.daño_arma}")


Guerrero = Personajes("Kein", "elfo oscuro", "luz solar y agua", "oscuro", "1.80 metros", "Bola de Fuego", "Bosque Tenebroso", "Guerrero", "Armadura Oscura, Espada Larga", "3", "3000", "4000", "Soldado de élite", "3500", "Espada Larga", "Leyenda", "45000")


class NPC(Personajes):
    def __init__(self, nombre, rol, descripcion, tipo_personaje, equipo_especial, vidas, resistencia, habilidades, oficio, poder_equipo, tipo_arma, nivel_arma, daño_arma):
        super().__init__(nombre, None, None, None, None, None, None, tipo_personaje, equipo_especial, vidas, resistencia, habilidades, oficio, poder_equipo, tipo_arma, nivel_arma, daño_arma)
        self.rol = rol
        self.descripcion = descripcion

        self.tipo_personaje = tipo_personaje
        self.equipo_especial = equipo_especial
        self.vidas = vidas
        self.resistencia = resistencia
        self.habilidades = habilidades
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.tipo_arma = tipo_arma
        self.nivel_arma = nivel_arma
        self.daño_arma = daño_arma

    def hablar(self):
        print(f"Hola, soy {self.nombre}, un(a) {self.rol}.")
        print(f"Soy {self.descripcion}.")
        print(f"Tipo de personaje: {self.tipo_personaje}")
        print(f"Equipo especial: {self.equipo_especial}")
        print(f"Vidas: {self.vidas}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Habilidades: {self.habilidades}")
        print(f"Oficio: {self.oficio}")
        print(f"Poder del equipo: {self.poder_equipo}")
        print(f"Tipo de arma: {self.tipo_arma}")
        print(f"Nivel del arma: {self.nivel_arma}")
        print(f"Daño del arma: {self.daño_arma}")


NPC1 = NPC("Kael Dravon", "Guerrero Joniano", "un soldado nacido de las llamas de un dragón ancestral, con un gran poder oculto", "Guerrero", "Armadura de Dragón, Espada Llameante", "3", "5000", "6000", "Soldado", "3000", "Espada Llameante", "Raro", "5000")


print("Información del Guerrero:")
Guerrero.hablar()

print("\nInformación del NPC:")
NPC1.hablar()

input("\nPresiona Enter para salir...")
