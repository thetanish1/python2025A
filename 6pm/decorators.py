
# decorator always return inner function
# inner will perform addtion operatotor to function send as paramer

# def dec(fun):
#     def inner():
#         e = fun()
#         return e + 2
#     return inner
    


# @dec
# def num():
#     return 10

# e = num()
# print(e)

def dec2(fun):
    def inner():
        e = fun()
        return "hello "+e
    return inner


@dec2
def greet():
    return "chinmay"

@dec2
def greet2():
    return "sarka"

e = greet()
e2 = greet2()
print(e)
print(e2)

# program 3

def decorOne(fun):
    def inner():
        val = fun()
        return val + 2
    return inner

def decorTwo(fun):
    def inner():
        val = fun()
        return val * 2
    return inner

@decorOne
@decorTwo
def Cal():
    return 10
e = Cal()
print(e)

# wednesday 10.00pm - sql
# thursday 8:30 am power BI
# wednesday 9:30 pm numpy pandas