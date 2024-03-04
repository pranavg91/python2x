# try:
#     pass
# except Exception as e:
#     print(e)
#
#

try:
    a =int(input("Enter number "))
except ValueError as e:
    print(e)
except Exception as v:
    print(v)
else:
    print("else")