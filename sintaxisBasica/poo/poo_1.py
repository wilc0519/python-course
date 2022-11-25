class Vehicle():

    def __init__(self) -> None:
        self.__chassis_length = 350
        self.__chassis_width = 150
        self.__tires = 4
        self.__in_motion = False
        self.__color = "red"

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

myVehicle = Vehicle()
print(myVehicle.start_up(True))
print(myVehicle.state())

print("-----------------------Next we create another vehicle------------------------")

myVehicle2 = Vehicle()
print(myVehicle2.start_up(False))
print(myVehicle2.state())