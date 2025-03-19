# int as and int as return 
def add(a):
    return a + a
e = add(1)
print(e)

# float as param and float as return type 
def addB(b):
    return b + b
e2 = addB(12.3)
print(e2)

# string as a parameter and string as return type 
def greet(word):
    return "hello" + word
e3 = greet("good morning !")
print(e3)

# list a parameter and list as return type 
cities = ["wardha","pune","mumbai"]
def addElementToList(lst):
    lst.append("nagpur")
    return lst
e4 = addElementToList(cities)
print(e4)

# boolean as parameter and boolean as return 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False
e5 = canDrive(18,True)
print(e5)

# dict as parameter and dict as return type

info = {"firstNname":"chinmay","lastName":"deshpande"}
def addCity(dic):
    dic.update({"city":"pune"})
    return dic
e6 = addCity(info)
print(e6)

# tuple as parameter and tuple as return tupe

tupleA = (11,22,33)

def addValueTuple(tupA):
    # (11,22,33)
    tupA = list(tupA)  #[11,22,33]
    print(tupA)
    tupA.append(44) #[11,22,33,44]
    f = tuple(tupA) # (11,22,33,44)
    return f
e7 = addValueTuple(tupleA)
print(e7)

# set as parameter and set as return type 
setA  = {11,22,33}
def addElementToSet(setB):
    setB.add(44)
    return setB

e7 = addElementToSet(setA)
print(e7)

# default parameter 

# optional parameter 

# args 

# **kwargs

# lambda function

# function as parameter and function as written 

# map()

# filter()

# reduce()