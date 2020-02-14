def printMax(x, y):
    '''prints the maximum of two numbers..
    both the numbers should be integers'''
    x = int(x)
    y = int(y)
    if (x > y):
        print(x, "is maximum")
    else:
        print(y, "is maximum")


printMax(4, 5)  # prints the result
print(printMax.__doc__)  # prints doc string.