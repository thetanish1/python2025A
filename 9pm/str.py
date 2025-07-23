firstName = "chinmay"
print(firstName)
print(type(firstName))

lastName = 'deshpande'
print(lastName)
print(type(lastName))

info = """
    I am learning js 
    and python is similar to js
"""
print(type(info))

info2 = '''
    I am learning javascript
'''
print(type(info))


# program 2
str2  = 'chandrapur'
print(str2)
print(str2[0])

# update - str are immutable
#str2[0] = "h"

# particular char or substring exist in list
str3 = "pune"
print('p' in str3)
print("pu" in str3)
print("P" in str3)

# total number of charactes in string
str4 = "chandrapur"
e = len(str4)
print(e)

# loops  through string 
str5 = "nagpur"

#  0     1      2    3    4    5
#  n     a      g    p    u    r

# for - range 
for  x in range(len(str5)):
    #print(x)
    print(str5[x])

# for - each 
for char in str2:
    print(char)

# while loop
i3 = 1
while(i3 < len(str5)):
    #print(i3)
    print(str5[i3])
    i3 = i3 + 1


# methods
strA = "pune"
e2 = strA.upper()
print(e2)

strB ="Jaipur"
e2 = strB.lower()
print(e2)

strC = "amruta"
e3 = strC.capitalize()
print(e3)

strD = "i am learning  javascript"
e4 = strD.title()
print(e4)

strE = "I am learning javascript"
e5 = strE.replace('javascript',"python")
print(e5)
















