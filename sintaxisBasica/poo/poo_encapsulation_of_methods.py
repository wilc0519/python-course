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
            check = self.__internal_check()

        if self.__in_motion and check:
            return "The vehicle is running"
        
        elif self.__in_motion and check == False:
            return "Something went wrong in the check, the vehicle cannot be started."
        else:
            return "The vehicle is stopped"
     
    def state(self):
        print("the vehicle has ",self.__tires ," tires", " a width of ",
         self.__chassis_width, " cm, and a length of ", self.__chassis_length, " cm." )
        return None

    def __internal_check(self): #el methodo solo puede ser usado desde dentro de la clase (encapsulamiento)
        print("performing internal check")
        self.gasoline = "Ok"
        self.oil = "Ok"
        self.doors = "Closed"

        if(self.gasoline == "Ok" and self.oil == "Ok" and self.doors == "Closed"):
            return True
        else:
            return False


myVehicle = Vehicle()
print(myVehicle.start_up(True))
print(myVehicle.state())

print("-----------------------Next we create another vehicle------------------------")

myVehicle2 = Vehicle()
print(myVehicle2.start_up(False))
print(myVehicle2.state())