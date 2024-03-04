my_dict = {'b':1,'a':4,'c':8}
for k,v in my_dict.items():
    if k == 'b':
        print("B is found")

#other way

op='b' in my_dict
print(op) 