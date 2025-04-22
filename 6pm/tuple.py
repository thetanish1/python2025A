
a = 10 
print(a)
print(type(a))


b = True
print(b)
print(type(b))

c = "chinmay"
print(c)
print(type(c))

d = 10.6
print(d)
print(type(d))


e = [11,22,33,44]
print(e)
print(type(e))


f = {
    "firstName":"chinmay",
    "lastname":"deshpande"
}
print(f)
print(type(f))



# tuple
g = (1,2,3)
print(g)
print(type(g))

g  = 1,
print(type(g))


# does tuple stores the value by index
names = ("chinmay","poorva","sarika")
print(names[0])

# mutable - not
# names[0] = "tanmay"
# names = (11,22,33)
# f = "info"
# f[0] = "e"


# program 4 
fruits = ("apple","mango","grapes")

# for 
for item in fruits:
    print(item)

# for range 
for x in range(len(fruits)):
    print(fruits[x])

# while
i1 = 0
while i1 < len(fruits):
    print(fruits[i1])
    i1 = i1 + 1

# program 5
fruits = ("apple","mango","grapes")
print("apple" in fruits)
t = len(fruits)

# program 6
# unpack
j = (11,22,33,44,55)
j1,j2,j3,j4,j5 = j
# j1 = j[0]
# j2 = j[1]
# j3 = j[2]
# j4 = j[3]
print(j1)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":22
}

for item in info.items():
    k,v =item
    print(k,v)

# program 7

numbers = (11,22,33,44,55,11)
e = numbers.count(11)
print(e)

numbers.index(22)
print(numbers.index(11,3))






