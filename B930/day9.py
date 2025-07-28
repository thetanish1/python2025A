

# int as parameter and int as a return type 

def add(x,y):
    return x + y
q1 = add(12,4)
print(q1)

# float as parameter and float as a return type
def addB(x,y):
    return x + y
q2 = addB(12.5,11.5)
print(q2)

# boolean as parameter and boolean as return type 
def canDriver(age , haveVehicle):
    if age >= 18 and haveVehicle:
        print('can drive')
        return True
    else:
        print("cannot drive")
        return False

q3  = canDriver(17,True)
print(q3)

# str as parameter and str as return 

def greet(word):
    return "hello " + word
e2 = greet("chinmay")
print(e2)

# list as as parameter list as return type 
city = ["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
q5  = addCity(city)
print(q5)

# dict as parameter and dict as return type 

info  = {
    "fn":"chinmay",
    "ln":"deshpande"
}

def addLang(dicInfo):
    dicInfo['lang'] = "marathi"
    return dicInfo
q6 = addLang(info)
print(q6)


# tuple as parameter and tuple as return 

tupleA = (11,22,33)

def tupleAaddE(tupC):
    tupC = list(tupC)
    tupC.append(44)
    tupC = tuple(tupC)
    return tupC
q7 = tupleAaddE(tupleA)
print(q7)

# set as parameter and set as return type

f = {11,22,33}

def addESet(setA):
    setA.add(44)
    return setA

q8 = addESet(f)
print(q8)