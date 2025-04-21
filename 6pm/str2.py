
# program 1

# lower() , upper() , title() , capitalize(), swapcase()

str = "mR Chinmay deshpande"

# print(str.lower())
# print(str.upper())
# print(str.title())
# print(str.capitalize())
# print(str.swapcase())

# Check methods  -- boolean value 

# print("chinmay".isalpha())
# print("123".isdigit())
# print("aaa123".isalnum()) # alpha , numbers  or alphanumber - 
# print("a".isspace())
# print("chinmay".islower())
# print("Chinmay".isupper())
# print("I am Learning Js".istitle())
# print("chinmay".startswith("C"))
# print("chinmay".endswith("y"))

# replace join and split methods 

s = "apple-mango-banana-orange" 
e = s.split("-")
print(e)
print(s.split('n'))

listA= ["python","is","fun"]
f = " ".join(listA) # "python-is-fun"
print(f)

info = "i am learning python"
e1  = info.replace("python","javascript")
print(e1)


str2 = "a-b-c"  
e = str2.partition("-") # ["a","-","b-c"]
print(e)
print(str2.rpartition("-")) # ["a-b","-","c"]


# search
# 0  1  2  3  4  5  6
# c  h  i  n  m  a  y  

e = "chinmayainm"
q1 = e.index("h")
print(q1)

q2 = e.count("a")
print(q2)

q3  = e.find("inm")
print(q3)

q4  = e.rfind("inm")
print(q4)


firstName = "chinmay"
lastName = "deshpande"

# I am chinmay deshpande 
print("I am"+" "+firstName+" "+lastName)
print(f"I am {firstName} {lastName}")
print("I am {} {}".format(firstName,lastName))
