# #reverse of string
#
# str ="pramod"
# revstr=""
# for c in str:
#     revstr = c + revstr
#
# print(revstr)

def reverse_str(str):
    rev =" "
    for c in str:
        rev = c + rev
    return rev

original_string =input("enter string")
original_string =original_string.lower()

result = reverse_str(original_string)
print(result)

#palidrome  madam-->madam
if original_string == result:
    print("palidrome")
else:
    print("Not a palidrome")


