class VWOlogin:

    email =None
    password =None

    def __init__(self,email,password):
        self.email =email
        self.password =password

    def login(self):
        if self.password == "pass123":
            print("Allowed to login")
        else:
            print("Invalid user")

login1=VWOlogin("pranav@gmail.com","pass123")
login1.login()\
    
print(id(login1 ))

print("-------------------------------------------------------- ")
login2=VWOlogin("pranav123@gmail.com","pass13423")
login2.login()