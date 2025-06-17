print(1)
print(2)
print(3)
print(4)
print(5)

# 100 lines 
# for  and while 
# for   --- definite
# while --- loop

#range(startIndex , endIndex(not included),stepsize)
#range(5) ---> startIndex = 0 , endIndex - 5 , stepsize = 1
#range(1,6) ---> startIndex = 1 , endIndex = 6 , stepsize = 1
#range(2,20,2) ---> startIndex = 2 , endIndex = 20 , stepsize = 2
# program 1 - print 0 -4
for x in range(5):  # startIndex - 0 , endIndex(not included)-5 ,stepSize - 1
    print(x) #0 ,1 ,2,3,4

# print 1 to 4
for x in range(1,5):
    print(x)

# print 1 to 5
for x in range(1,6,1):
    print(x)

for x in range(3):
    print("hello")
    print("bye")
    print("hello2")

# program 2
# print 5 to 1 
for x in range(5,0,-1):
    print(x)

#program 3
# print 1 to 10
for x in range(1,11):
    print(x)

#program 4
for x in range(1,11):
    print(x * 2)

for x in range(2,21,2):
    print(x)

# program 5
# table 
for x in range(3,31,3):
    print(x)

# program 6
# table of 3 in reverse 
for x in range(30,2,-3):
    print(x)

# program 7
# table of 5 in reverse 
for x in range(50,4,-5):
    print(x)

#program 8
#break statement in for 

for x in range(1,6): #2 #3
    if x == 3:
        break
    print(x) #1 #2

