from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):

    def sound(self):
        return "bew bew"

class Cat(Animal):

    def sound(self):
        return "meow"

obj =Dog("gogo")
print(obj.sound())


k=Cat("Brown")
print(k.sound())
