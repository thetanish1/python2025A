# for while 

# for --- definite number of tyms 
# while loop - until certain condition is meet

# print 1 to 5
print(1)
print(2)
print(3)
print(4)
print(5)

# for loop in python 
#range(startIndex,endIndex(not included),stepsize)
# range(5)  startIndex - 0 , endIndex = 5 , stepsize  = 1
# range(1,5) startIndex - 1 , endIndex = 5 , stepsize = 1
# range(1,10,2) startIndex - 1 , endIndex - 10 , stepsize = 2

# program 1
# startIndex - 0
# endIndex - 5 
# stepSize - 1
for x in range(5):
    print(x)


# program 2
# print 1 to 5
for x in range(1 ,6):
    print(x)

#program  3
# print hello 3 times 
for x in range(3):
    print("hello")

# program 4
for x in range(1,11):
    print(x)

# program 5
# table of 2 
for x in range(1,11):
    print(x * 2)

# program 6
# table 
# 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
for x in range(2,21,2):
    print(x)

for x in range(3,31,3):
    print(x)

# program 7
# print 5 to 1 in reverse 
for x in range(5,1,-1):
    print(x)

# table of 3 in reverse
for x in range(30,2,-3):
    print(x)

# program 8
# break statement in for loop

for x in range(1,6): #2 #3
    if x == 3:
        break
    print(x) # 1 # 2

for x in range(1,6): #2 #3
    print(x) # 1 # 2 #3
    if x == 3:
        break

for x in range(10,5,-1):# 9 #8 #7
    if x == 7:
        break
    print(x)# 10 # 9 # 8