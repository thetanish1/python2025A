# abstract class
# abstract class object 
# abc module ABC
# abstract class will normal
# abstract --- abstract implementation


from abc import *
# interface 

class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print("oracle connected....")
    def disconnect(self):
        print("oracle disconnected ..")

class MongoDb(Myclass):
    def connect(self):
        print("mongoDb connected....")
    def disconnect(self):
        print("mongoDb disconnected ..")

class Database:
    str = input("Enter the database name .....") # Oracle
    className = globals()[str] # Oracle
    x = className()
    x.connect()
    x.disconnect()


# Inheritance 
# MRO

class A(object):
    def method(self):
        print("A is called ...")  #3
        super().method()

class B(object):
    def method(self):
        print("B is called ...")  #5
        super().method()

class C(object):
    def method(self):
        print("C is called ...") #6

class X(A,B):
    def method(self):
        print("X is called ..")  #2
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called ..")   #4
        super().method()
        
class P(X,Y,C): 
    def method(self):
        print("P is called")  #1
        super().method()

p = P()
p.method()
# 1 - numpy 
# 2 - pandas
# exceptional handling 
# file handling 
# regular expression
# date and time 
# directors

        











