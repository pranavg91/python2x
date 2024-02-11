# find maximum number between 3 number
num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))
if num1 > num2 and num1 > num3:
    print("Num1 is maximum")
elif num2 > num1 and num2 > num3:
    print("num2 is max")
elif num3 > num1 and num3 > num1:
    print("num3 is max")
else:
    print("Enter number")
# max =max(num1,num2,num3)
# print(max)

