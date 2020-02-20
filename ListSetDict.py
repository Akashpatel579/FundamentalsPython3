#list
ls = []
ls = [1,2,3,4,2,4]
print(ls)

#dict
s = {}
print(type(s))

dict = {1:"Hello", 2:"world"}
print(dict[1])

# set
set = set({})

print(type(set))

# Operations

print(ls.count(2))


print(ls.pop(2))

ls.reverse()
print(ls)


dict_2 = {1:"Hello", 2:"Akash"}
dict.update(dict_2)

print(dict)

print(dict.items())