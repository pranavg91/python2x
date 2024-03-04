from abc import ABC,abstractmethod


class ATB(ABC):

    @abstractmethod
    def learn(self):
        pass
    def writecode(self):
        pass

class pranav(ATB):

    def learn(self):
        return "Learning"

    def writecode(self):
        return "writecode"

class pranav1(ATB):
    pass


obj1= pranav()
print(obj1.learn())
print(obj1.writecode())


obj2= pranav1()
