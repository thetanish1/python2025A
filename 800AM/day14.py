#set 
setA = {11,22,33,44}
print(setA)
print(type(setA))
# does set stores the value by index ? - No
#print(setA[0])
# total number of elements in set 
setA = {11,22,33,44}
print(len(setA))
# does set stores duplicate values 
setB = {11,33,44,44,55,11}
print(setB)

# loop
# for - range()
# for - each
# while - ?
# list , dict , tuple , string , set 
#  yes    yes     no      no      ?

numbers  = {11,22,33,44,55,66}
print(numbers)
for item in numbers:
    print(item)

# methods 

numA = {11,22,33,44}
numB = {33,44,55}
numC = numA.intersection(numB)
print(numC)
numA.intersection_update(numB)
print(numA)

numE = {11,33,44}
numF = {55,66,11}
# numG = numE.difference(numF)
# numG2 = numF.difference(numE)
# print(numG)
# print(numG2)
# print(numG)
# print(numG2)
numE.difference_update(numF)
print(numE)


# program 2
numE2 = {11,22,33}
numF2 = {33,44,55}
# numG2 = numE2.symmetric_difference(numF2)
# print(numG2)
numE2.symmetric_difference_update(numF2)
print(numE2)


# program3 
setA = {11,22,33}
setB = {44,55,66,33}
e = setA.isdisjoint(setB)
print(e)


setC = {11,22,33}
setD = {44,55,66,11}
setE = setC.union(setD)
print(setE)

setN = {11,22}
setM = {11,22,33}
print(setN.issubset(setM))
print(setM.issuperset(setN))


setN = {11,22}
setN.add(33)
print(setN)



setK = {55,66,77,88,99}
#setK.clear()
# print(len(setK))

# setL = setK
# setK.remove(55)
# print(setK)
# print(setL)


setR  = setK.copy()
setR.remove(55)
print(setR)
print(setK)

setR.pop()
print(setR)


# remove , discard
setJ = {11,22,33,44}

print("hello")
setJ.discard(444)
print("bye")



