class A:
     def home1(self):
         print("A home")

class B(A):
    def home2(self):
        print("B home")

class C(A):
    def home3(self):
        print("C home")


objc= C()
objc.home1()
objc.home3()