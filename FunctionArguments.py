#Default arguments

def say(s,times=1):
    print(s*times)

say("Hello")                         #prints only one 'Hello'
say("World",4)                      #prints 'World' 4 times

#Keyword arguments

def func(a,b=5,c=10):
    print('a is ',a,'b is ',b,'and c is ',c)

func(3,7)                           #Output : a is 3 b is 7 and c is 10
func(25,c=24)                       #Output : a is 25 b is 5 and c is 24
func(c=50,a=100)                    #Output : a is 100 b is 5 and c is 50

#Variable-length arguments

def total(initial=5,*numbers,**keywords):
    count=initial
    for num in numbers:
        count+=num
    for key in keywords:
        count+=keywords[key]
    return count
print(total(10,1,2,3,vegetables=50,fruits=100))

#Output : 166

#Keyword-only parameters


def total(initial=5,*numbers,vegetables):
    count=initial
    for num in numbers:
        count+=num
    count+=vegetables
    return count
print(total(10,1,2,3,vegetables=50)) #Output:66
# print(total(10,1,2,3))               #Output: ERROR -> total() needskeyword-only argument vegetables


