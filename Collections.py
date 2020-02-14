# List, Set, Dictionary, Tuples

# List Operations
list1=['Akash',10,2.5,'Patel']
list2=[123,'AkashPatel']

print(list1) #prints complete list1
print(list2) #prints complete list2
print(list1[2:4]) #prints elements from 3rd till 4th
print(list2 * 2) #prints list2 two times
print(list1[1]+list2[0]) #prints 2nd element of list1 concatenated with 1st element of list2
print(list1+list2)#prints concatenated list of list1 and list2


# Set Operations

# Remove duplicates

# Dictionary operations
dict1 = {}
dict1['one'] = "This is one"
dict1[2]     = "This is two"

dict2 = {'name': 'Akash','val':6734, 'dept': 'sales'}


print (dict1['one'])   # Prints value for 'one' key
print (dict1[2])       # Prints value for 2 key
print (dict2)          # Prints complete dictionary
print (dict2.keys())   # Prints all the keys
print (dict2.values()) # Prints all the values


# Tuples operations

tuple1=('Akash','123','25.68','456')
tuple2=('Clairvoyant','789')

print(tuple1)
print(tuple2)
print(tuple1[1:3])
print(tuple2 * 2)
print(tuple1+tuple2)