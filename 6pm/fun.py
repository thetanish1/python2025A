# variables 
# types
# arithmetic 
# comparison operator 
# logical operators
# functions 
# loops
# list 
# dict
# tuples
# string
# set 
# functions 

# program 1
# def add(x,y):
#     # statement
#     print(x+y)
# add(12,3)


# def add():
#     print(9+9)
# add()
# add()
# add()

# def add2(x,y):
#     return x + y
# e = add2(12,3)
# print(e)
# print(e+e)


# int as a parameter and int as a return 
def add(x,y):
    return x + y
e  = add(12,3)
print(e)
print(type(e))


# float as a parameter and float as a return type
def addB(x,y):
    return x + y
e = addB(12.4,3.7)
print(e)
print(type(e))

# boolean as a parameter and boolean as a return type 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True 
    else:
        return False  
f = canDrive(18,True)
print(f)
print(type(f))


# String as parameter and string as return type 
def greet(word):
    return "good "+ word  
e = greet("morning")
print(e)
print(type(e))


# list as parameter and list a  return type 
names = ["chinmay","sarika","sanjay","ram"]
print(names)

def addElement(lst,name):
    #lst = ["chinmay","sarika","sanjay","ram"]
    #name = monika
    #lst.append(name)
    #lst = ["chinmay","sarika","sanjay","ram","monika"]
    lst.append(name)
    return lst
    
e2 = addElement(names,"monika")
print(e2)
print(type(e2))


# dict as a parameter and dict as return 
info  = {
    "firstName":"chinmay",
    "lastName":"deshpande"
    # "city":"pune"
}

def addCity(dictA):
    dictA['city'] = "pune"
    return dictA
e3 = addCity(info)
print(e3)


# tuple as parameter and and tuple as return type 

tupOne = (11,22,33)
def addE(tupA):
    tupA  = (11,22,33,44,55)
    return  tupA
e4 = addE(tupOne)
print(e4)
print(type(e4))


# set as parameter and set as return type
# removeE
setA = {11,22,3,344,55,66}
def removeE(seta,elementToremove):
    seta.remove(elementToremove)
    return seta
e5 = removeE(setA,55)
print(e5)

# program 1
# default parameter
def add(x=3,y=2):
    print(x+y)

add()
add(12,3)

# postional arguments
# x- 34
# y - 56
def add2(x,y):
    print(x-y)
add2(y=56,x=34)

# program 3
def addAll(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x #12
    print(total)

addAll(12,33,4,5,6,7,8,4,6,7,8,5,6,7,8,4,6,7,8)

# program 4
def showInfoandAddCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    print(kwargs)
showInfoandAddCity(name="chinmay",lastName="deshpande",age=34,rollNo=65)


# program 5 
#lamda function

def add(x,y):
    print(x+y)
add(21,4)

add = lambda x,y:x+y
# x,y - parameter
# x + y - return 
e=add(34,5)
print(e)

square = lambda x : x * x
e2= square(3)
print(e2)


def sqrt():
    return lambda x : x * x
f = sqrt()
e3 = f(3)
print(e3)

# f = lambda x : x * x