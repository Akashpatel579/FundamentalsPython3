# if-statements
var = 10
var1 = 0
if var:
    print("Value of var is " + str(var))
if var1:
    print("Value of var1 is " + str(var1))

# if-else statements
if var1:
    print("Value of var1 is not equal to zero")
else:
    print("Value of var1 is equal to zero")

# Nested-if
if var < 50:
    print("Value of var is less than 50")
    if var == 30:
        print("Which is 30")
    elif var == 10:
        print("Which is 10")
    else:
        print("Which is not either 10 or 20")
elif var > 50:
    print("Value of var is more than 50")
else:
    print("Couldn't find value of var")
