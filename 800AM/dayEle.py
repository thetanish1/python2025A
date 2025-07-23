

# string ?

# checkMethods 
str = "chinmay"
print(type(str))

q1 = str.startswith('c')
print(q1)
q2 = str.startswith('chi')
print(q2)

str2 = "nagpur"
q3 = str2.endswith('r')
q4 = str2.endswith('ur')
print(q3)
print(q4)

str3 = "CHINMAY"
print(str3.isupper())
print(str3.islower())

str4 = "i am leaning title"
e = str4.istitle()
print(e)

str5 = "e"
e = str5.isspace()
print(e)

# need to discuss
#print("0.5".isnumeric())
#print("123213".isdigit()) #includes different superscripts


print("234324".isdecimal()) # 0  -9
print("ad_3".isidentifier())

print("1".isalnum())
print("1a".isalnum())
print("sssa".isalnum())
print("sssa".isalpha())


str = "I am learning js"
print(str.replace("js","python"))

info = ["chinmaydeshpande","gmail.com"]
e = "@".join(info)
print(e)

info  = "rao "
# print(len(info))

e = info.rstrip()
print(len(e))

info2 = " goa "
e2 = info2.lstrip()
print(len(e2))


info  = " rao "
e3 = info.strip()
print(len(e3))

s = "chinmaya"
print(s.count('a'))
print(s.index("a"))

s.capitalize()