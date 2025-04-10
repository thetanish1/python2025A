# program 1
#          0  1  2  3
numbers = [11,22,33,44]
print(numbers)
print(type(numbers))

# program 2 retrive the value from list 
#            0        1         2        3
names = ["chinmay","sarika","poorva","shraddha"]
#          -4        -3         -2         -1
print(names)
print(names[0])
print(names[3])
e  = len(names)
print(e)
print(names[len(names)-1])
# len -1 is always the last index
print(names[-2])

# program 3
# update the value in list 
fruits = ["apple","banana","grapes"]
print(fruits[0])
fruits[0] = "papaya"
print(fruits)

# program 4
# value present in list 
animals = ["tiger","lion","goat"]
print("tiger" in animals)
print("Tiger" in animals)
print("lion" in animals)

# program 5
cities = ["pune","mumbai","chennai","bangalore"]
print(cities[0])
a = len(cities)
print(a)

for x in range(a):
    #print(x)
    print(cities[x])


#             0       1       2     3
country = ["india","china","cuba","USA"]

for x in range(len(country)):
    #print(x)
    print(country[x])


# loop using for 
for item in country:
    print(item)


# loop using while
#            0        1      2     3
country = ["india","china","cuba","USA"]

i1 = 0

while(i1 < 4):
   # print(i1)
    print(country[i1])
    i1 = i1 + 1