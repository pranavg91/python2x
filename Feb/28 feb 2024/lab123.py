#method overriding

class Animal():

    def __init__(self):
        pass
    def sound(self):

        print("Animal sound")

class Dog(Animal):

    def __init__(self):
        pass
    def sound(self):
        super().sound()
        print("Dog sound")

# obj =Animal()
# obj.sound()

obj1 =Dog()
obj1.sound()