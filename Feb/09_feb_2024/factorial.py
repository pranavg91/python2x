num = int(input("Enter number"))
if num < 0:
    print("factorial is not possible")
else:
    fact = 1
    for i in range(1,num +1):
        fact =fact * i
    print(fact)