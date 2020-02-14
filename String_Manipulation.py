order = '1,2013-07-25 00:00:00.0,11598,CLOSED'

print(order)

print(order.split(","))

print(order.split(",")[-1])

print(type(order.split(",")[-1]))

print (10 > 2)

print ('10' > '2')

print(type(int(order.split(",")[0])))

if  int((order.split(",")[0]).isdigit()):
   print("integer")


print(len(order))

print("count : ", order.count("00"))


print("index of ", order.index("00"))

# print(order.index(("000")))    # will throw an erro if sting doesnot found

print("find ", order.find(("000")))


orderstatus  = order.split(",")[3]

print(orderstatus)

print(orderstatus.lower())

print(orderstatus.capitalize())

s = "Hello     "
s1 = "   Hello    "
print (s.strip())


# join

year = 2013
month = 7
date = 25

date_format = "=".join([str(year), str(month).rjust(2, "0"), str(date).rjust(2, "0")])
print(date_format)

orders = '1,2013-07-25 00:00:00.0,11598,CLOSED\n1,2013-07-25 00:00:00.0,11598,CLOSED'
orderlist = orders.split("\n")
print(orderlist)

orderlist = orders.splitlines()

print (orderlist)


