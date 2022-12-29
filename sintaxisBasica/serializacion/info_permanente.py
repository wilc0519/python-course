import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con el nombre de:", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []

    def __init__(self):
        lista_de_personas = open("fichero_externo", "ab+")
        lista_de_personas.seek(0)


        try:
            self.personas = pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            lista_de_personas.close()
            del(lista_de_personas)        

    def agregar_personas(self, persona):
        self.personas.append(persona)
        self.guardar_personas_en_fichero_externo()

    def mostrar_personas(self):
        for persona in self.personas:
            print(persona) 

    def guardar_personas_en_fichero_externo(self):
        lista_de_personas = open("fichero_externo", "wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del(lista_de_personas)

    def mostrar_info_de_fichero_esterno(self):
        print("La informacion del fichero externo es la siguiente")
        for persona in self.personas:
            print(persona)

miLista = ListaPersonas()

persona1 = Persona("Nana", "Femenino", 15)
persona2 = Persona("Lilo", "Masculino", 13)
persona3 = Persona("Mela", "Femenino", 8)
persona4 = Persona("David", "Masculino", 12)


miLista.agregar_personas(persona1)
miLista.agregar_personas(persona2)
miLista.agregar_personas(persona3)
miLista.agregar_personas(persona4)
# list.mostrar_personas()

miLista.mostrar_info_de_fichero_esterno()

