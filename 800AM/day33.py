
# syntax error
#1s = 12
# 

# run time error
#print(3/0) 

#logical error

# def salary(sal):
#     return salary * 0.10 


#Exception -Run time error
# The purpose of handling error is to make the program robust

#BaseException

#Exception

#StandError                  # Warning

#ArithmeticError                  Runtime time warning
#AssertionError                    import warning
#SyntaxError
#TypeError
#EOFError
#RuntimeError
#NameError


# program 1

# print("hello")
# numA = int(input("Enter the numberA"))
# numB = int(input("Enter the numberB"))
# print(numA/numB)
# print("Bye")


# try
# except
# finally

# program 2
print("hello")
try:
    numA = input("please enter a number A")
    numB = input("please enter a number B")
    print(int(numA)/int(numB))
    print(numA/numB)
    
except ZeroDivisionError:
    print("number cant be divisible by zero")
except TypeError:
    print("string division not supported in python")
print("bye")










































