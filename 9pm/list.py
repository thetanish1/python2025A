

# list , string , dict , set , tuple
#           0         1        2
#create
#            0        1         2
names  = ["sarika","poorva","mayuri"]
#           -3          -2         -1

# retrive 
e = names[0]
print(e)

#mutable
# names[0] = "kajal"
# print(names)

# # delete
# names.pop(1)
# print(names)

names.remove("sarika")
print(names)


# program 2
fruits = ["apple","mango","banana","orange",'grapes']
print(len(fruits))
print("apple" in fruits)
del fruits[1]
print(fruits)


# program 3
# loop using range()
animals = ["tiger","lion","rabbit","snake"]

# startIndex = 0
# endIndex = not included
# size = 1
for x in range(len(animals)):
    #print(x)
    print(animals[x])

animals = ["tiger","lion","rabbit","snake"]
for x in animals:
    print(x)

#             0       1       2      3
animals = ["tiger","lion","rabbit","snake"]
i1  =  0
while(i1 < len(animals)):
    #print(i1)
    print(animals[i1])
    i1 = i1 + 1

