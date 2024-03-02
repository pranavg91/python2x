class vehicle:

    def info(self):
        return  "this is a vehicle class"

class car(vehicle):
    pass

class motorcycle(vehicle):
    def info(self):
        return "this is a vehicle motorcycle"


co=car()
print(co.info())
