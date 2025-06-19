x = 10 
print(x)

# int list
listA  = [11,22,33]
print(listA)
print(type(listA))

# str list 
names = ["chinmay","ninad","mayur","ram","sham"]
print(names)

#program 3
# does the list stores the value by index
#         0       1        2
city = ["pune","mumbai","bangalore"]
print(city[0])
print(city[1]) 
print(city[2]) 

#program 4
# update a particular value in list
#           0       1        2       3
fruits = ["apple","mango","banana","grapes"]
fruits[2] = "papaya"
print(fruits)

#program 5
#particular element exist in list - in operator
animals = ["tiger","lion","snake"]
print("Lion" in animals)

#program 6
# total number of elements in list
numbers = [11,22,33,44,55,66,77,88,99]
print(len(numbers))

maxValue = max(numbers)
print(maxValue)

minValue  = min(numbers)
print(minValue)

del numbers

# loops
#          0          1       2         3         4
names = ["chinmay","sarika","poorva","shraddha","rohit"]
print(len(names))
# len - 1 is always index
# for - range()
for x in range(len(names)):
    #print(x) # index
    print(names[x]) # element

# for - each 

for item in names:
    print(item)

# while
#           0   1   2   3
numbers = [111,222,333,444]
i1 = 0
while(i1 < len(numbers)):
    #print(i1)
    print(numbers[i1])
    i1 = i1 + 1

# methods

