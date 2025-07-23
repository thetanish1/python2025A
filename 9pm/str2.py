
# str methods 
strOne = "chinmay"
e1 = strOne.upper()
print(e1)

str2 = "Ram"
e2 = str2.lower()
print(e2)

str3 = "chinmay"
e3 = str3.capitalize()
print(e3)

str4 = "i am learning javascript"
e4 = str4.title()
print(e4)


str5 = "i am learning javascript"
e5 = str5.replace('javascript',"python")
print(e5)

# checked methods -- o/p boolean

str6 = "pune"
e6 = str6.startswith('p')
print(e6)
print(str6.startswith("pu"))
print(str6.startswith("Pu"))

print(str6.endswith("e"))
print(str6.endswith("ne"))
print(str6.endswith("Ne"))


str7 = "12334"
# 1234567890
e8 = str7.isdecimal()
print(e8)

# isDigit() , subscript superscript digits

str8 = "4324234"
e9  = str8.isdigit()
print(e9)

# fraction
e10 = str8.isnumeric()
print(e10)
#1/2

e10  = "anc".isalpha()
print(e10)

e11 = "aaa32123423".isalnum()
print(e11)

e12 = " ".isspace()
print(e12)


# formatting methods 
firstName = "chinmay"
lastName = "deshpande"

# my firstName is chinmay and lastName is deshpande
print(f"my firstName is {firstName} and my lastName is {lastName}")
e12 = "my firstname is {} and lastName is {}".format(firstName,lastName)
print(e12)

e3 = " goa "
print(len(e3))

e4 = e3.strip()
print(len(e4))

e3 = " goa "
e4 = e3.rstrip()
print(len(e4))

e3 = " goa"
e4 = e3.lstrip()
print(len(e4))

# 18 minuntes  ---> 365 days ----> 90 % 