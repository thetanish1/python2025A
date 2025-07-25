

# instance varibale 
# instance method

# class method 
# class varibale

class Person:

    def __init__(self,fn,ln):
        # instance properties
        self.firstName = fn 
        self.lastName = ln
    
    # instance methods
    def displayName(self):
        print(self.firstName + self.lastName)

amol = Person("amol","rao")
chinmay = Person("chinmay","deshpande")
amol.displayName()
chinmay.displayName()



class PersonB:

    # class variable
    country = "India"

    def __init__(self,fn,ln):
        # instance varibales
        self.firstName  = fn 
        self.lastName = ln

    # instance method
    def displayName(self):
        print(self.frstName + self.lastName)

    # class method
    @classmethod
    def changeCountry(cls):
        cls.country = "INDIA"

amolB = PersonB("amolB","RaoB")
amolC= PersonB("amolC","RaoC")
amolD = PersonB("amolC","RaoC")

print(amolB.firstName)
print(amolB.lastName)
print(amolB.country)

print(amolC.firstName)
print(amolC.lastName)
print(amolC.country)

print(amolD.firstName)
print(amolD.lastName)
print(amolD.country)

amolC.country = "bharat"
print(amolC.country)
print(amolB.country)
print(amolD.country)

PersonB.changeCountry()
print(amolB.country)
print(amolD.country)
