class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")


class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")



miMoto = Moto()
miMoto.desplazamiento()

miCoche = Coche()
miCoche.desplazamiento()
#----------------polymorphysn---------------------------
miCamion = Camion()
miCamion.desplazamiento()

def desplazamiento(vehiculo):
    vehiculo.desplazamiento()

miVeliculo = Camion()
desplazamiento(miVeliculo)