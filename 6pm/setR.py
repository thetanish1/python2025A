
setA = {11,22,33,44,11}
print(setA)

# add
setA.add(77)
print(setA)

setA.remove(11)
print(setA)

setA.pop()
print(setA)

# setA.clear()
# print(setA)

# program 2

setB = {11,22,33,44}
print(len(setB))

setB.update([55,66,77])
setB.update((33,555,66666,77777))
print(setB)


# program 3

setA = {11,22,33}
setB = {44,55,66}
setC = setA.union(setB)
print(setC)




setA = {11,22,33,44}
setB = {44,55,66,22}
# setD = setA.intersection(setB)
# print(setD)
# print(setA)
# print(setB)
setA.intersection_update(setB)
print(setA)



# program 4

setA = {11,22,33,44}
setB = {44,55,66,22}

print(setA.difference(setB)) # 11,33
print(setB.difference(setA))

print(setA)
print(setB)
setA.difference_update(setB)
print(setA)



setA = {11,22,33,44}
setB = {44,55,66,22}

# print(setA.symmetric_difference(setB))
# print(setA)
# print(setB)

setB.symmetric_difference_update(setA)
# setB 
# setB
print(setB)
setA = {11,22}
setB = {11,22,33}
print(setA.issubset(setB))
print(setB.issuperset(setA))

setA = {44,11}
setB = {11,22,33}
print(setA.isdisjoint(setB))

setA  = {44,55,66}
setB = setA.copy()
setA.remove(55)
print(setA)
print(setB)
# dictionary,list, Set 
setD = {11,22,33}
print("hello")
#setD.remove(444) # execution stopped
setD.discard(555)
print("bye")

