my_list=[1,2,3]
my_list1=[1,2,3,"pranav",True]

print("Element at index 0 :",my_list[0])  #1

#change the value in list

my_list[1] =20
print(my_list)

#list
my_list.append(30)
print(my_list)

my_list.extend([30,40,5])
print(my_list)

my_list.insert(1,'a')
print(my_list)

my_list.remove('a')
print(my_list)

my_copy_list =my_list.copy()
print(my_copy_list)
print(my_list)

my_list.clear()
print(my_list)
print(my_copy_list)

print("index of 3 in my list ",my_copy_list.index(30))


my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()