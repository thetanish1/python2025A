# overloading
# class Calculator:

#     # def addition(self,x,y):
#     #     print(x+y)
    
#     # def addition(self,x,y,z):
#     #     print(x+y+z)

#     # # upated
#     # def addition(self,x,y,z,a):
#     #     print(x+y+z+a)

#     def addition(self,a = None,b = None,c=None,d=None):
#         if a != None and b != None and c != None and d != None:
#             print(a+b+c+d)
#         elif a != None and b != None and c != None:
#             print(a+b+c)
#         elif a != None and b != None:
#             print(a+b)


# e = Calculator()

# e.addition(12,4)
# e.addition(12,4,3)
# e.addition(12,4,3,4)


# overriding 

class WorldBank:
    def loan(self):
        print("world bank loan")
    def save(self):
        print('world bank save')

class SBI(WorldBank):

    # override
    def loan(self):
        print("SBI save method")
    def save(self):
        print("SBI loan method")

class PNB(WorldBank):
    pass

sbi = SBI()
pnb = PNB()


sbi.loan()
sbi.save()

# same class , same method name , different signature - overloading 
# different , same method name , same signature , has a relationship - overriding
# duck typing

class Dog:
    # method
    def sound(self):
        print("Bow Bow")
class Human:
    def sound(self):
        print("Hi hello")
class Cat:
    def sound(self):
        print("meow meow")

# function
def callAnimal(obj):
    obj.sound()

a = Dog()
b = Human()
c = Cat()


callAnimal(a)
callAnimal(b)
callAnimal(c)




# operator overloading