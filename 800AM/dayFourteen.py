
# int as a parameter and int as return type 

def addNumber(x,y):
    return x + y

e = addNumber(12,3)
print(e)

# float as a parameter and float as return type 
def  addFloats(x,y):
    return x + y
e2 = addFloats(12.4,12.5)
print(e2)

# str as parameter and string as return 
def greet(word):
    return "hello " + word
e3 = greet("chinmay")
print(e3)

# boolean as parameter and boolean as return 
def canDrive(haveVehicle , age):
    if haveVehicle and age >= 18:
        return True
    else:
        return False
e4 = canDrive(True,18)
print(e4)

# list as parameter and list as return type 
names = ["chinmay","sarika","poorva","sham","raj"]
def addName(lst):
    lst.append("rahul")
    return lst
e5 = addName(names)
print(e5)

# set as parameter and set as return type 
setA = {11,22,33}
def removeE(setNew):
    setNew.remove(22)
    return setNew
e6 = removeE(setA)
print(e6)
# dict as parameter and dict as return type 
info = {
    "fn":"chinmay",
    "ln":"deshpande"
}
def addAge(info):
    info['age'] = 29
    return info
e6  = addAge(info)
print(e6)
# tuple as a parameter and tuple as return type
tup = 11,44,55
def addE(tupNew):
    tupNew = list(tupNew)
    tupNew.append(33)
    tupNew = tuple(tupNew)
    return tupNew
e7 = addE(tup)
print(e7)