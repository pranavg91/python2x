# def saay_hello():
#     print("hello")
# saay_hello()


def saay_hello(name,age): # function with argument
    print("name",name)
    print("age",age)
saay_hello("pranav",23 )


def say_hello_my(name ="pranav"):
    print("hello  ",name)

say_hello_my()
say_hello_my(name = "lucky")


def sum_of_number(a,b):
    return  a+b
sum = sum_of_number(10,2)
print("sum of number:",sum)

#add =sum_of_number("amit",34) #TypeError: can only concatenate str (not "int") to str
#print(add)

add1=sum_of_number(a = 12,b =32)
print(add1)