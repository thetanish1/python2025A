
# class Mother:
#     def __init__(self,firstName,lastname):
#         self.firstName = firstName
#         self.lastName = lastname

#     def displayMotherName(self):
#         print(self.firstName + self.lastName)

# class Father:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def displayFatherName(self):
#         print(self.firstName + self.lastName)

# class Son(Father,Mother):
#     def __init__(self, firstName, lastName,ssn):
#         super().__init__(firstName, lastName)
#         self.sname = ssn 

#     def displaySname(self):
#         print(self.firstName + self.lastName)



# Method resolution order
# Multiple inheritance with several classes

class A(object):
    def method(self):
        print("A is called") #3
        super().method()

class B(object):
    def method(self):
        print("B is called")
        super().method()

class C(object):
    def method(self):
        print("C is called") 

class X(A,B):
    def method(self):
        print("X is called") 
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called")
        super().method()

class P(X,Y,C):
    def method(self):
        print("p is called") 
        super().method()

p = P()
p.method()














