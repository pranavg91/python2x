class Grandfather:

    def home(self):
        return  "grandfather home"

class pranav(Grandfather):

    def home(self):
        return "This is pranav home"

class pranavbro(Grandfather):

    def home(self):
        return "This is pranavbro"

pranav =pranav()

print(pranav.home())