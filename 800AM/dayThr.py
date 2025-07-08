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
