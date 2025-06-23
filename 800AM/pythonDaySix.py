
# methods
x = 100
print(x)
y = x
print(x)
y = 900

print(x)
print(y)


lstA  = [11,22,33]
print(lstA)
lstB = lstA
lstB[0] = 999

print(lstA)
print(lstB)


# copy 

listC = [22,33,44]
listD = listC.copy()

print(listC)
print(listD)

listD[0]= 777
print(listD)
print(listC)


# program 2
# dict

# list
#         fn          ln      rn  age
info = ["chinmay","deshpande",33,45]
print(info)


# dictionary
info = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":33,
    "rollNo":45
}
print(info)
print(type(info))

# does dict stores the value by index ? - No
#print(info[0])

# does dictionary allows to store duplicate values
vehicle = {
    "color":"red",
    "type":"sedane",
    "color":"green"
}
print(vehicle)
# total number of key and values 
info2 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":33,
    "rollNo":45
}
print(info2)
e  = len(info2)
print(e)

# particular key exist in dictionary ?
info3 = {
    "fn":"chinmay",
    "ln":"deshpande",
    "age":33,
    "rollNo":45
}
print("Fn" in info3)
# retrive
print(info3['ln'])

# update
info3['ln'] = "dani"
print(info3)