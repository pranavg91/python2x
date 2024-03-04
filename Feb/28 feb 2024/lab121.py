class GF:

    def car(self):
        return  "Old car"


class F(GF):

    def car(self):
        return "Honda car"


class S(F):

    def car(self):
        return "Lambo car"

s=S()
print(s.car())

