def sq_of_number(num):
    return num ** 2


number = [1, 2, 3, 4, 5]
sq_number = list(map(sq_of_number, number))
print(sq_number)
   