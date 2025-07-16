

# lamda arguments : expression
def add(x,y):
    return x + y
e = add(12,3)
print(e)

add = lambda x,y:x+y
e2 = add(12,4)
print(e2)

# program 2
sub = lambda x,y : x-y
e3 = sub(10,5)
print(e3)

square = lambda x : x * x
e4 = square(5)
print(e4)


# program 3
birthYear = [1989,1990,1991,1992]
ages = []
for x in birthYear:
    ag = 2025 - x
    ages.append(ag)
print(ages)

ages  = [2025 - x for x in birthYear]
print(ages)
ages = list(map(lambda x:2025-x,birthYear))
print(ages)


numbers = [11,22,33,44]
e = map(lambda x :x+10,numbers)
print(list(e))


marks = [11,44,55,66,33,44,55]
above40 = []

for x in marks:
    if x > 40:
        above40.append(x)
print(above40)

e2 = [x for x in marks if x > 40]
print(e2)

e3 = filter(lambda x : x > 40,marks)
print(list(e3))