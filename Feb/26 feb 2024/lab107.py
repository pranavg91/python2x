class Secureclass:

    def submit(self):
        self.__password = "pass123"
        self.__username = "username"
        self.heading = "VUWheading"
        print(self.__password + "  " +self.__username)
    def publicfun(self):
        self.submit()

s =Secureclass()
s.publicfun()