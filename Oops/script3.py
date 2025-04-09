# methods

# instance method 
    #  accessor methods 
    #  mutator methods
    # class  methods 
    # static methods 

# class Person:
#     # class level attribute
#     country = "india"
#     count = 0

#     # constructor 
#     def __init__(self,fn,ln,age):
#         self.firstName = fn 
#         self.lastName = ln
#         self.age = age
#         Person.count = Person.count + 1
#     # Instance methods
#     #instance - accessor methods 
#     def displayName(self):
#         print(self.firstName + self.lastName)
#         return self.firstName + self.lastName

#     # instance - updateAge - mutator methods
#     def updateAge(self,ag):
#         self.age = ag

#     # class level method 
#     @classmethod
#     def updateCountry(cls,countryName):
#         cls.country  = countryName

#     @staticmethod
#     def totalNumberOfCounts():
#         print(Person.count)

# amol = Person("amol","rao",23)
# sarika = Person("sarika","pansare",34)
# satish = Person("satish","rao",34) 
# poorva = Person("poorva","vyas",45)


# print(amol.country)
# print(sarika.country)
# print(satish.country)

# Person.updateCountry("bharat")
# print(amol.country)
# print(sarika.country)
# print(satish.country)

# amol.country = "USA"
# print(amol.country)
# print(sarika.country)
# print(satish.country)
# Person.totalNumberOfCounts()
class Bank:
    country = "India"
    count = 0
    def __init__(self,fullName,balance):
        self.balance = balance
        self.fullName = fullName
        self.transactions = []
        Bank.count = Bank.count + 1
    #method to retrive the balane 
    def getBalance(self):
        return self.balance

    #method to deposit()
    def deposit(self,amt):
        self.balance  = self.balance + amt
        self.transactions.append(amt)
        return self.balance
    
    # method to withdraw()
    def withdrawl(self,amt):
        if amt <= self.balance:
            self.transactions.append(-amt)
            self.balance = self.balance  - amt 
        else:
            print("Insufficient balance")
        return self.balance
    
    #method to show last 5 transaction 
    def last_five_transactions(self):
        return self.transactions[-5::]

    #method to show number of accounts created
    @staticmethod
    def totalAccounts():
        return Bank.count

    # method to change country name for all acc holders
    @classmethod
    def changeCountry(cls,countryName):
        cls.country = countryName

amol = Bank("amol",12300)  
chinmay = Bank("chinmay",10000000000000)  
gauri = Bank("gauri",12300000000)  
sarika = Bank("sarika",12300000000)  
vedant = Bank("vedant",123000000000000000)  


amol.withdrawl(110)   
amol.withdrawl(11)  
amol.withdrawl(10)  
amol.deposit(10)
amol.deposit(1000)
amol.deposit(100000)  

print(amol.last_five_transactions())
print(amol.country)
Bank.changeCountry("bharat")
print(amol.country)
accounts = Bank.totalAccounts()
print(accounts)
