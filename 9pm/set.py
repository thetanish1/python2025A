

# int 

# float

# boolean 

# string 

# list 

# dictionary 

# tuple 

# create , update , retrive , delete , isexist, len , loop 

setA = {11,22,33}
print(setA)
print(type(setA))


# does not stores the value by index 
#print(setA[0])

# program 2
setB = {11,22,33,44}
print(11 in setB)


# program 3
# set allows to store duplicate values
setC = {11,11,23,44,5,44}
print(len(setC))
print(setC)


# program 4
setD = {11,11,23,44,5,44}
print(max(setD))
print(min(setD))

# program 5
# for range()  - X
# for each  - >
# while - X

setE = {11,23,44,55,66}
for e in setE:
    print(e)


# methods in setA


# program 5

setA = {11,22,33}
setB = {22,44,66,33}
setC = setA.intersection(setB)
print(setC)

setA.intersection_update(setB)
print(setA)
print(setB)

#setB.intersection_update(setA)
# print(setA)
# print(setB)

# program 7
setD = {11,22,33}
setE = {11,22,44,55}

setF2 = setE.difference(setD)
print(setF2)

# setF = setD.difference(setE)
# print(setF)


# program 1 


# setA = {11,22,33,44}
# setB = {44,55,66,77,33}
# setB = setA.intersection(setB)
# print(setB)
# setB.intersection_update(setA)
# print(setB)



# program 2

# setR = {11,22,33}
# setQ = {33,44,55}
# # setY = setR.difference(setQ) # {11,22}
# # print(setY)
# setR.difference_update(setQ)
# print(setR)


# program 3

setR = {11,22,33}
setQ = {33,44,55}
# setE = setR.symmetric_difference(setQ)
# print(setE)
setR.symmetric_difference_update(setQ)
print(setR)

# program 4
setR = {11,22,33}
setQ = {33,44,55}
setY = setR.union(setQ)
print(setY)


# program 5
setR = {11,22,33}
setQ = {33,44,55}
e = setR.isdisjoint(setQ)
print(e)

# setI = {11,22}
# setG = {11,22,33,44}
# setG.issuperset(setI)
# setI.issuperset(setG)
# setI.issubset(setG)


setH = {11,33,44}
setH.add(55)
print(setH)

setH.remove(44)
print(setH)

setH.discard(55)
setY = {11,22,33}
print("hello")
setY.discard(66)
print("bye")


setY.clear()
print(setY)

setY = {11,22,33}
setU = setY.copy()
setU.remove(33)
print(setU)
print(setY)









