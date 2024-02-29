class GF:
    def home(self):
        print("GF home")

class Father(GF):
    def home1(self):
        print("GOA home")

class Son(Father):
    def home2(self):
        print("Delhi home")

obj1 =Son()
obj1.home()
obj1.home1()
obj1.home2()


mmd =Father()
mmd.home()
mmd.home1()
#mmd.home2()

gkd =GF()
gkd.home()
