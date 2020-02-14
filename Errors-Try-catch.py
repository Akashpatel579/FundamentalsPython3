# Exception handaling
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
    print("program ended")



# raise exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



