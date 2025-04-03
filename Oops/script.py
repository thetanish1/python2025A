# class Person:
#     # properties and attributes
#     firstName = None
#     lastName = None 
#     age = None 

#     # methods
#     def talk(self):
#         print("I am talking ")
#     def walk(self):
#         print("I am walking")

# amol = Person()
# print(amol.age)
# print(amol.firstName)
# print(amol.lastName)
# amol.walk()
# amol.talk()
# amol.firstName = "amol"
# amol.lastName = "rao"
# amol.age = 12
# print(amol.age)
# print(amol.firstName)
# print(amol.lastName)
# chinmay = Person()
# print(chinmay.firstName)


# Program 2
# Setting the class attribute at the time object creation

class Person2:
    # constructor
    def __init__(self,fn,ln,age):
        self.firstName = fn 
        self.lastName = ln 
        self.age = age 

    def displayName(self):
        print(self.firstName + self.lastName)
    
amol2 = Person2("amol2","rao2",23)
amol2.displayName()
print(amol2.firstName)
print(amol2.lastName)
print(amol2.age)

chinmay2 = Person2('chinmay','deshpande',34)

class Person4:
    country = "India"
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

amol  = Person4("chinmay","deshpande")
sarika = Person4("sarika","pansare")
print(sarika.firstName)
print(sarika.lastName)
print(sarika.country)
sarika.country ="Bharat"

print(amol.country)
print(sarika.country)