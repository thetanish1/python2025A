
#Oops
# inhertiance 

# single inheritance
# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln

#     def displayName(self):
#         print(self.fn + self.lastName)

# class Teacher(Student):
#     def __init__(self, fn, ln ,sl):
#         super().__init__(fn, ln)
#         self.salary = sl
    
#     def displaySalary(self):
#         print(self.salary)

# chinmay = Teacher("chinmay","deshpande",1000)
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.salary)

# chinmay.displayName()
# chinmay.displaySalary()


# multi-level  interitance


# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayGName(self):
#         print(self.firstName + self.lastName)

# class Father(GrandFather):
#     def __init__(self, fn, ln ,ffn):
#         super().__init__(fn, ln)
#         self.fname = ffn

#     def displayFName(self):
#         print(self.fname + self.lastName)

# class Son(Father):
#     def __init__(self, fn, ln, ffn,ssn):
#         super().__init__(fn, ln, ffn)
#         self.sname = ssn
    
#     def displaySName(self):
#         print(self.sname + self.firstName)

# d = Son("manohar","deshpande","shirish","chinmay")
# d.displayFName()
# d.displayGName()
# d.displaySName()

# herarchical inheritance 
# one parent two child
# class Father:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)


# class Son(Father):
#     def __init__(self, fn, ln,ssn):
#         super().__init__(fn, ln)
#         self.sname = ssn 
    
#     def displaySname(self):
#         print(self.sname + self.lastName)

# class Daugter(Father):
#     def __init__(self, fn, ln,ddn):
#         super().__init__(fn, ln)
#         self.dname = ddn

#     def displayDName(self):
#         print(self.dname + self.lastName)


# chinmay = Son("shirish","deshpande","chinmay")
# gauri = Daugter("shirish","deshpande","gauri")

# chinmay.displayName()
# chinmay.displaySname()

# gauri.displayName()
# gauri.displayDName()

# multiple inheritance
class Father():
    def __init__(self,fn,ln):
        print("Father constructor called ....")
        self.firstName = fn 
        self.lastName = ln

    def displayFName(self):
        print(self.firstName)
        print(self.lastName)

class Mother():
    def __init__(self,fn,ln):
        print("Mother constructor called")
        self.firstName = fn 
        self.lastName = ln

    def displayMName(self):
        print(self.firstName)
        print(self.lastName)


class Son(Mother,Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    
    def displaySname(self):
        print(self.firstName + self.sname)

chinmay = Son("shirish","deshpande","chinmay")