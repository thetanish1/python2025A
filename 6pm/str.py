# fn = "chinmay"
# print(fn)
# print(type(fn))


# ln = 'deshpande'
# print(ln)
# print(type(ln))


# mn = """
# I am learning javascript
# I am learning python
# I am learning data analysis
# """

# print(mn)
# print(type(mn))


# nm = '''
#     I am learning java and concepts 
#     I am learning python and concepts
# '''

# # program 2
# # does string stores value by index ?
# # strings are not mutable 

# city = "pune"
# #print(city[0])
# #print(city[-1])
# # String Immutability 
# #city[0] = "a"

# # program 3
# # same for list and string
# #slicing 

# #           0           1        2        3      4
# names = ["chinmay","shirish","sarika","sachin","ram"]
# #         -5          -4         -3      -2        -1

# #lstName[startIndex:EndIndex(notincluded):stepSize]
# # by default startindex -0
# # by default end index - lastIndex - len-1
# # by default stepsize - 1
# print(names[0:4:2])
# print(names[1::])
# print(names[1:-1:1])
# print(names[:3])
# print(names[-4:3])
# print(names[-1:-3])
# print(names[::-1])
# print(names[0:4:2])


# # slcing with string 


# city  = "chandrapur"

# #  0     1     2     3      4     5    6     7     8     9    
# #  c     h     a     n      d     r    a     p     u     r
# # -10   -9    -8    -7     -6    -5   -4    -3    -2     -1

# # print(city[:9])
# # print(city[3::])
# # print(city[3:7:])
# # print(city[::-1])
# print(city[1:10:2])


# # loops

# name = "chinmay"
# # for 

# for x in  name:
#     print(x)

# # for - range

# for x in range(7):
#     #print(x)
#     print(name[x])

# # while

# i1 = 0
# while(i1 < len(name)):
#     print(name[i1])
#     i1 = i1 + 1


#Methods of string 
fn = "chinmay"
print(fn)
print(type(fn))

e = fn.upper()
print(e)

ln = "Deshpande"
e2 = ln.lower()
print(e2)

nm = "chinmay"
e3 = nm.capitalize()
print(e3)

# checked methods 

city = "pune"
e4 = city.startswith('p')
print(e4)

e5 = city.startswith("P")
print(e5)

e6 = city.endswith("e")
print(e6)

city2 = "nagpur"
e7 = city2.isupper()
print(e7)

e8 = city2.islower()
print(e8)

info = "123a"
e9 = info.isdigit()
print(e9)

info2 = "abc"
e10 = info2.isalpha()
print(e10)

info3 = "123aaaa"
e11 = info3.isalnum()
print(e11)


