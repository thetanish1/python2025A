
# functions 

# function without parameter and withour return type 
def addA():
    print(9+9)
addA()
addA()
addA()

# function with parameter and without return type 
def addB(x,y):
    print(x+y)
addB(12,3)
addB(12,1)
addB(1,3)

# function with parameter and with return type
def addC(x,y):
    return x + y
g = addC(11,4)
print(g)
print(g + g)

# default parameter 
def addD(x = 1,y = 1):
    print(x+y)
addD()
addD(2,3)

# postional argument 
# x = 10
# y = 5

def addE(x,y):
    print(x-y)
addE(y = 5,x = 10)

# * args
# 1,3,3,4,5,6 ----> (1,3,3,4,5,6)
def addAll(*args):
    print(args)
    return sum(args)
r2 = addAll(1,2,3,4,5,6,7,8,9,6,7,8,4,6,7,8,5,6,7)
print(r2)
# **kwargs
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
}
# {"city":"pune"}

def addCity(**kwargs):
    print(kwargs)
    info.update(kwargs)
    return info

e = addCity(city="pune",language="marath")
print(e)

# lamda function