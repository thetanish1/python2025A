# program 1
listA = [11,22,33]
print(listA)
print(type(listA))

# program 2
# list stores duplicate values 
listB = [22,33,44,55,66,55]
print(listB)
print(type(listB))

# program 3
# retrive the value from list 
# does list stores the value by index ?? - yes

#           0         1        2       3
names = ["chinmay","sarika","amruta","ninad"]
print(names[0])
print(names[1])
print(names[2])

# program 4 
city = ["pune","nagpur","sangamner","nagar"]
city[0] = "mumbai"
print(city)

# particular
print("nagpur" in city)
print("Nagpur" in city)

# program 5
# total number of elements in list
#    0  1  2  3  4
f = [11,22,33,44,55]
print(f)
print(len(f))

#           0          1         2         3
country = ["india","pakistan","srilanka","cuba"]
q1 = len(country) - 1 # 3
country[3]

# looping through list 
# for - range()
fruits = ["apple","mango","banana","orange","grapes"]
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])

# for - loop 
for item in fruits:
    print(item)

# while loop
q1 = 0
while(q1 < 5):
    #print(q1)
    print(fruits[q1])
    q1 = q1 + 1
