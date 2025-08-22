# Abstraction 
from abc import ABC , abstractmethod

class MyClass(ABC):
    @abstractmethod
    def Calculate(self,x):
        pass


class subClassOne(MyClass):
    # override
    def Calculate(self,x):
        return x * x * x
    def One(self):
        print("One is called ....")

class subClassTwo(MyClass):
    
    def Calculate(self,x):
        return x * x 
    
    def Two(self):
        print("Two class defined")


f = subClassTwo()
f.Calculate()
f.Two()


# e = subClassOne()
# e.Calculate(12)
# e.One()





# we can create object of abstract method
# obj1  =  MyClass()