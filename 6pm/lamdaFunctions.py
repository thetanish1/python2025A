
birthYear = [2000,2001,2002,2003]

# for loop
ages = []
for x in birthYear:
    ag = 2025 - x
    ages.append(ag)
print(ages)

# listcomprehesion 
e1 =[2025 - x for x  in birthYear]
print(e1)

# map function
e2 = list(map(lambda x:2025-x,birthYear))
print(e2)

numbers = [11,22,33]
#[21,32,43]
e3 = list(map(lambda x : x+10,numbers))
print(e3)


# program 2
marks = [44,55,66,33,44,55,66]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

e4 = [x for x in marks if x > 50]
print(e4)

e5 = list(filter(lambda x : x > 50 ,marks))
print(e5)

transactions = [100,-45,40,66,-55]
# [-45,-55]
# [100,40,66]
e6 = list(filter(lambda x:x > 0,transactions))
print(e6)

e7 = list(filter(lambda x:x < 0,transactions))
print(e7)

deposits = [x for x in transactions if x > 0]
withdrawl = [x for x in transactions if x < 0]

print(deposits)
print(withdrawl)

deposit= []
withdrawl = []
print([deposit.append(x) if x > 0 else withdrawl.append(x) for x in transactions])
print(deposit)
print(withdrawl)

j = [11,22,33]
x = j.append(44)
print(j)
print(x)

# program 3

sum = [11,22,33]
total = 0
for x in sum:
    total = total + x
print(total)

from functools import reduce
e = reduce(lambda total,y:total+y,sum,0) # 66
print(e)