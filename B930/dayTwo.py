# comparison operators
# entity < entity ---> boolean ---> True or False
# < , > , <= , >= , == , != 

print(2 > 1)
print(2 < 1)
print(2 == 2)
print(2 != 2)
print(2 >= 1)
print(2 <= 1)
print(2 >= 2)
print(2 <= 2)

# logical operator 
#and

# True    and     True   -------> True
# False   and     True   -------> False
# True    and     False  -------> False
# False   and     False  -------> False

print(2 > 1 and 3 < 4)
print(2 == 1 and 3 == 3)
print(4 == 4 and 5 == 3)
print(5 == 3 and 5 == 6)

#or 

# True  or   True  -----> True
# False or   True  -----> True
# True  or   False  -----> True 
# False or   False -----> False

print(3 == 3 or 2 == 2)
print(2 == 1 or 4 == 4 )
print(2 == 2 or  5 == 5)
print(4 == 3 or 3 == 2)

#not
# not True  --> False
# not False --> True
print(not (3 > 1))
print(not (4 == 2))