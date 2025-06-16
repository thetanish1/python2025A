# conditional statments 
# one input and multiple outcomes ----> statement

# music concert 
# numT > 0 and numT <= 5   -----> 1 to 5  ---->  10 %
# numT > 5 and numT <= 10  ----->  5 to 10 ----> 20 %
# numT > 10                ----->   > 10    ---> 30 % 

# conditional

#if condition:
    # statement

# program1 
numT = 17
if numT  > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# program 2
numT2 = -17
if(numT2 > 0 and numT2 <= 5):
    print("10 % discount")
elif(numT2 > 5 and numT2 <= 10):
    print("20 % discount")
elif(numT2 > 15):
    print("30 % discount")
else:
    print("please provide correct input")

# program 3
marks = -66
if(marks > 90):
    print("Grade A")
if (marks >= 75):
    print("Grade B")
if (marks >= 65):
    print("Grade C")

# program 4
if(marks > 90):
    print("Grade A")
elif (marks >= 75):
    print("Grade B")
elif (marks >= 65):
    print("Grade C")
else:
    print("please try again ..")

# program 5

e = 10
f = 5

if e > f:
    print("e is greater")
else:
    print("f is greater")

a1 = 8 
a2 = 40
a3 = 100
if a1 > a2 and a1 > a3:
    print("a1 is greater")
elif a2 > a3 and a2 > a1:
    print("a2 is greater")
else:
    print("a3 is greater")

# program 6
d = 7
e = 5

if d > e:
    print("d is greater")
else:
    print("e is greater")

# statemen1    condition  # statement 2
print("d is greater") if d > e else print("e is greater")