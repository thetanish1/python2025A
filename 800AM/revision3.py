#          0          1      2     3
names = ["sarika","poorva","ram","ram"]
print(names)
print(names[0])

# list stores duplicate value ??yes
# update
names[0] = "prachi"
print(names)
# particular value exist in list
print("sarika" in names)
print("prachi" in names)
# total number of elements 
print(len(names))

# program 2
numbers = [11,22,33,55]
print(max(numbers))
print(min(numbers))
del numbers

# program 3
#            0        1        2        3
fruits  = ["apple","mango","banana","chikoo"]
print(len(fruits))

# start index - 0 , endIndex - 4 , stepSize - 1
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])

for x in fruits:
    print(x)

i1 = 0
while(i1 < len(fruits)):
    #print(i1)
    print(fruits[i1])
    i1 = i1 + 1

# program 4

names = ["sarika","poorva","chinmay"]
names.append("shraddha")
print(names)

names.insert(2,"amit")
print(names)

names.pop() # lastIndex
names.pop(3) # 3rd index
print(names)
names.remove("poorva")
print(names)

numbers = [11,22,11,22,33,11]
e = numbers.count(11)
print(e)

# numbers.clear()
# print(numbers)

numberA = [11,22,33]
numberB = [44,55,66]
numberA.extend(numberB)
print(numberA)

numberB = [44,55,66]
e  = numberB.index(55)
print(e)

numberB.reverse()
print(numberB)

numberB.sort()
print(numberB)

x = 10
y = x
y = 77
print(y)
print(x)

nums = [11,22,33]
# numsB = nums
# numsB[0] = 111

# print(nums)
# print(numsB)


numC = nums.copy()
numC[0] = 555

print(numC)
print(nums)