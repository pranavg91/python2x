class Father:

    def home(self):
        return "father home"
    def father_money(self):
        return "5"

class Mother:

    def home(self):
        return "Mother home"
    def mother_money(self):
        return "6"

class Son(Father,Mother):
    pass

son = Son()
print(Son.mro())
# print(son.father_money())
# print(son.mother_money())
print(son.home())