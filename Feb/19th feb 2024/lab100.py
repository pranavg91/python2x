class car:
    color =None
    model =None

    def print(self):
        print("car color & model",self.color,self.model)

car_color = input("enter color\n")
car_model = input("enter model\n")

obj_ref=car()
obj_ref.model =car_model
obj_ref.color =car_color

obj_ref.print()