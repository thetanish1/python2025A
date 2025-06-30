# x = 10 
# print(x)
# x = 1000
# print(x)

# # Arithmetic operator
# f = 8
# e = 4

# print(f+e)
# print(f-e)
# print(f*e)
# print(f/e)
# print(f%e)

# q1 = 9
# q2 = 3

# print(q1 +q2)
# print(q1 -q2)
# print(q1 *q2)
# print(q1 /q2)
# print(q1 %q2)

# # 1 pair 5 lines 
# # 10 pair  50 lines

# def Calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)
# Calculator(4,2)
# Calculator(10,5)




# Day2 

# function without parameter and without return type 
def addA():
    print(9+9)
addA()
addA()
addA()

# function with paramerter and without return type 
def addB(x,y):
    print(x+y)
addB(12,4)
addB(12,6)
addB(12,1)


# function with parameter and with return type
# 100 show
# 100 given 
# 100 + 100 , 100 - 50 , 100 / 5 , 100 * 0.10
def addC(x,y):
    return x + y
r1 = addC(12,4)
print(r1)
print(r1 + r1)
print(r1 / 4)


# type 

# introvert       extrovert
# calm             loud
# less social      more social
# less outing      more outing 

# Human 
# Propeties - name , age , gender , weight , height 
# Methods - walk() , talk()

# Vehicle
# Properties - color , wheel , type , logo , companyName
# Methods - start() , stop()

#Bank acc
#Properties - accNo , bal , accName , atmCard
#Methods - withdrawl() , deposit()

f = 10 
print(f)
print(type(f))
# 10 , -10 ,0

e = 10.5
print(e)
print(type(e))
# 10.5 , -10.5 , 0.12

g = True
print(g)
print(type(g))
# True False

f = "chinmay"
print(f)
print(type(f))
# "chinmay" , "A", " 4","  ","234324#!@esdfdsf"
# comparison 

# entity < enity ---> boolean ---> True or False
print(2 > 1)
print(2 < 1)
print(2 == 1)
print(2 >= 1)
print(2 <= 1)
print(2 >= 2)
print(2 <= 2)
print(2 != 2)
print(2 != 1)


# logical operator 
# and 

# true   and    true  -----> true
# false  and    true  -----> false
# true   and    false -----> false
# false  and    false -----> false

print(3 == 3 and 2 == 2)
print(3 != 3 and 2 == 2)
print(3 == 3 and 2 != 2)
print(3 != 3 and 2 != 2)

# or 

# true   or   true  -----> true
# false  or    true  -----> true
# true   or    false -----> true
# false  or    false -----> false

print(3 == 3 or 2 == 2)
print(3 != 3 or 2 == 2)
print(3 == 3 or 2 != 2)
print(3 != 3 or 2 != 2)

# not
# not True ----> False
# not False ----> True

print(not 2 == 2)
print(not 1 != 1)

































