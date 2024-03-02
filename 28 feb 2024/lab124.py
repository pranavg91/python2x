class Mathutil:
    def add(self, a,b=0,c=0):
        return a+b+c
    # def add(self,a,b): # not allowed
    #     return a+b

math =Mathutil()

op1=math.add(1)
op2=math.add(1,3,4,)
op3=math.add(1,3)
print(op1)
print(op2)
print(op3)