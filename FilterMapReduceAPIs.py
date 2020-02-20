min = (lambda x, y: x if x < y else y)
print(min(101*99,102*98))  #Output = 9996
print(min(10*21,24*9))  #Output = 210

# Map

#Without lambdas

a=[1,2,3,4,5]
def foo(a):
    return 3*a
print(list(map(foo,a)))

#Output : [3, 6, 9, 12, 15]

#With lambdas

a=[1,2,3,4]
b=[17,12,11,10]
c=[-1,-4,5,9]

print(list(map(lambda x,y : x+y,a,b) )         )              # Output : [18,14,14,14]
print(list(map(lambda x,y,z : x+y+z ,a,b,c))   )              # Output : [17,10,19,23]
print(list(map(lambda x,y,z : x+y-z ,a,b,c) ))                # Output : [19,18,9,5]

#  filter
number_list = range(-5,5)
less_than_zero=list(filter(lambda x : x < 0,number_list))
print(less_than_zero)

#Output : [-5,-4,-3,-2,-1]


# Reduce
from functools import reduce
product = reduce((lambda x,y :x*y),[1,2,3,4])

#Output : 24
print(product)