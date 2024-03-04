class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fun(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance = self.balance + amount

    #protected method
    def _withdrew (self,amount):
        self.balance = self.balance - amount

    #private method
    def __showbalance(self):
        print("your bal", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__showbalance()
        else:
            print("Not allowed")
    def bank_manager(self,amount):
        self._withdrew(amount = amount)

jp = BankAccount()
jp.deposit(1000)
jp.bank_manager(401)
jp.if_you_are_auth(True)
jp.public_fun()