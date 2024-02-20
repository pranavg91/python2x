t=("thetesting","HHH","thetesting")
print(set(t))


set1={1,2,3,3}
set2={4,5,6}

my_union=set1.union(set2)
print(my_union)

set3={1,2,3,3}
set4={3,4,5,6}

my_union1=set3.intersection(set4)
print(my_union1)

diff=set3.difference(set4)
print(diff)

   diff1=set4.difference(set3)
print(diff1)