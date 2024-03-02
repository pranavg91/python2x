class Grandfather:

    def home1(self):
        return "Grandfatherhome"

class Father(Grandfather):

    def home2(self):
        return "Father home"

class Son(Father):
    def home3(self):
        return "Son home"

son =Son()
print(son.home1())
print(son.home2())
print(son.home3())
