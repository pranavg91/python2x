side1 = float(input("enter side 1\n"))
side2 = float(input("enter side 2\n"))
side3 = float(input("enter side 3\n"))
if side1 == side2 == side3:
    print("eq")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isoceles")
else:
    print("scalne")