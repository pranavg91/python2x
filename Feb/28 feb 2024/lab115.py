class Grandfather:

    def grand_father(self):
        return "Grandfather"

class Father(Grandfather):

    def father(self):
        return "Father"

class son(Father):
    def sonfun(self):
        return "Son"

obj1 = son()
print(obj1.father())
print(obj1.grand_father())
print(obj1.sonfun())
