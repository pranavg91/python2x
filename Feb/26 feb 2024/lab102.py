class Person:
    name ="Amit"
    age =None

    def walk(self):
        print("Hi your name is ",self.name)
        print("Hi your age is ",self.age)
    def __init__(self,name,age):
        self.name =name
        self.age =age



p =Person("pranav",45)
p.walk()