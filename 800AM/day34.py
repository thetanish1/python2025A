# # try except else finally
# try:
#     numA = input("please enter a number")
#     numB =input("please enter a numbe12r")
#     print(int(numA)/int(numB))
#     a = [11,22,33]
#     print(a[4])
# except TypeError:
#     print("type error")
# except ZeroDivisionError:
#     print("print zero division error")
# except IndexError:
#     print("exception raised index error")
# except:
#     print("exception raises")
# finally:
#     print("i will alaways execute")


# A single try block can be followed by several except block - true
# mutilple except blocks can be used to handle multiple exceptions -true
# we cannot write except block without try block - true
# we can write  a try block without except block -true
# else and finally blocks are not compulsory - true
# When ther is no exception else block is executed after try block - true
# Finally block is always executed  - true


# try:
#     print(10/5)
# finally:
#     print("i will always except")


# program 3

try:
    numA  = input("enter a number")
    numB = input("enter a number")
    print(int(numA)/int(numB))
except ArithmeticError:
    print("cannot divide by zero")
else:
    print("division occured")
finally:
    print("i will always execute...")

# Type of exception in python - inbuilt exception
# user defined exception
