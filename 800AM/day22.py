
class Person:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def  displayName(self):
        print(self.firstName + self.lastName)

# chinmay = Person("chinmay","deshpande",123)

# incorrect way
# class Teacher:
#     def __init__(self,fn,ln,adharNo,salary):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.adharNo = adharNo
#         self.salary = salary

#     def  displayName(self):
#         print(self.firstName + self.lastName)

#     def displaySalary(self):
#         print(self.salary)

    

# program 2 correct way


class Person:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def  displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Person):
    
    salary  = 1000
    def displaySalary(self):
        print(self.salary)


chinmayT = Teacher("chinmayT","deshpandeT",123)
print(chinmayT.adharNo)
print(chinmayT.lastName)
print(chinmayT.firstName)
print(chinmayT.salary)
chinmayT.displayName()
chinmayT.displaySalary()

#chinmay = Person("chinmay","deshpande","123")