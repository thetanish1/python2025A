# 

#for x in range(startIndex , endIndex , stepSize):
    # statement

# startIndex - 0 
# endIndex - 5 (not inclued)
# stepSize - 1

# for x in range(5):
#     print(x)

# # print hello 3 times 
# for x in range(3):
#     print("hello")


# # print  1 to  5
# for x in range(1,6):
#     print(x)


# # print 1 to 10 
# for x in range(1,11):
#     print(x)

# for x in range(1,11):
#     print(x * 2)

# for x in range(2,21,2):
#     print(x)

# # print 5 to 1 
# for x in range(5,0,-1):
#     print(x)

# for x in range(50,4,-5):
#     print(x)

# # break statement with for 

# for x in range(1,6): #2 #3
#     if x == 3:
#         break
#     print(x) # 1 #2


# for x in range(1,6): #2 #3
#     print(x)  # 1 #2 #3
#     if x == 3:
#         break

# for x in range(5,0,-1): # 4 #3
#     if x == 3:
#         break
#     print(x)  # 5 #4


# # for with continue
# for x in range(1,6): #2 #3 #4 #5
#     if x == 3:
#         continue
#     print(x) # 1 # 2 #4 #5


# intialization 
# while(condition):
    # statement 
    # increment / decrement


i1 = 1
while(i1 <= 3):
    print(i1) #1 #2 #3
    i1 = i1 + 1 #2 #3 #4


# print hello 3 times 

i2 = 1
while(i2 <= 3):
    print('hello') # "hello" #"hello" #"hello"
    i2 = i2 + 1 # 2 #3 #4

# print 5 to 1
i3 = 5
while(i3 >= 1):
    print(i3) # 5 #4 #3 #2 # 1
    i3 = i3 - 1 #4 #3 #2 #1 #0

# print table of 2
i4 = 2
while(i4 <= 20):
    print(i4) #2 # 4 # 6 ----------20
    i4 = i4 + 2 # 4 #6 # 8 -------> 22

i5 = 3
while(i5 <= 30):
    print(i5)
    i5 = i5 + 3

# table of 5 in reverse 
i6 = 50
while(i6 >= 5):
    print(i6)
    i6 = i6 - 5

# break statement with while loop

i7 = 1
while(i7 <= 5):
    if i7 == 3:
        break
    print(i7) # 1 # 2
    i7 = i7 + 1 #2 #3


i7 = 1
while(i7 <= 5):
    print(i7) 
    if i7 == 3:
        break
    i7 = i7 + 1 