

# function with parameter and without return type 
def Cal():
    print(8+8)

# calling the function
Cal()
Cal()
Cal()

# function with parameter and without return type 
def CalA(x,y):
    print(x+y)

CalA(12,3)
CalA(12,13)
CalA(1,13)

# function with parameter and with return type
def CalC(x,y):
    return x + y

e = CalC(13,3)
print(e)
print(e + e)
print(e * 0.10)

# Type 
# Human 
# Properties - name, color , gender 
# Methods   - walk() , talk()

# Vehicle
# Properties - color , regNo, type , logo 
# Methods - start() , stop()

# Bank acc
# Properties - bal , accNo , accName 
# Methods - withdrawl() , deposit()


# int
w = 10
print(w)
print(type(w))
# 10 , -10 ,0

# float
w2 = 10.5
print(w2)
print(type(w2))
# 10.5 , -19.6 ,0.23

# boolean
w3 = True
print(w3)
print(type(w3))
# True False

# string
w4 = 'chinmay'
print(w4)
print(type(w4))
#'A','abc','123'," ","3435","234$@#$#$"


# comparison 
# entity < entity  ------> boolean
# boolean --> true or false

a = 10
b = 5
print(a > b)

# < , > , <= , >= , == ,!=

print(3 > 1) # True
print(3 < 1) # False
print(3 == 1) # False
print(3 != 1) # True
print(1 == 1) # True
print(1 != 1) # False
print(3 >= 2) # True
print(3 <= 2) # False
print(3 >= 3) # True
print(3 <= 3) # True


# logical operator 

#and

#True and True   -----> True
#True and False   -----> False
#False and True   -----> False
#False and False   -----> False
print(2 == 2 and 3 == 3)
print(2 == 2 and 2 == 1)
print(1 !=1 and 3 == 3 )
print(2 ==1 and 1 == 0)

# or 
#True or True   -----> True
#True or False   -----> True
#False or True   -----> True
#False or False   -----> False

print(2 == 2 or 3 == 3)
print(2 == 2 or 2 == 1)
print(1 !=1 or 3 == 3 )
print(2 ==1 or 1 == 0)


# not
# not False ---> True
# not True ----> False
# print(not (2 == 2))
# print(not (2 == 1))