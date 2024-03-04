#handle exception
#try and except block

a = int(input("Enter number 1 \n"))
b = int(input("Enter number 2 \n"))


try:
    c = a/b
    print("Div is ",c)

except Exception as e :
    print(e)
    print("Divison by zero is not possible please enter valid number 1 -9")


print("exception is handle")


