
x = 10 

#         0   1  2
listA  = [11,22,33]
print(type(listA))

# does list stores the value by index
print(listA[1])

#retrive the value from list
#           0         1        2         3       4 
names = ["chinmay","sarika","poorva","sharddha","sham"]
print(names[0])
print(names[2])


# update the list
fruits = ["apple","mango","banana"]
fruits[0] = "papaya"
print(fruits)

# particular element exist on list 
#         0        1         2        3
city  = ["pune","mumbai","banglore","kolkata"]
e = "Mumbai" in city
print(e)

# total length
country = ["india","srilanka","japan","cuba"]
e = len(country)
print(e)

# del country
# print(country)

# numbers 
numA = [11,22,11,6,44,666,77]
print(max(numA))
print(min(numA))

# does list allows to store duplicate values
listB = [11,22,11,22,33]
print(listB)

# loop 

#for range
#           0      1      2      3     4
names2 = ["amol","amit","sham","ram",'sachin']
print(len(names2))
print(len(names2) - 1) # length -1 is last index

for x in range(len(names2)):
    #print(x)
    print(names2[x])

# for loop 
for name in names2:
    print(name)


# while loop
i2 = 0
while(i2 < len(names2)):
    #print(i2)
    print(names2[i2])
    i2 = i2 + 1