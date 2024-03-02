class Father:

    def __init__(self):
        self.__private_var = 50

    def home(self):
        print("Grandfather home")

    def public(self):
        return self.__private_var


class Son(Father):
    pass


son = Son()
son.home()
f = Father()
print(son.public())
