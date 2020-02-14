# Correct way of getting sumOfIntegers
def sumOfIntegers(lb, ub):
    l = lb - 1
    return ((ub * (ub + 1)) / 2) - ((l * (l + 1)) / 2)


print(sumOfIntegers(2, 5))


# To demonstrate lambda functions we will loop through the range
# Conventional approach, we need to write different functions for
# sum of range of numbers
# sum of squares in range of numbers
# and more
def sum(lb, ub):
    total = 0
    for i in range(lb, ub + 1):
        total += i
    return total


print("sum of integers using conventional approach " + str(sum(3, 5)))


def sumOfSquares(lb, ub):
    total = 0
    for i in range(lb, ub + 1):
        total += (i * i)
    return total


print("sum of squares using conventional approach " + str(sumOfSquares(3, 5)))


# With lambda functions, we can get more concise and readable code
def sum(lb, ub, f):
    total = 0
    for i in range(lb, ub + 1):
        total += f(i)
    return total


print("sum of integers using lambda functions " + str(sum(3, 5, lambda i: i)))
print("sum of squares using lambda functions " + str(sum(3, 5, lambda i: i * i)))


# We can also pass named function as argument
def cube(i): return i * i * i


print("sum of cubes using lambda functions " + str(sum(3, 5, lambda i: cube(i))))
