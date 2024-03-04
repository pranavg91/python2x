# noinspection PyRedundantParentheses
class abc:

    def fun(self):
        try:
            a = int(input("Enter a number\n"))

        except Exception as v:
            print("enter number only 0-9")

        else:
            print("You have enter number only")

        finally:
            print("I'll execute always")

obj1 =abc()
obj1.fun()