


# abstract class - no object 
# abstract can have - abstract and non - abstract methods
# abstract class ---> inherited by non- abstract class ---> 
# non abstract methods --  body 

# from abc import ABC,abstractmethod
# # Encapsulation + Abstraction + Polymorphism + inheritance
# class Shape(ABC):
#     #constructor
#     def __init__(self,color):
#         self.color = color
    
#     # abstract 
#     @abstractmethod
#     def area(self):
#         pass
#     # non - abstract method
#     def describe(self):
#         print(self.color)

# class Circle(Shape):
#     def  __init__(self, color,radius):
#         super().__init__(color)
#         self.raduis = radius

#     def area(self):
#         return 3.14 * self.raduis
    

# class Sqaure(Shape):
#     def  __init__(self, color,radius):
#         super().__init__(color)
#         self.raduis = radius

#     def area(self):
#         return self.radius * self.radius
    


# a = Circle("red",3)
# b = Sqaure("blue",4)


# print(a.raduis)
# print(a.color)
# a.describe()
# a.area()

# Program 2
from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def show_amount(self):
        return f"Amount: ${self.amount}"
    

class CreditCard(Payment):
    def pay(self):
        print("using creadit card..")

class DebitCard(Payment):
    def pay(self):
        print("using debit card")

cc = CreditCard(1000)
dd = DebitCard(2000)










