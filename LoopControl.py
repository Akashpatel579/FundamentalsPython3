# Prints out 0,1,2,3,4 using while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only even numbers - 2,4,6,8,10 using for loop and continue
for x in range(10):
    # Check if x is even
    if not x % 2 == 0:
        continue
    print(x)

# Prints out only even numbers - 2,4,6,8,10 using for loop
for x in range(10):
    if x % 2 == 0:
        print(x)

# Printing even and odd numbers using for loop and ternary operator
for x in range(10):
    print(str(x) + " is even number") if (x % 2 == 0) else print(str(x) + " is odd number")

# nested loop----printing prime numbers less than 100
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > (i / j)): print(str(i) + " is prime")
    i = i + 1