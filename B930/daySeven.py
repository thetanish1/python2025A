


# listA = [11,22,33,44,55]
# print(type(listA))

# print(listA[0])

# listA[0] = 111
# print(listA)

# print(222 in listA)

# listB = [22,33,44,55,22,33,55]
# print(listB)

# print(max(listB))
# print(min(listB))
# print(len(listB))

# del listB

# Gym - 
# action - exercise
# return - health

# program 1
fruits = ["apple","mango","banana","orange","grapes"]
fruits.append("papaya")
print(fruits)

fruits.insert(2,"chikoo")
print(fruits)

# program 2 
# vegetables 

vegetables = ["potato","brinjal","tomato","cucumber"]
vegetables.pop()
vegetables.pop(1)
print(vegetables)
print(vegetables)
vegetables.remove("tomato")
print(vegetables)

# program 3
city = ["pune","mumbai","bangalore","kolkata"]
# print(city)
# city.clear()
# print(city)
city.extend(["nagpur","wardha","nagpur"])
print(city)

city.reverse()
print(city)

f = city.count("nagpur")
print(f)

city.sort()
print(city)

# ['bangalore', 'kolkata', 'mumbai', 'nagpur', 'nagpur', 'pune', 'wardha']
g = city.index("kolkata")
print(g)