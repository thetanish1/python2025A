# class Person:
#     fn = None
#     ln = None
#     age = None

#     def displayName(self):
#         print(self.fn+self.ln)

# amol = Person()
# mayuri = Person()
# print(amol.fn)
# print(amol.ln)
# print(amol.age)
# #amol.displayName()
# amol.fn = "amol"
# amol.ln = "rao"
# amol.age = 34

# print(amol.fn)
# print(amol.ln)
# print(amol.age)
# amol.displayName()


class Person:
    # class level attribute 
    country = "india"

    # instance level attribute
    def __init__(self,fn,ln,age):
        self.firstName  = fn 
        self.lastName = ln 
        self.age = age

    def displayName(self):
        print(self.firstName+ self.lastName)

amol = Person("amol","rao",23)
chinmay = Person("chinmay","deshpade",34)
amit = Person("amit","bhure",34)

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.age)
print(chinmay.country)
chinmay.country = "bharat"
print(chinmay.country)

persons = [amol,chinmay,amit]
for person in persons:
    person.displayName()

# program 3

class Person:
    country = "India"
    def __init__(self,fn,ln):
        self.fn = fn 
        self.ln = ln 

    # instance level method
    def displayName(self):
        print(self.fn + self.ln)

    @classmethod
    def changeCountry(cls,cn):
        cls.country = cn

amol  = Person("amol","rao")
amol2 = Person("amol2",'rao3')
print(amol.fn)
print(amol.ln)
print(amol.country)

Person.changeCountry("bharat")
print(amol.country)
print(amol2.country)


