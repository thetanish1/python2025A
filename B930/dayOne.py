#  python is dynamically typed language
x = 10
print(type(x))

x = "chinmay"
print(type(x))

x = True
print(x)
print(type(x))


# program 2
x = 100
print(x)
x = 1000
print(x)

# Arithmetic
# + , -, * , / , %

a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

s = 8
t = 4

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)


# 100 pairs ----> 500 repetation ---> DRY 

# function 

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(12,6)
Calculator(6,3)


# Day 2
# function without parameter and without return 
def add():
    print(8+7)

add()
add()
add()
add()
add()

# function with parameter and without return type
def addB(x,y):
    print(x+y)
addB(12,4)
addB(12,1)
addB(12,2)
addB(12,3)

# function with parameter and with return type 
# 100 - show 
# 100 - given 
def addC(x,y):
    return x + y
e = addC(13,1)
print(e)
print(e + e)

# Day 3

# introvert     extrovert 
# calm          loud
# less social   more social
# less outing   more outing 

# Human 
# Properties - weight , height , gender 
# Methods - walk() , talk()

#Vehicle 
# Properties - color , type , logo , companyName
# Method - start() , stop()

# Bank acc 
# Properties - bankAccNumber , Name , Bal, IFSC code 
# Methods - withdrawl() , deposit()


x = 10
print(x)
print(type(x))
# 10, -10 ,0

y = 10.5
print(y)
print(type(y))
# 10.5 , -10.6 , 0.45

z = True 
print(z)
print(type(z))