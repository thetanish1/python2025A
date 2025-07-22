
names = ["chinmay","poorva","sarika","shraddha","rahul"]
print(names)
capitalNames = []

# 1st way
for name in names:
    capitalNames.append(name.upper())
print(capitalNames)
#[expression:loop:condition]
# 2nd way
e1 = [name.upper() for name in names]
print(e1)

#3rd way
e = map(lambda x:x.upper(),names)
print(list(e))

# filters 

transactions = [33,44,-56,77,88,99,-100,-200,-899,999]
withdrawl = []
deposit =[]


e = filter(lambda x : x > 0,transactions)
deposit = list(e)
print(deposit)

e = filter(lambda x : x < 0,transactions)
withdrawl = list(e)
print(withdrawl)


# ternary operator
# manange for 2 conditions
#[withdrawl.append(x) if x > 0 else deposit.append(x) for x in transactions]

#manage one condition
#          [expression:loop:conditio] 
# deposit = [x for x in transactions if x > 0]
# withdrawl = [x for x in transactions if x < 0]
# print(withdrawl)
# print(deposit)

# for x in transactions:
#     if x > 0:
#         deposit.append(x)
#     else:
#         withdrawl.append(x)

# print(withdrawl)
# print(deposit)


# reduce
sum = [11,22,33]
total = 0

for x in sum:
    total = total + x
    #         0   + 11  -----> 11
    #         11  +  22 -----> 33
    #         33  +  33 -----> 66
print(total)

from functools import reduce
e = reduce(lambda acc,y:acc+y,sum,0)
print(e)

h = [2,3,4]
e = reduce(lambda acc,y:acc*y,h,1) 
print(e)
