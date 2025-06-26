fn = "chinmay"
e1 = fn.upper() # all upperCase
print(e1)

ln = "Deshpande"
print(ln)
e2 = ln.lower() # all lowerCase
print(e2)

info = 'i am learning javascript' # one char every word to uppercase()
e3 = info.title()
print(e3)

fruit = "apple"
e4 = fruit.capitalize() # first character to upperCase()
print(e4)

# checkedMethods  --> boolean 
s1 = "chinmay"
e1 = s1.islower()
print(e1)

s2 = "CHINMAY"
e3 = s2.isupper()
print(e3)

s3 = "I Am Learning Javascript"
e4 = s3.istitle()
print(e4)

s4 = "apple"
e5 = s4.isalpha()
print(e5)

s5 = "123321"
e6 = s5.isdigit()
print(e6)

s6 = "Abc"
s7 = "Abc123"
s8 = "123"
s9 = ' @'

# Or typeof method
print(s6.isalnum())
print(s7.isalnum())
print(s8.isalnum())
print(s9.isalnum())

s10 = "!"
print(s10.isspace())

s11 = "i am learning javascript"
s12 = s11.replace("javascript","python")
print(s12)








