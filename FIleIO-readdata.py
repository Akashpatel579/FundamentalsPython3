ordersPath = "Data.csv"
ordersFile = open(ordersPath)
ordersData = ordersFile.read()
orders = ordersData.splitlines()
orders = orders[1:10]
for i in orders[:10]:
    print(i)

print(type(orders))


# Get all sports ranking across the years (loop through list, get year 2008 data and add it to the set)
ordersPath = "Data.csv"
ordersFile = open(ordersPath)
ordersData = ordersFile.read()
orders = ordersData.splitlines()
#set can be initialized by saying set([]) or set({})
orderStatuses = set([])
for order in orders:
  orderStatuses.add(order.split(",")[3])

for i in orderStatuses:
  print(i)

# sort is avalilable only for the list  - the changes will be apply to the actual data (variable)
# sorted()  return new list -- can apply to iterables

ordersPath = "Data.csv"
orderFile = open(ordersPath)
orderData = orderFile.read()
dataList = orderData.splitlines()

print(dataList[1:10])

dataList.sort(key = lambda k: k.split(",")[0])

print(dataList[1:10])

print(sorted(dataList, key = lambda k: k.split(",")[0])[1:10])

# descending sorting  
print(sorted(dataList, key = lambda k: k.split(",")[0], reverse = True)[1:10])

