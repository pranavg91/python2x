from builtins import input


class MyCustomException(Exception):

    def __init__(self,message):
        self.message =message
        super().__init__(message)


balance =100
withdraw =int(input("Enter amount of withdraw"))

if withdraw >balance:
    raise MyCustomException("Bal is low")

else:
    print("total after withdraw",balance-withdraw)