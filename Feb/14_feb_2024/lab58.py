#*args and *krgs

def f1(a,b,c):
    return a+b+c
#f1()
#f1(1)
#f1(1,2)
f1(1,2,3)
final=f1(a=1,b=2,c=3)
print(final)


def print_arg(*args):
    for i in args:
        print(i,end =" ")
print_arg(1)
print_arg(1,2)
print_arg(1,4,5)
print_arg(1,"hello","bata")
