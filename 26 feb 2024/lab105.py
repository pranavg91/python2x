class Car:
    name =None

    def __init__(self):
        self.public ="public"
        self._protected_var ="protected"
        self.__password ="pass123"

    def printname(self):
        print("car name is " + self.name)

    def printpass(self):
        print("password value is " + self.__password)

xuv = Car()
print(xuv.public)
print(xuv._protected_var)
print("-----------------")

xuv.printpass() 

