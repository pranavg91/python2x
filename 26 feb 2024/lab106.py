class Myclass:

    def __init__(self):
        self.name ="Amit"

    def publicfun(self):
        print("public fun")

    def __privatefun(self):
        print("private fun")

    def newpublicfun(self):
        self.__privatefun()

a =Myclass()
a.publicfun()
a.newpublicfun()

#a.__privatefun() # not allowed direct