class car:
    name=None
    model =None
    color =None
    speed =None

    def drive(self):
        print("car drive")

    def start_enigine(self):
        print("start engine")

    def car_break(self):
        print("break")

    def whoisdriving(self):
        print("name is :", self.name)

tesla =car()
lambo =car()
tesla.car_break()
tesla.name ="tesla"
lambo.name ="lambo"
tesla.whoisdriving()
lambo.whoisdriving()
