#match

number =int(input("Enter number \n"))
match number:
    case 1 :
        print("Enter number is 1")
    case 2:
        print("Enter number is 2")
    case 3:
        print("Enter number is 3")
    case 4:
        print("Enter number is 4")
    case _:
        print("Default case")