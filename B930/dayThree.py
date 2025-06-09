# conditional statements

# program 1

# one and multipleoutcomes
# numT > 0 and numT <= 5   -----> 10 % discount
# numT > 5 and numY <= 10  -----> 20 % discount 
# numT > 10                -----> 30 % discount 

numT = 17
#if condition(boolean):
    # statament

if numT > 0  and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# program 2

numT2 = 17
if numT2 > 0 and numT2 <= 5:
    print('10 % discount')
elif numT2 > 5 and numT2 <= 10:
    print("20 % discount")
elif numT2 > 10:
    print('30 % discount')
else:
    print("incorrecct input")

# program 3

marks = 55
# if (marks > 90):
#     print("Grade A")
# if (marks >= 75):
#     print("Grade B")
# if (marks >= 65):
#     print("Grade C")


if (marks > 90):
    print("Grade A")
elif (marks >= 75):
    print("Grade B")
elif (marks >= 65):
    print("Grade C")
else:
    print("please try again")

# program 5
d = 6
e = 3
if d > e:
    print("d is greater")
else:
    print('e is greater')

# program 6
a1 = 10
a2 = 50
a3 = 200

if a1 > a2 and a1 > a3:
    print("a1 is greater")
elif a2 > a1 and a2 > a3:
    print("a2 is greater")
else:
    print("a3 is greater")


# program 7

g = 7
e = 50
if g > e:
    print("g is greater")
else:
    print("e is greater")

print("g is greater") if g > e else print("e is greater")

# statement1  if conditionIsTrue else statement2
age = 17
e = "can drive" if age >= 18 else "cannot drive"
print(e)


