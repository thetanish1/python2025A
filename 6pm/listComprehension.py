
# program 1
birthYear = [2000,2001,2002,2003]
ages  = []
for x in birthYear:
    ag = 2025 - x
    ages.append(ag)
print(ages)


# program 2
marks = [89,90,91,92,75,78]
above70 = []  #[91,92]
for x in marks:
    if x > 90:
        above70.append(x)
print(above70)

# program 3
listA = [11,22,33]
total = 0
for x in listA:
    total = total + x
print(total)

# list comprehension --- list 
# [expression:loop:conditio]

# program 4
listA = [1,2,3,4,5,6,7,8,9,10]
e = [x * 2 for x in listA]
print(e)

marks = [89,55,66,77,33,44]
e2 = [x for x in marks if x > 70]
print(e2)


birthYear = [2000,2001,2002,2003]
e3 =[2025 - x for x in birthYear]
print(e3)

# program 5
h = [33,44,55,22,33]
e4 = [x for x in h if x % 2 == 0]
print(e4)

names = ["sarika","chinmay","rakesh","suresh"]
e5  = [x.upper() for x in names]
print(e5)


names = ["sarika","chinmay","rakesh","suresh"]
#["s","c","r","s"]
e6 = [x[0] for x in names]
print(e6)

evenOdd = [11,22,44,55]
#["odd","even","even","odd"]
# if two conditions 
#[tenary(expression) loop]
e = ["even" if x %2 == 0 else "odd" for x in evenOdd ]
print(e)

