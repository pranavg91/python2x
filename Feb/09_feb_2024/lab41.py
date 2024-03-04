score = int(input("Enter score "))
if score >=90 and score <=100:
    print("A grade")
elif score >=80 and score <=89:
    print("B grade")
elif score >=70 and score <=79:
    print("C grade")
elif score >=60 and score <=69:
    print("D grade")
elif score >=0 and score <=59:
    print("F grade")
else:
    print("invalid")