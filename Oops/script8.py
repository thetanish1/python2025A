# abstraction 
# interface 
# import math
# class MyClass:
#     def Calulate(self,x):
#         print(x * x)
    
#     def Calculate_cube(self,x):
#         print(x * x * x)

#     def Calculate_sqrt(self,x):
#         print(math.sqrt(x))

# a = MyClass()
# a.Calulate(2)
# a.Calulate(4)
# a.Calulate(5)


from abc import ABC,abstractmethod
import math

# this is abstract class because it contains abstract method
# we cannot create object of abstract class 
# the class which inherits abstract class has to give method implementation

# class Myclass(ABC):
#     @abstractmethod
#     def Calculate(self,x):
#         pass
# class SubOne(Myclass):
#     def Calculate(self,x):
#         print(x * x)
#     def Info(self):
#         print("square")


# class SubTwo(Myclass):
#     def Calculate(self,x):
#         print(x * x * x)
#     def Info(self):
#         print("cube")


# class SubThree(Myclass):
#     def Calculate(self,x):
#         print(math.sqrt(x))
#     def Info(self):
#         print("sqaure root")

# #a  = Myclass()

# a1 = SubOne()
# a2 = SubTwo()
# a3 =  SubThree()

# a1.Calculate(1)
# a2.Calculate(3)
# a3.Calculate(16)



class Car(ABC):
    def fuel(self):
        print("fuel inserted")

    def regNo(self):
        print("registered")

    @abstractmethod
    def brake(self):
        pass

class Audi(Car):
    def brake(self):
        print("automatic")

    def companyLogo(self):
        print('round')

class Maruti(Car):
    def brake(self):
        print("Manual")

    def companyLogo(self):
        print('traingle')

audiA  = Audi()
marutiB  = Maruti()




