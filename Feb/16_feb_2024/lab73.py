import math

def sq_root(num):
    return math.sqrt(num)
my_list = [2.4,6]
sq_root_of_num = list(map(sq_root,my_list))
print(sq_root_of_num)