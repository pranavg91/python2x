#try,except and finally

try:
    a = int(input("Enter 1st number\n"))
    b = int(input("Enter 2nd number\n"))
    c=a/b

except ValueError as v:
    print("value error")

except ZeroDivisionError as z:
    print("0 is not allowed")

else:
    print("Div is ",c)
finally:
    print("I always execute")


