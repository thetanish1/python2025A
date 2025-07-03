a = 10
print(a)
print(type(a))

b = 12.5
print(b)
print(type(b))
# 12.5 , 13.5

c = True 
print(c)
print(type(c))

d = 'chinmay'
print(d)
print(type(d))


e = [11,22,33]
print(e)
print(type(e))

f = {
    "fn":"chinmay",
    "ln":"deshpande"
}
print(type(f))
# create retrive update delete is exist ? 'in' loop

h = [11,22,33,44]
h[0] = 111
print(h)

# tuple 
e = 11,
print(e)
print(type(e))

e = (1,2,3)
print(e)
print(type(e))

# tuple stores the value by index 
cities = ("pune","mumbai","bangore","kolkata")
print(cities)
print(cities[0])

# tuple is always fixed length
#cities[0] = "mumbai"

# total number of elements in tuple
print(len(cities))


# program 2
d = (11,22,33,44)
r = max(d)
r2 = min(d)
print(r)
print(r2)


# loop
#               0         1          2         3 
countries = ("india","pakistan",'bangladesh','cuba')

# range()
for x in range(len(countries)):
    print(countries[x])

# for each
for x in countries:
    print(x)

# while
i = 0
while(i < len(countries)):
    print(countries[i])
    i = i + 1

# tuple unpacking 
e = (11,22,33)
a,b,c = e
print(a)
print(b)
print(c)

# a = e[0]
# b = e[1]
# c = e[2]
# print(a)
# print(b)
# print(c)

w = (1,3,4,5)
w = list(w)
w.append(77)
print(w)
w = tuple(w)
print(w)

d = (112,11,11,11,123)
f = d.count(11)
print(f)

r = d.index(123)
print(r)
