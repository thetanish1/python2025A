# 5 pm 
# str tuple set

fn = "chinmay"
print(fn)
print(type(fn))

ln = 'deshpande'
print(ln)
print(type(ln))

middleName = '''
    This is javascript
'''
middleName2 = """
    This is javascript
"""
print(type(middleName))
print(type(middleName))

# does string stores the value by index ?
fn = "chinmay"
print(fn[0])

# is string mutable ?
#fn[0] = "t"
print(fn)

# how to find substring inside string 
fruits = "apple  mango banana orange grapes"
print('Apple ' in fruits)

# loops
# for Each
fruits = "apple"
for x in fruits:
    print(x)

# range - 
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])

i1 = 0
while(i1 < len(fruits)):
    #print(i1)
    print(fruits[i1])
    i1 = i1 + 1

# total number of char in string 
city  = "pune"
print(len(city))

# define
# update 
# add
# retrive 
# loop 
# len

# methods - dictionatory

str = "apple"
print(str)
s1 = str.upper()
print(s1)

str2 = "Apple"
s2 = str2.lower()
print(s2)

str3 = "ram"
s3 = str3.capitalize()
print(s3)

str4 = "i am learning javascript"
s4 = str.title()
print(s4)

# checked methods ---> boolean
str5 = "amit"
s5 = str5.isalpha()
print(s5)

str5 = "123"
s6 = str5.isdigit()
print(s6)

# isnumeric(), isDecimal()

str7 = "A123"
s7 = str7.isalnum()
print(s7)
str8 = "123"
s8 = str8.isalnum()
print(s8)

str9 = "ABC"
s9 = str9.isalnum()
print(s9)

str10 = "abc"
s10 = str10.islower()
print(s10)

str11 = "ABC"
s11 = str11.isupper()
print(s11)

str12 = " 1"
s12  = str12.isspace()
print(s12)

str13 = " goa "
s13 = len(str13)
print(s13)

s14 = str13.lstrip()
print(len(s14))

str15 = "goa "
print(len(str15))
s16 = str15.rstrip()
print(len(s16))

str16 = " goa "
s17 = str16.strip()
print(s17)
print(len(s17))


city = "nagpur"
e = city.startswith("n")
print(e)

f = city.startswith("nag")
print(f)

s = city.startswith("N")
print(s)

city  = "rampur"
d = city.endswith("r")
print(d)

f = city.endswith("ur")
print(f)

fe = city.endswith("Ur")
print(fe)


# 0 1 2 3 4 5 6 7 8 9
e = "123"
e.isdecimal()

f = "2".isdigit()
# subscript and superscript both will be true 
print(f)

# g = "1/2".isnumeric()
# print(g)

# variable cannot start with one 
#1ty = chinmay
r = "ty_1".isidentifier()
print(r)

info = "I am learning javascript"
e = info.replace("javascript","python")
print(e)

# tuple
# 5 pm ---> SET
f = [11,22,33]
print(type(f))

f = 1
print(type(f))

f = 12.4
print(type(f))

f = True
print(type(f))

g = "123"
print(type(g))

h = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(h)

# create , retrive , index , del , update , add , isExist and methods

# tuple is fixed length 

# define 
d = 1,
print(type(d))

d = (1,3)
print(d)
print(type(d))

# does tuple stores the value by index ??
print(d[0])

# mutable  - No 
# d[0] = 11
# print(d)

names = ("chinmay","ram","sham","satish","sachin","ramesh")
e = len(names)
print(e)
print("chinmay" in names)

# range()
for x in range(len(names)):
    #print(x)
    print(names[x])

# for Each 
for item in names:
    print(item)

# while 
i1  = 0 
while(i1 < len(names)):
    #print(i1)
    print(names[i1])
    i1 = i1 + 1


# unpacking 
n = (11,22,33)

# x1 = n[0]
# x2 = n[1]
# x3 = n[2]
# print(x1,x2,x3)

x1 ,x2 ,x3 = n 
print(x1)
print(x2)
print(x3)

city = ("pune","mumbai","goa")
city = list(city)
print(city)
city.append("jaipur")
print(city)
city = tuple(city)
print(city)


#Methods
fruits = ("apple","mango","banana","apple")
print(fruits)
e1 = fruits.count("apple")
print(e1)
e = fruits.index("banana")
print(e)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23
}

for key,value in info.items():
    print(key,value)
