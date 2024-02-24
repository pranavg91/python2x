class cal:

    def sum(self, a, b):
        return a + b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
    def minus(self, a, b):
        return a - b


obj1_ref = cal()
sumofnumber = obj1_ref.sum(2, 3)
print(sumofnumber)

minusop = obj1_ref.minus(2, 3)
print(minusop)

mulop =obj1_ref.mul(7,5)
print(mulop)
