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

class ElectricVehicles:
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

class Van(Vehicle):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "la furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Motorcycle(Vehicle):
    do_horse = ""
    def horse(self):
        self.do_horse = "I'm doing the wheelie"

    def state(self):
        print("Make: ", self.make, "\nModel: ", self.model, "\nIn motion: ", self.in_motion,
        "\nAccelerating: ", self.accelerate, "\nBraking: ", self.brake, "\nDo Horse", self.do_horse )

myMotorcycle = Motorcycle("Honda", "CBR")
myMotorcycle.start_up()
myMotorcycle.horse()
myMotorcycle.state()

myVan = Van("Renault", "Kangoo")
myVan.start_up()
myVan.state()
print(myVan.carga(True))

class BicicletaElectrica(ElectricVehicles, Vehicle):

    pass

myBicicletaElectrica = BicicletaElectrica()