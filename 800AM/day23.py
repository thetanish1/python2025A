
# single  inheritance

# class Student:

#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
    
#     def __init__(self, fn, ln,sl):
#         super().__init__(fn, ln)
#         self.salary = sl

#     def displaySalary(self):
#         print(self.salary)

# chinmayT  = Teacher("chinmay","deshpande",10000)
# print(chinmayT.salary)
# print(chinmayT.lastName)
# print(chinmayT.firstName)
# chinmayT.displayName()
# chinmayT.displaySalary()


# multi-level inheritance
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):

    def __init__(self, fn, ln , ffn):
        super().__init__(fn, ln)
        self.fname = ffn


    def displayFName(self):
        print(self.fname +  self.lastName)

class Son(Father):

    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sanme = ssn
        
    def displaySname(self):
        print(self.sanme +  self.lastName)


chinmay = Son("Manohar","Deshpande","Shirish","Chinmay")

chinmay.displayFName()
chinmay.displayGName()
chinmay.displaySname()





