# continue statement with for loop
for x in range(1,6): #2 #3 #4 #5
    if x == 3:
        continue
    print(x) # 1 #2 #4 #5

# while loop
# intialization
# while(condition):
    #statements
    #increment/ decrement

i1 = 1
while(i1 <= 3):
    print(i1) # 1 #2 #3
    i1 = i1 + 1 #2 #3 #4

i2 = 1
while(i2 <= 5):
    print(i2) #1 #2 #3 #4 #5
    i2 = i2 + 1 #2 #3 #4 #5 #6

# program 2
# print hello 3 tyms

i3 = 1
while(i3 <= 3):
    print("hello") # "hello" , "hello" , "hello"
    i3 = i3 + 1 #2 #3 #4

# program 3
i4 = 5
while(i4 >= 1):
    print(i4) #5 #4 #3 #2 #1
    i4 = i4 - 1 #4 #3 #2 #1 #0

# program 4
# table of 2 
i5 = 1
while(i5 <= 10):
    print(i5*2)
    i5 = i5 + 1

i6 = 2
while(i6 <= 20):
    print(i6) #2 #4 #6 ---- 20
    i6 = i6 + 2 #4 #6 #8------22

# table of 5 in reverse
i7 = 50
while(i7 >= 5):
    print(i7) # 50 45 ---------------5
    i7 = i7 - 5 # 45 40 ----------0

#program 3
# break statement with while loop
i8 = 1
while(i8 <= 5):
    print(i8)  # 1 #2 #3
    if i8 == 3:
        break
    i8 = i8 + 1  #2 #3

i8 = 1
while(i8 <= 5):  
    if i8 == 3:
        break
    print(i8) #1 #2
    i8 = i8 + 1  #2 #3

# program 4
# continue statement with while loop
i9 = 1
while(i9 <= 5):
    if i9 == 3:
        i9 = i9 + 1 #4
        continue
    print(i9)  #1 #2 #4 #5
    i9 = i9 + 1  #2 #3 #5 #6

