class Car():

    def __init__(self) -> None:
        self.__chassis_length = 350 #variable solo puede ser usada desde dentro de la clase
        self.__chassis_width = 150 #variable solo puede ser usada desde dentro de la clase
        self.__tires = 4 #variable solo puede ser usada desde dentro de la clase
        self.__in_motion = False #variable solo puede ser usada desde dentro de la clase
        self.__color = "red" #variable solo puede ser usada desde dentro de la clase

    def start_up(self, start_the_vehicle):
        self.__in_motion = start_the_vehicle
        if self.__in_motion:
            return "The vehicle is running"
        else:
            return "The vehicle is stopped"
     
    def state(self):
        print("the vehicle has ",self.__tires ," tires", " a width of ",
         self.__chassis_width, " cm, and a length of ", self.__chassis_length, " cm." )
        return None

myVehicle = Car()
print(myVehicle.start_up(True))
print(myVehicle.state())

print("-----------------------Next we create another vehicle------------------------")

myVehicle2 = Car()
print(myVehicle2.start_up(False))
print(myVehicle2.state())