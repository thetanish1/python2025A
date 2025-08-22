
#Exception

# program ---write ---compile ----- run ------ output

# compile time error 
# run time error 
# logical error

# compile time errors are syntax error

q1 = 10
q2 = 5

print(q1 + q2)

# if q1 > q2
#     print("q1 is greater")
# else:
#     print("q2 is greater")

# program 2
# def add(a,b):
# return a + b
# add(12,3)

# Run time errors 
# program 3

# def divideA(a,b):
#     return a/b

# e1 = divideA(10,0)
# print(e1)

# program 4
# q1 = 100
# q2 = "hello"
# print(q1 + q2)

# program 5
#           0  1  2  3
# numbers =  [11,22,33,44]
# e = numbers[6]
# print(e)


# 30 + 3 ----> 33k
# def CalculateBonusSalary(salary):
#     return salary * 0.10 + salary

# e2 = CalculateBonusSalary(30000)
# print(e2)


# Exception handling -- topic 
#run time errors

print("hello")
try:
    print(10/0)
except:
    print("zero division error")
print("bye")


# An exception is the run time error managed by programmer
