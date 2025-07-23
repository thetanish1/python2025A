
years = [2000,2001,2002,2003]
#[25,24,23,22]
birthYear = []
for x in years:
    age = 2025 -  x
    birthYear.append(age)
print(birthYear)


# filter 
marks = [45,34,66,77,40]
above40 = []
for x in marks:
    if x > 40:
        above40.append(x)
print(above40)

# sum of all elements of array
numbers = [11,22,33]
total = 0
for x in numbers:
    total = total  + x
    #        0     + 11 ---> 11
    #        11    + 22 ---> 33
    #         33   + 33 ---> 66
print(total)

fruits  = ["apple","mango","banana","orange"]
for x in fruits:
    print(f'i like {x}')

# list comprehension [list]
years = [2000,2001,2002,2003]
#[expression:loop:condition]
birthyears = [2025 - x for x in years]
print(birthYear)

numbers = [1,2,3,4,5,6,7,8,9,10]
tableOfTwo = [x * 2 for x in numbers]
print(tableOfTwo)

marks = [45,34,66,77,40]
above40 = [x for x in marks if x > 40]
print(above40)

even  = [11,22,33,44,33,44,55]
e = [x for x in even if x % 2 == 0]
o = [x for x in even if x % 2 != 0]
print(e)
print(o)


evenOdd = [11,22,44,23]
#["odd","even","even","odd"]
f = ["even" for x in evenOdd if x % 2 == 0]
print(f)
#           ternary                   loop
f = ["even" if x % 2 == 0 else "odd" for x in evenOdd]
print(f) 


fruits  = ["apple","mango","banana","orange"]
e = [f'i like {x}' for x in fruits]
print(e)
for x in e:
    print(x)


w =[1,2,3,4,5]
e = [x * x for x in w]
print(e)

# 12 pm ist -- dipanshu
# 7:30 am js , 8:00 am python 
# 8:30 pm js , 9:30 pm python
# 8:30 am ist  excel