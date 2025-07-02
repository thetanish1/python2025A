
#          0         1       2      3
names = ["sarika",'poorva',"ram","sham"]
print(names)
print(type(names))
# retrive
print(names[0])
# update 
names[1] = "mayuri"
print(names)
print(len(names))
print("mayuri" in names)

nums  = [11,23,77,88,66]
e  = max(nums)
print(e)
f = min(nums)
print(f)
del nums

#           0      1         2        3
cities = ["pune","mumbai","nagpur","wardha"]

for x in range(len(cities)):
    #print(x)
    print(cities[x])

for city in cities:
    print(city)

i1 = 0
while(i1 < len(cities)):
    #print(i1)
    print(cities[i1])
    i1 = i1 + 1

# #methods
# country = ["india","cuba","USA","UK"]
# country.append('china')
# print(country)

# country.insert(1,"srilanka")
# print(country)

# country.pop()
# print(country)

# country.pop(1)
# print(country)

# country.remove("india")
# print(country)

# country.clear()
# print(country)


country = ["india","cuba","USA","UK",'india']
country.sort()
print(country)
country.reverse()

e = country.count('india')
print(e)

#             0       1     2    3    4 
country = ["india","cuba","USA","UK",'india']
e = country.index("cuba")
print(e)

country.extend(["brazil","pakistan"])
print(country)


x = 10
print(x)

y = x
y = 900

print(x)
print(y)

nums = [11,22,33]
# print(nums)
# numsB = nums
# numsB[0] = 111
# print(nums)
# print(numsB)

numC = nums.copy()
numC[1] = 88
print(numC)
print(nums)