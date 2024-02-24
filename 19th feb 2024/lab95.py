class person:

    #Person attribute -> data members
    name =None
    age =None
    id=None

    #Behaviour -> methods
    def talk(self):
        print("i can talk")

    def walk(self):
        print("i can walk")

    def sleep(self):
        print("i can sleep")

def fun():
    print("I am function")

#object creation objectname = classname
pranav = person()
pranav.sleep()
pranav.walk()
pranav.walk()
pranav.name ="pranav"
print(pranav.name)
fun()

