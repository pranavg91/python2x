class Protect:

#protected value
    _protect_var1 ="protectvalue"

    def __init__(self):
        print("I'll call at the time of object creation ")

#protected fun
    def _pro_fun(self):
        print(self._protect_var1)

    def myfun(self):
        print(self._protect_var1)

pro = Protect()
pro._pro_fun()
pro.myfun()