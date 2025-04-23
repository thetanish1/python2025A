s = {11,22}
print(s)

# program 1 
# set allow
# set stores unquie values only
s1 = {"pune","mumbai","pune"}
print(s1)

# program 2
# whether the set stores the value by index 
s2 = {11,22,33,44,55}
#print(s2[0]) set does not stores the value by index

# particular element exist in set
s3 = {22,33,44,55,66,77,22}
print(222 in s3)


# program 3
s4  = {3,4,5,6,7,8,9,0}
for x in s4:
    print(x)

# program 4
# add 
s5 = {666,777,888,999}
s5.add(5555)
print(s5)
# update 
s5.update([577,588,599])
s5.update((577,588,599))
print(s5)

# remove
s5.remove(599)
print(s5)

# pop
s5.pop()
print(s5)

# clear
# s5.clear()
# print(s5)

print(len(s5))
print(type(s5))
del s5
#print(s5)


# program 5

setA  = {11,22,33}
setB = {44,55,66,11}
e1 = setA.union(setB)
print(e1)



setA  = {11,22,33,55}
setB = {44,55,66,11}

# print(setA.intersection(setB))
# print(setA)
# print(setB)
# setA.intersection_update(setB)
# print(setA)

setB.intersection_update(setA)
setA  = {11,22,33,55}
setB = {44,55,66,11}

#print(setA.difference(setB))
# print(setB.difference(setA))

# # print(setB)
# # print(setA)

# # setA.difference_update(setB)
# # print(setA)

setB.difference_update(setA)
print(setB)