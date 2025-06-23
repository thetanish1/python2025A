# methods 
#           0          1      2         3       4
names  = ["chinmay","sarika","poorva","amit","chinmay"]
names.append("raj")
print(names)

e = names.index("sarika")
print(e)

e2 = names.count("chinmay")
print(e2)

# program 2
#          0         1       2        3
fruits = ["apple","mango","banana","grapes"]
fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.insert(1,"grapes")
print(fruits)

fruits.extend(["papaya","grapes","coconut"])
print(fruits)

# fruits.clear()
# print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

x = 10
print(x)

y = x
y = 900
print(y)
print(x)

numbersA = [11,22,33]
# numbersB = numbersA
# numbersA[0] = 111
# print(numbersA)
# print(numbersB)
numberC = numbersA.copy()
numberC[0] = 111
print(numberC)
print(numbersA)

city = ["pune","mumbai","banglore"]
print(type(city))


city[0] = "poona"
print(city)

print("mumbai" in city) 

e = len(city)
print(e)

#del city

numbers  = [11,22,33]
e = max(numbers)
print(e)

f  = min(numbers)
print(f)

names = ["ram","sham","sachin"]

for x in range(len(names)):
    #print(x)
    print(names[x])

for item in names:
    print(item)

i1 = 0
while(i1 < len(names)):
    #print(i1)
    print(names[i1])
    i1 = i1 + 1

# slicing