def readData(dataPath):
    dataFile = open(dataPath)
    dataStr = dataFile.read()
    dataList = dataStr.splitlines()
    return dataList


orders = readData("Data.csv")
print(orders [0:10])

orders.pop(0)

print(orders [0:10])

s = set([])

for i in orders:
    print(i.split(",")[0])
    s.add(i.split(",")[0])

print(s)