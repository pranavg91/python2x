class mul_param:

    name=None

    def nameinfo(self,firstname,lastname,age):
        print("your info is :",firstname,lastname,age)
        print(self.name)

obj_ref = mul_param()
obj_ref.nameinfo("Pranav","Gupta",33)

obj_ref.name ="Himani"
print(obj_ref.name)

