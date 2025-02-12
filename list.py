#          0      1     2        3
names  = ["raj","ram","sham","sanket"]
#retrive 
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# program 2
# allows to store duplicate values ?? - yes
#           0  1  2  3  4
numbers  = [11,22,33,44,11]
print(numbers)
# program 3
# mutable ????                    - yes
numbers[1] = 77
print(numbers)

# program 3
# Particular element present in list
fruits  = ["apple","mango","banana","orange"]
print("Apple" in fruits)

#program 4
# How to find number of element
fruits  = ["apple","mango","banana","orange"]
e = len(fruits)
print(e)

#program 5
fruits  = ["apple","mango","banana","orange"]
#del fruits
print(fruits)


# loops 
# list stores the value by index
#          0        1        2           3
cities = ["pune","mumbai","banglore","kolkata"]
# for loop  - range()
print(cities[0])

for x in range(4):
    #print(x)
    print(cities[x])

#            0          1       2       3       4
country = ["india","srilanka","cuba","japan","china"]
for x in range(5):
    #print(x)
    print(country[x])


# while
#            0         1       2        3       4
country = ["india","srilanka","cuba","japan","china"]
i1 = 0
while(i1 < 5):
    print(i1)
    print(country[i1])
    i1 = i1 + 1

# for loop 
vegetables = ["tomato","potato","brinjal","cucumber"]
for item in vegetables:
    print(item)
