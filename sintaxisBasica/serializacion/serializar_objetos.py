import pickle

class Vehicle():
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        self.in_motion = False
        self.accelerate = False
        self.brake = False

    def start_up(self):
        self.in_motion = True

    def speed_up(self):
        self.accelerate = True

    def brake_the_car(self):
        self.brake = True

    def state(self):
        print("Make: ", self.make, "\nModel: ", self.model, "\nIn motion: ", self.in_motion,
        "\nAccelerating: ", self.accelerate, "\nBraking: ", self.brake )



auto1 = Vehicle("Mazda", "cxs")
auto2 = Vehicle("Honda", "xyz")
auto3 = Vehicle("Toyota", "abc")

autos = [auto1, auto2, auto3]

fichero = open("losCoches", "wb")

pickle.dump(autos, fichero)

fichero.close()

del(fichero)


#lectura fichero

fichero_lectura = open("losCoches", "rb")

mis_coches = pickle.load(fichero_lectura)

fichero_lectura.close()


#print(mis_coches[1].state())

for c in mis_coches:
    print("+++++++++++++++++++++")
    print(c.state())
    