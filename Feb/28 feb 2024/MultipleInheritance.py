class A:
    def home1(self):
        print("A home")
    def car(self):
        print("A car")

class B:
    def home2(self):
        print("B home")
    def car(self):
        print("B car")

class C(A,B):

    def home3(self):
        print("C home")


c =C()

c.home1()
c.home2()
c.home3()
c.car()


print("--------------------------------------------------")
d= B()
d.home2()
