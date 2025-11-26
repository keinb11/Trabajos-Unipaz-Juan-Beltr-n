# ahora creemos un input para que el usuario elija un personaje y muestre sus caracteristicas y agregar un npc elegible
if __name__ == "__main__":
    print("Elige un personaje:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Curandero")
    print("4. Demonio")
    print("5. Cazadora")
    eleccion = input("Ingresa el número del personaje que deseas conocer: ")

class Personajes: 
    def __init__  (self, nombre, edad, debilidades, color_de_piel, estatura, hechizo_fuerte, lugar_de_origen):
        self.nombre = nombre
        self.edad = edad
        self.debilidades = debilidades
        self.color_de_piel = color_de_piel
        self.estatura = estatura
        self.hechizo_fuerte = hechizo_fuerte
        self.lugar_de_origen = lugar_de_origen

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
        print(f"Soy un {self.edad}.")
        print(f"Mis debilidades son {self.debilidades}.")
        print(f"Mi color de piel es {self.color_de_piel}.")
        print(f"Mido {self.estatura}.")
        print(f"Mi hechizo fuerte es {self.hechizo_fuerte}.")
        print(f"Vengo de {self.lugar_de_origen}.")

Guerrero = Personajes( "Kein", "elfo oscuro", "luz solar y agua", "oscuro", "1.80 metros", "Bola de Fuego", "Bosque Tenebroso")
Mago = Personajes("Elandra", "elfa", "fuego y tierra", "claro", "1.70 metros", "Rayo Congelante", "Montañas Brillantes")
Curandero = Personajes("Tharok", "enano", "magia oscura y venenos", "rojizo", "1.50 metros", "Sanación Suprema", "Colinas Rocosas")
Demonio = Personajes("Zarath", "demonio", "agua bendita y símbolos sagrados", "rojo intenso", "2.00 metros", "Llama Infernal", "Abismo Ardiente")
Cazadora = Personajes("Lyria", "humana", "magia oscura y trampas", "bronceado", "1.65 metros", "Flecha Teledirigida", "Tierras Salvajes")

if eleccion == "1":
        Guerrero.hablar()
elif eleccion == "2":
        Mago.hablar()
elif eleccion == "3":
        Curandero.hablar()
elif eleccion == "4":
        Demonio.hablar()
elif eleccion == "5":
        Cazadora.hablar()
else:
        print("Elección no válida.")

class NPC:
    def __init__  (self, nombre, rol, descripcion):
        self.nombre = nombre
        self.rol = rol
        self.descripcion = descripcion

    def hablar(self):
        print(f"Hola, soy {self.nombre}, un(a) {self.rol}.")
        print (f"Soy {self.descripcion}.")

NPC1 = NPC ("Arwen Lysveil", "Arquera elfa", "Silenciosa y precisa, guío a los héroes a través de los senderos prohibidos y organizo emboscadas a los enemigos con mi arco lunar")
NPC2 = NPC ("Kael Dravon", "Guerrero Joniano", "un soldado nacido de las llamas de un dragón ancestral, con un gran poder oculto")
NPC3 = NPC ("Nira Valenheart", "Maga sanadora", "devota y sabia, canalizo la energia celestial para curar y proteger a mis aliados")

print("\n¿Deseas añadir un NPC?")
print("1. Arwen Lysveil")
print("2. Kael Dravon")
print("3. Nira Valenheart")
npc_eleccion = input("Ingresa el número del NPC que quieres que acompañe a tu héroe: ")

if npc_eleccion == "1":
    NPC1.hablar()
elif npc_eleccion == "2":
    NPC2.hablar()
elif npc_eleccion == "3":
    NPC3.hablar()
else:
    print("Elección no válida de NPC.")
    
input ("\nPresiona Enter para salir...")