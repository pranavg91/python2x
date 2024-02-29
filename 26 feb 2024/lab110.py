class Password:

    def __init__(self,password):
        self.__password = password
        self.public_var = 10


    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("invalid password")

    def set_password(self,password): 
            if len(password) > 10:
                self.__password == password
                print(self.__password)
            else:
                print("Not allowed week password")

pwd =Password("hacker123")

#print(pwd.__password)

pwd.get_password(True)
pwd.set_password("pran7")