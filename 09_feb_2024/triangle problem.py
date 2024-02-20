#triangle problem
from builtins import print

side1 = int(input("Enter first side "))
side2 = int(input("Enter second side "))
side3 = int(input("Enter third side "))

if side1 == side2 and side1 == side3:
    print("Equaliteral triangel")
elif side1 == side2 or side1 == side3:
    print("isocele")
elif side1 !=side2 or side1 !=side3:
    print("scalene")
else:
    print("Wrong input")