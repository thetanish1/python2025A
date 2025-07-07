# names = ["chinmay","deshpande",23,45]
# print(names)
# print(len(names))
# print(type(names))

# d = 12
# print(type(d))

# e = 12.4
# print(e)
# print(type(e))

# g = True
# print(type(g))

# h = {
#     "fn":"chinmay",
#     "ln":"deshpande"
# }
# print(type(h))

# g = (12,3,4)
# print(type(g))

# d = "chinmay"
# print(type(d))


# SET

# CRUD 
# Create 
# Retrive 
# Update 
# Delete 

# Element exist 
# Duplicate 
# Index 
# loops 

h = {11,22,33,44}
print(h)
print(type(h))

# does set stores the value by index? - No 
# does set stores duplicate value - No
h = {11,22,33,44,11} 
print(h)
print(type(h))
#print(h[0])

# particular value exist in set 
print(22 in h)
print(33 in h)

# loop 
# range() ----> index  X
# while() ----> index X

# for 
setA = {11,22,33,44,55}
for item in setA:
    print(item)

setA.clear()
print(setA)
e = len(setA)
print(e)


setA = {11,22,33}
setB = {44,55,11}
setC = setA
setC.remove(33)
print(setC)
print(setA)

setD = setA.copy()
setD.remove(11)
print(setA)
print(setD)


setR = {11,22,33}
setE = {22,33,44}

# e1 = setR.intersection(setE)
# print(e1)

# setR.intersection_update(setE)
# print(setR)
# print(setE)

setE.intersection_update(setR)
print(setE)
print(setR)


setR1 = {11,22,33,99}
setR2 = {44,55,66,22,11}

print(setR1.difference(setR2))
print(setR2.difference(setR1))

# setR1.difference_update(setR2)
# print(setR1)

setR2.difference_update(setR1)
print(setR2)


setN2 = {22,33,44}
setM2  = {22,33,55}

# print(setN2.symmetric_difference(setM2))
# print(setM2.symmetric_difference(setN2))


setN2.symmetric_difference_update(setM2)
print(setN2)