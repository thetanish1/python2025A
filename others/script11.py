# Create 
# Update 
# Retrive 
# Delete 

a  = 10
print(a)
print(type(a))

b = 20
print(b)
print(type(b))

c = "chinmay"
print(c)
print(type(c))

d = True 
print(d)
print(type(d))

names = ["chinmay","sarika","ram"]
print(names)
print(type(names))

info = {
    'fn':"chinmay",
    'ln':"deshpande"
}
print(info)
print(type(info))

g = 12,3
print(g)
print(type(g))

# set 
numbers = {11,22,33,44,55,66,11}
print(numbers)

#print(numbers[0])
# range() X
numbersB  = {22,33,44,55,66}
for x in numbersB:
    print(x)


# program 2
setB = {"ram","sham","sachin","piyush","niliesh","rahul"}
print("ram" in setB)
print("Ram" in setB)


#program 3
print(len("chinmay"))
print(len([11,22,33]))
print(len({"fn":'chinmay','ln':"deshpande"}))
print(len((11,22,33,44)))
print(len({33,44,55,66}))

setC = {"ram","sham","sachin","piyush","niliesh","rahul"}
print(len(setC))


#program 5 not possible
# setH  = {11,22,33}
# setH[0] = 55

# program 6
# delete the set
# del setC
# print(setC)


# program 7
setA = {11,22,33}
setA.add(44)
print(setA)

setA.clear()
print(setA)

setA = {44,55,66}
# setB = setA 
# setA.clear()
# print(setA)
# print(setB)

setB  = setA.copy()
setB.clear()
print(setB)
print(setA)



