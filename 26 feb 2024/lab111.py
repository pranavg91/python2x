from enum import _is_private


class Father:

    gold =4
    __private_villa_access ="GOA"
    def car(self):
        print("lambo")

    def threebhkflat(self):
        print("father flat")

    def private_villa(self):
        print(self.__private_villa_access)
class son(Father):
    pass

obj1 = son()
obj1.car()
obj1.threebhkflat()
print(obj1.gold)
obj1.private_villa()

mmd =Father()
mmd.car()
mmd.threebhkflat()
mmd.gold