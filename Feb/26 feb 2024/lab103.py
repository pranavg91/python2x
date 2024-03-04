class Car:
    name=None
    make=None
    model=None

    

    def __init__(self,o_name,o_make,o_model):
        self.name =o_name
        self.make =o_make
        self.model =o_model


    def enginestart(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


lambo =Car("lambo","v3","sx")
lambo.enginestart()


print("------------------------------------------------")

santro =Car("santro","hyundai","S")
santro.enginestart()