class shape:

    def area(self):
        print("Area of shape")

class Rectangle(shape):

    def __init__(self,length,breath):
        self.length =length
        self.breath =breath

    def area(self):
        return self.length * self.breath

class Circle(shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
           return 3.14 * self.radius * self.radius

rec =Rectangle(3,4)
print(rec.area())


cir =Circle(4)
print(cir.area())

