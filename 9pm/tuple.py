# x = 10
# print(type(x))

# x = 10,
# print(type(x))

# x = (10,0)
# print(type(x))

# # does tuple the stores value by index

# #            0         1      2       3
# names = ("chinmay","sarika","pooja","ram")
# e = names[0]
# print(e)

# # update 
# # names[0] = "sham"
# # print(names)

# # value exist or not ?
# print("chinmay" in names)
# print("Chinmay" in names)

# numbers = (11,22,33,44)
# print(len(numbers))

# print(max(numbers))
# print(min(numbers))

# del numbers


# program 2 
#          0        1        2       3
cities = ("pune","nagpur","mumbai","wardha")
for x in range(len(cities)):
    #print(x)
    print(cities[x])

for city in cities:
    print(city)

i1 = 0
while(i1 < len(cities)):
    print(i1)
    print(cities[i1])
    i1 = i1  + 1 


m = (11,22,33)
x,y,z = m
print(x)
print(y)
print(z)

# x = m[0]
# y = m[1]
# z = m[2]

# print(x)
# print(y)
# print(z)

animals = ("tiger","snake","dog")
animals = list(animals)  # ["tiger","snake","dog"]
animals.append("rabbit")
animals = tuple(animals)
print(animals)

vegetables = ("onion","tomato","brinjal","onion")
e = vegetables.count("onion")
print(e)

e2 = vegetables.index("tomato")
print(e2)
