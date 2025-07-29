
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



class Bank:
    country = "India"
    count = 0

    def __init__(self,fullName,bal):
        self.fullName = fullName
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1


    def deposit(self,amt):
        self.balance = self.balance + amt
        self.transactions.append(amt)
        return self.balance
    
    def withdrawl(self,amt):
        if amt < self.balance:
            self.balance = self.balance - amt
            self.transactions.append(-amt)
            return self.balance
        else:
            print("insufficient balance")

    def last5transaction(self):
        return self.transactions[-5:]

    @classmethod
    def updateCountry(cls,updateCountry):
        Bank.country = updateCountry

    @staticmethod
    def totalAcc():
        print(Bank.count)

chinmay = Bank("chinmay deshpande",100)
sarika = Bank("sarika pansare",10)
poorva = Bank("poorva vyas",5)

Bank.totalAcc()
poorva.deposit(10)
poorva.deposit(10)
poorva.deposit(10)
poorva.deposit(10)
poorva.deposit(10)
poorva.deposit(10)
poorva.withdrawl(10)
print(poorva.last5transaction())


