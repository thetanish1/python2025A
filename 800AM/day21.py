
# instance variable 
# class variable 
# instance method 
# class level method 
# access method 
# mutator method
# static method


class Person:

    # class level variable
    country = "India"
    # constructor
    def __init__(self,fn,ln):
        # instance level
        self.firstName = fn 
        self.lastName = ln 
    # instance
    # accessor method
    def displayName(self):
        print(Person.country)
        return self.firstName + self.lastName
    
    # instance
    # mutator method
    def updateFirstName(self,nfn):
        self.firstName = nfn
        return self.firstName
    

    @classmethod
    def updateCountry(cls,ucountry):
        Person.country = ucountry


chinmay = Person("chinmay","deshpande")
amol = Person("amol","rao")

print(chinmay.displayName())
print(chinmay.firstName)
print(chinmay.lastName)

chinmay.updateFirstName("chinmay d")
print(chinmay.firstName)
print(chinmay.lastName)
    
print(chinmay.country)
print(amol.country)

chinmay.country = "bharat"

print(chinmay.country)
print(amol.country)

sarika = Person("sarika","pansare")
print(sarika.country)

Person.updateCountry("INDIA")

print(chinmay.country) # bharat
print(amol.country) # INDIA
print(sarika.country) # INDIA


class Bank:

    country = "INDIA"
    def __init__(self,fullName,balance):
        self.fullName = fullName
        self.balance = balance
        self.transactions =  []

    
    # deposit method which will return balance


    # withdrawl method which will return balance


    # last 5 transactions


    # displayFullName


# class objects 